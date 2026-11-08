"""Fragment, reconstruct, and replicate USIRMS on MySQL/MariaDB.

Live evidence:
  - horizontal fragments by campus (schemas usirms_frag_main / usirms_frag_north)
  - reconstruction UNION equals global student count
  - primary usirms -> replica schema usirms_replica apply
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from shared.mysql_db import connect, connect_server, ensure_database  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"

FRAG_DDL = """
CREATE TABLE student_fragment (
    student_id   INT          NOT NULL,
    matric_no    VARCHAR(32)  NOT NULL,
    first_name   VARCHAR(60)  NOT NULL,
    last_name    VARCHAR(60)  NOT NULL,
    email        VARCHAR(120) NOT NULL,
    status       VARCHAR(16)  NOT NULL,
    programme_id INT          NOT NULL,
    campus_code  VARCHAR(8)   NOT NULL,
    PRIMARY KEY (student_id),
    UNIQUE KEY uk_frag_matric (matric_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""


def write_fragment(campus_code: str, schema: str) -> int:
    ensure_database(schema)
    src = connect("usirms")
    dst = connect(schema)
    try:
        dst.execute("DROP TABLE IF EXISTS student_fragment")
        dst.execute(FRAG_DDL)
        rows = src.execute(
            """
            SELECT s.student_id, s.matric_no, s.first_name, s.last_name, s.email,
                   s.status, s.programme_id, c.campus_code
            FROM student s
            JOIN campus c ON c.campus_id = s.campus_id
            WHERE c.campus_code = %s
            """,
            (campus_code,),
        ).fetchall()
        dst.executemany(
            "INSERT INTO student_fragment VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            [tuple(r.values()) for r in rows],
        )
        dst.commit()
        return len(rows)
    finally:
        src.close()
        dst.close()


def reconstruct_count() -> tuple[int, int, int, int]:
    conn = connect_server()
    try:
        m = conn.execute("SELECT COUNT(*) AS n FROM usirms_frag_main.student_fragment").fetchone()["n"]
        n = conn.execute("SELECT COUNT(*) AS n FROM usirms_frag_north.student_fragment").fetchone()["n"]
        distinct = conn.execute(
            """
            SELECT COUNT(*) AS n FROM (
                SELECT matric_no FROM usirms_frag_main.student_fragment
                UNION
                SELECT matric_no FROM usirms_frag_north.student_fragment
            ) u
            """
        ).fetchone()["n"]
        overlap = conn.execute(
            """
            SELECT COUNT(*) AS n
            FROM usirms_frag_main.student_fragment m
            JOIN usirms_frag_north.student_fragment n ON n.matric_no = m.matric_no
            """
        ).fetchone()["n"]
        return m, n, distinct, overlap
    finally:
        conn.close()


def clone_schema_to_replica() -> None:
    """Copy table structures + data from usirms into usirms_replica (logical replica)."""
    ensure_database("usirms_replica")
    src = connect("usirms")
    tables = src.execute(
        """
        SELECT TABLE_NAME AS name
        FROM information_schema.TABLES
        WHERE TABLE_SCHEMA = 'usirms' AND TABLE_TYPE = 'BASE TABLE'
        ORDER BY TABLE_NAME
        """
    ).fetchall()
    src.close()
    admin = connect_server()
    try:
        admin.execute("SET FOREIGN_KEY_CHECKS = 0")
        for row in tables:
            name = row["name"]
            admin.execute(f"DROP TABLE IF EXISTS usirms_replica.`{name}`")
            admin.execute(f"CREATE TABLE usirms_replica.`{name}` LIKE usirms.`{name}`")
            admin.execute(f"INSERT INTO usirms_replica.`{name}` SELECT * FROM usirms.`{name}`")
        admin.execute("SET FOREIGN_KEY_CHECKS = 1")
        admin.commit()
    finally:
        admin.close()


def replicate() -> list[str]:
    cleanup = connect("usirms")
    try:
        cleanup.execute("DELETE FROM transcript_issue WHERE purpose = 'Distributed replica test'")
        cleanup.commit()
    finally:
        cleanup.close()
    clone_schema_to_replica()
    primary = connect("usirms")
    secondary = connect("usirms_replica")
    notes = []
    try:
        before = secondary.execute(
            "SELECT current_level, status FROM student WHERE matric_no = 'RU/CSC/2024/001'"
        ).fetchone()
        notes.append(
            f"replica before apply: level={before['current_level']} status={before['status']}"
        )
        primary.execute("START TRANSACTION")
        primary.execute(
            """
            INSERT INTO transcript_issue (student_id, requested_on, purpose, status)
            SELECT student_id, NOW(), 'Distributed replica test', 'Requested'
            FROM student WHERE matric_no = 'RU/CSC/2024/001'
            """
        )
        primary.execute("COMMIT")
        row = primary.execute(
            """
            SELECT issue_id, purpose, status
            FROM transcript_issue
            WHERE purpose = 'Distributed replica test'
            ORDER BY issue_id DESC LIMIT 1
            """
        ).fetchone()
        notes.append(f"primary committed issue_id={row['issue_id']} status={row['status']}")
        stale = secondary.execute(
            "SELECT COUNT(*) AS n FROM transcript_issue WHERE purpose = 'Distributed replica test'"
        ).fetchone()["n"]
        notes.append(f"replica before catch-up: matching rows={stale} (expected 0)")
        full = primary.execute(
            """
            SELECT issue_id, student_id, requested_on, issued_on, issued_by, purpose, status
            FROM transcript_issue WHERE issue_id = %s
            """,
            (row["issue_id"],),
        ).fetchone()
        secondary.commit()
        secondary.execute(
            """
            INSERT INTO transcript_issue
                (issue_id, student_id, requested_on, issued_on, issued_by, purpose, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            tuple(full.values()),
        )
        secondary.commit()
        caught = secondary.execute(
            "SELECT COUNT(*) AS n FROM transcript_issue WHERE purpose = 'Distributed replica test'"
        ).fetchone()["n"]
        notes.append(f"replica after apply: matching rows={caught} (expected 1)")
        notes.append(
            "Replication style: primary schema + logical replica catch-up (strong consistency after apply)."
        )
        notes.append("During the gap the replica was available but stale (eventual consistency / DBASE).")
    finally:
        primary.close()
        secondary.close()
    return notes


def route_query(matric: str) -> str:
    prefix = matric.split("/")[1]
    return "MAIN" if prefix in {"CSC", "MTH", "ACC"} else "NORTH"


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    src = connect("usirms")
    try:
        global_n = src.execute("SELECT COUNT(*) AS n FROM student").fetchone()["n"]
    finally:
        src.close()
    main_n = write_fragment("MAIN", "usirms_frag_main")
    north_n = write_fragment("NORTH", "usirms_frag_north")
    m, n, distinct, overlap = reconstruct_count()
    notes = replicate()
    ada_site = route_query("RU/CSC/2024/001")
    eng_site = route_query("RU/ENG/2022/0005")

    lines = [
        "USIRMS distributed database exercise",
        f"generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "DBMS: MySQL/MariaDB schemas usirms / usirms_frag_main / usirms_frag_north / usirms_replica",
        "",
        "Horizontal fragmentation (derived attribute: campus_code)",
        f"global students: {global_n}",
        f"MAIN fragment rows: {main_n}",
        f"NORTH fragment rows: {north_n}",
        f"reconstruction UNION count: {distinct}",
        f"fragment overlap: {overlap}",
        "Correctness: MAIN + NORTH = global and overlap = 0"
        if main_n + north_n == global_n == distinct and overlap == 0
        else "WARNING: reconstruction does not match the global table",
        "",
        "Location transparency (directory routing, not a full DDBMS)",
        f"RU/CSC/2024/001 -> {ada_site} fragment",
        f"RU/ENG/2022/0005 -> {eng_site} fragment",
        "",
        "Replication",
        *notes,
        "",
        "CAP choice for this case study:",
        "- Grade and fee writes: CP. Refuse the write if the primary is unreachable.",
        "- Timetable / catalogue reads: AP. A campus may serve a slightly stale replica.",
        "See README and 01-architecture.md.",
    ]
    (EVIDENCE / "distributed_run.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
