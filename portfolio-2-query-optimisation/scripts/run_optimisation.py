"""Run USIRMS reporting queries, capture plans before/after indexes, and time them.

Rebuilds the database at --scale full so join cardinality is large enough for
type=ALL vs type=ref to appear in EXPLAIN. Timings are measured with
time.perf_counter on this machine; they are not invented.
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(REPO))
from shared.mysql_db import Connection, connect  # noqa: E402

P1_BUILD = REPO / "portfolio-1-database-design" / "scripts" / "build_database.py"
EVIDENCE = ROOT / "evidence"
SQL_INDEXES = ROOT / "sql" / "indexes.sql"

SECONDARY_INDEXES = [
    ("idx_student_status_programme", "student"),
    ("idx_enrolment_student_status", "enrolment"),
    ("idx_enrolment_offering_status", "enrolment"),
    ("idx_enrolment_letter", "enrolment"),
    ("idx_grade_enrolment_status", "grade"),
    ("idx_offering_semester_lecturer", "module_offering"),
    ("idx_attendance_student_status", "attendance"),
    ("idx_invoice_session_status", "fee_invoice"),
]

QUERIES = {
    "Q1_transcript": """
        SELECT t.session_label, t.semester_no, t.module_code, t.module_title,
               t.credit_units, t.final_mark, t.letter_grade, t.grade_point,
               t.enrolment_status
        FROM v_transcript_line t
        WHERE t.matric_no = 'RU/CSC/2024/001'
        ORDER BY t.session_label, t.semester_no, t.module_code
    """,
    "Q2_csc_cgpa_rank": """
        SELECT s.matric_no, CONCAT(s.first_name, ' ', s.last_name) AS student_name,
               s.current_level, c.cgpa, c.credit_units_completed
        FROM student s
        JOIN programme p ON p.programme_id = s.programme_id
        JOIN department d ON d.department_id = p.department_id
        JOIN v_student_cgpa c ON c.student_id = s.student_id
        WHERE d.department_code = 'CSC' AND s.status = 'Active'
        ORDER BY c.cgpa DESC, s.matric_no
        LIMIT 15
    """,
    "Q2b_pushed_selection": """
        SELECT s.matric_no, CONCAT(s.first_name, ' ', s.last_name) AS student_name,
               s.current_level,
               ROUND(SUM(e.grade_point * m.credit_units) * 1.0 / SUM(m.credit_units), 2) AS cgpa,
               SUM(m.credit_units) AS credit_units_completed
        FROM student s
        JOIN programme p ON p.programme_id = s.programme_id
        JOIN department d ON d.department_id = p.department_id
        JOIN enrolment e ON e.student_id = s.student_id
        JOIN module_offering o ON o.offering_id = e.offering_id
        JOIN module m ON m.module_id = o.module_id
        WHERE d.department_code = 'CSC'
          AND s.status = 'Active'
          AND e.status = 'Completed'
          AND e.grade_point IS NOT NULL
        GROUP BY s.student_id, s.matric_no, s.first_name, s.last_name, s.current_level
        ORDER BY cgpa DESC, s.matric_no
        LIMIT 15
    """,
    "Q3_failure_rates": """
        SELECT m.module_code, m.module_title, COUNT(*) AS completed_enrolments,
               SUM(CASE WHEN e.letter_grade = 'F' THEN 1 ELSE 0 END) AS fails,
               ROUND(100.0 * SUM(CASE WHEN e.letter_grade = 'F' THEN 1 ELSE 0 END) / COUNT(*), 1)
                   AS fail_rate_pct
        FROM enrolment e
        JOIN module_offering o ON o.offering_id = e.offering_id
        JOIN module m ON m.module_id = o.module_id
        WHERE e.status = 'Completed'
        GROUP BY m.module_id, m.module_code, m.module_title
        HAVING COUNT(*) >= 5
        ORDER BY fail_rate_pct DESC, completed_enrolments DESC
    """,
    "Q4_outstanding_fees": """
        SELECT s.matric_no, CONCAT(s.first_name, ' ', s.last_name) AS student_name,
               sess.session_label, b.amount_due, b.amount_paid, b.balance, b.status
        FROM v_invoice_balance b
        JOIN student s ON s.student_id = b.student_id
        JOIN academic_session sess ON sess.session_id = b.session_id
        WHERE sess.is_current = 1 AND b.balance > 0
        ORDER BY b.balance DESC, s.matric_no
        LIMIT 20
    """,
    "Q5_lecturer_load": """
        SELECT st.staff_number, CONCAT(st.first_name, ' ', st.last_name) AS lecturer,
               d.department_name, COUNT(o.offering_id) AS offerings,
               COUNT(e.enrolment_id) AS enrolled_students
        FROM staff st
        JOIN department d ON d.department_id = st.department_id
        JOIN module_offering o ON o.lecturer_staff_id = st.staff_id
        JOIN semester sem ON sem.semester_id = o.semester_id
        LEFT JOIN enrolment e ON e.offering_id = o.offering_id AND e.status <> 'Dropped'
        WHERE sem.status = 'Open' AND st.role IN ('Lecturer', 'Advisor', 'HoD')
        GROUP BY st.staff_id, st.staff_number, st.first_name, st.last_name, d.department_name
        ORDER BY offerings DESC, enrolled_students DESC
    """,
    "Q6_low_attendance": """
        SELECT s.matric_no, CONCAT(s.first_name, ' ', s.last_name) AS student_name,
               m.module_code, COUNT(*) AS meetings,
               SUM(CASE WHEN a.status IN ('Present', 'Late') THEN 1 ELSE 0 END) AS attended,
               ROUND(100.0 * SUM(CASE WHEN a.status IN ('Present', 'Late') THEN 1 ELSE 0 END)
                     / COUNT(*), 1) AS attendance_pct
        FROM attendance a
        JOIN timetable_slot ts ON ts.slot_id = a.slot_id
        JOIN module_offering o ON o.offering_id = ts.offering_id
        JOIN module m ON m.module_id = o.module_id
        JOIN student s ON s.student_id = a.student_id
        GROUP BY s.student_id, s.matric_no, s.first_name, s.last_name, m.module_id, m.module_code
        HAVING attendance_pct < 75
        ORDER BY attendance_pct, s.matric_no
    """,
    "Q7_enrolment_census": """
        SELECT p.programme_code, sess.session_label, sem.semester_no,
               COUNT(e.enrolment_id) AS enrolments,
               COUNT(DISTINCT e.student_id) AS distinct_students
        FROM enrolment e
        JOIN student s ON s.student_id = e.student_id
        JOIN programme p ON p.programme_id = s.programme_id
        JOIN module_offering o ON o.offering_id = e.offering_id
        JOIN semester sem ON sem.semester_id = o.semester_id
        JOIN academic_session sess ON sess.session_id = sem.session_id
        WHERE e.status <> 'Dropped'
        GROUP BY p.programme_id, p.programme_code, sess.session_label, sem.semester_no
        ORDER BY sess.session_label, sem.semester_no, p.programme_code
    """,
    "Q8a_nested_subquery": """
        SELECT s.matric_no, s.first_name, s.last_name
        FROM student s
        WHERE s.status = 'Active'
          AND s.student_id IN (
                SELECT e.student_id
                FROM enrolment e
                WHERE e.status = 'Completed'
                  AND e.letter_grade = 'F'
                  AND e.offering_id IN (
                        SELECT o.offering_id
                        FROM module_offering o
                        JOIN module m ON m.module_id = o.module_id
                        WHERE m.department_id = (
                            SELECT department_id FROM department WHERE department_code = 'CSC'
                        )
                  )
          )
        ORDER BY s.matric_no
        LIMIT 20
    """,
    "Q8b_rewritten_join": """
        SELECT DISTINCT s.matric_no, s.first_name, s.last_name
        FROM student s
        JOIN enrolment e ON e.student_id = s.student_id
        JOIN module_offering o ON o.offering_id = e.offering_id
        JOIN module m ON m.module_id = o.module_id
        JOIN department d ON d.department_id = m.department_id
        WHERE s.status = 'Active'
          AND e.status = 'Completed'
          AND e.letter_grade = 'F'
          AND d.department_code = 'CSC'
        ORDER BY s.matric_no
        LIMIT 20
    """,
}


def explain(conn: Connection, sql: str) -> str:
    rows = conn.execute("EXPLAIN " + sql).fetchall()
    if not rows:
        return "(no plan)"
    lines = []
    for row in rows:
        table = row.get("table")
        access = row.get("type")
        key = row.get("key")
        extra = row.get("Extra")
        lines.append(
            f"id={row.get('id')} select_type={row.get('select_type')} "
            f"table={table} type={access} key={key} rows={row.get('rows')} Extra={extra}"
        )
    return "\n".join(lines)


def time_query(conn: Connection, sql: str, repeats: int = 15) -> tuple[float, int]:
    conn.execute(sql).fetchall()
    started = time.perf_counter()
    count = 0
    for _ in range(repeats):
        count = len(conn.execute(sql).fetchall())
    elapsed_ms = (time.perf_counter() - started) * 1000.0 / repeats
    return elapsed_ms, count


def write_rows(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("(no rows)\n", encoding="utf-8")
        return
    headers = list(rows[0].keys())
    lines = [" | ".join(headers)]
    lines.append("-|-".join("-" * len(h) for h in headers))
    for row in rows:
        lines.append(" | ".join("" if v is None else str(v) for v in row.values()))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def drop_secondary_indexes(conn: Connection) -> None:
    for name, table in SECONDARY_INDEXES:
        try:
            conn.execute(f"DROP INDEX {name} ON {table}")
        except Exception:
            conn.rollback()
    conn.commit()


def main() -> int:
    subprocess.check_call([sys.executable, str(P1_BUILD), "--scale", "full"])

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    for sub in ("results", "plans_before", "plans_after"):
        (EVIDENCE / sub).mkdir(exist_ok=True)

    conn = connect()
    try:
        drop_secondary_indexes(conn)
        conn.execute("ANALYZE TABLE student, enrolment, grade, module_offering, attendance, fee_invoice")

        timing_before: dict[str, tuple[float, int]] = {}
        timing_after: dict[str, tuple[float, int]] = {}

        for name, sql in QUERIES.items():
            (EVIDENCE / "plans_before" / f"{name}.txt").write_text(
                f"EXPLAIN — {name} (before secondary indexes)\n\n"
                + explain(conn, sql)
                + "\n",
                encoding="utf-8",
            )
            rows = conn.execute(sql).fetchall()
            write_rows(EVIDENCE / "results" / f"{name}.txt", rows)
            timing_before[name] = time_query(conn, sql)

        conn.executescript(SQL_INDEXES.read_text(encoding="utf-8"))
        conn.commit()

        index_list = conn.execute(
            """
            SELECT INDEX_NAME AS name, TABLE_NAME AS tbl,
                   GROUP_CONCAT(COLUMN_NAME ORDER BY SEQ_IN_INDEX) AS cols
            FROM information_schema.STATISTICS
            WHERE TABLE_SCHEMA = DATABASE()
              AND INDEX_NAME LIKE 'idx_%'
            GROUP BY INDEX_NAME, TABLE_NAME
            ORDER BY INDEX_NAME
            """
        ).fetchall()
        (EVIDENCE / "indexes_created.txt").write_text(
            "Secondary indexes created (MySQL/MariaDB)\n\n"
            + "\n".join(f"{row['name']} ON {row['tbl']} ({row['cols']})" for row in index_list)
            + "\n",
            encoding="utf-8",
        )

        for name, sql in QUERIES.items():
            (EVIDENCE / "plans_after" / f"{name}.txt").write_text(
                f"EXPLAIN — {name} (after secondary indexes + ANALYZE)\n\n"
                + explain(conn, sql)
                + "\n",
                encoding="utf-8",
            )
            timing_after[name] = time_query(conn, sql)

        lines = [
            "USIRMS query timings (MySQL/MariaDB, this machine)",
            "Each figure is the mean of 15 runs after one warmup, time.perf_counter().",
            "These are measured values, not estimates.",
            "",
            f"{'query':<22} {'rows':>6} {'before_ms':>10} {'after_ms':>10} {'delta_ms':>10}",
        ]
        for name in QUERIES:
            before_ms, count = timing_before[name]
            after_ms, _ = timing_after[name]
            lines.append(
                f"{name:<22} {count:6d} {before_ms:10.3f} {after_ms:10.3f} {after_ms - before_ms:10.3f}"
            )
        (EVIDENCE / "timings.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("\n".join(lines))
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
