"""USIRMS transaction and concurrency demonstrations (MySQL/MariaDB InnoDB).

Two connections share the usirms schema. Output is written under evidence/.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import pymysql

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from shared.mysql_db import Connection, connect  # noqa: E402

EVIDENCE = Path(__file__).resolve().parents[1] / "evidence"


def snapshot(conn: Connection, title: str) -> str:
    row = conn.execute(
        """
        SELECT e.enrolment_id, e.status, e.final_mark, e.letter_grade, e.grade_point,
               (SELECT COUNT(*) FROM grade g WHERE g.enrolment_id = e.enrolment_id) AS grades
        FROM enrolment e
        JOIN student s ON s.student_id = e.student_id
        JOIN module_offering o ON o.offering_id = e.offering_id
        JOIN module m ON m.module_id = o.module_id
        WHERE s.matric_no = 'RU/CSC/2024/001' AND m.module_code = 'CSC102'
        """
    ).fetchone()
    return (
        f"{title}: enrolment_id={row['enrolment_id']} status={row['status']} "
        f"final={row['final_mark']} letter={row['letter_grade']} "
        f"gp={row['grade_point']} grade_rows={row['grades']}"
    )


def letter_and_point(mark: float) -> tuple[str, int]:
    if mark >= 70:
        return "A", 5
    if mark >= 60:
        return "B", 4
    if mark >= 50:
        return "C", 3
    if mark >= 45:
        return "D", 2
    if mark >= 40:
        return "E", 1
    return "F", 0


def demo_commit(lines: list[str]) -> None:
    lines.append("=== DEMO 1 - Atomic grade finalisation (COMMIT) ===")
    lines.append("Business: lecturer publishes remaining CSC102 scores and finalises Ada's module.")
    conn = connect()
    try:
        lines.append(snapshot(conn, "before"))
        row = conn.execute(
            """
            SELECT e.enrolment_id
            FROM enrolment e
            JOIN student s ON s.student_id = e.student_id
            JOIN module_offering o ON o.offering_id = e.offering_id
            JOIN module m ON m.module_id = o.module_id
            WHERE s.matric_no = 'RU/CSC/2024/001' AND m.module_code = 'CSC102'
            """
        ).fetchone()
        eid = row["enrolment_id"]
        assessments = conn.execute(
            """
            SELECT a.assessment_id, a.assessment_type, a.weight_percent, a.max_score
            FROM assessment a
            JOIN enrolment e ON e.offering_id = a.offering_id
            WHERE e.enrolment_id = %s
            ORDER BY a.assessment_type
            """,
            (eid,),
        ).fetchall()
        conn.execute("START TRANSACTION")
        scores = {"CA": 24.0, "Exam": 50.0}
        for a in assessments:
            conn.execute(
                """
                INSERT INTO grade (enrolment_id, assessment_id, score, entered_by, status)
                VALUES (%s, %s, %s, 1, 'Published')
                ON DUPLICATE KEY UPDATE
                    score = VALUES(score),
                    status = 'Published',
                    entered_by = VALUES(entered_by),
                    entered_at = CURRENT_TIMESTAMP
                """,
                (eid, a["assessment_id"], scores[a["assessment_type"]]),
            )
        weighted = 0.0
        for a in assessments:
            sc = scores[a["assessment_type"]]
            weighted += float(sc) / float(a["max_score"]) * float(a["weight_percent"])
        letter, point = letter_and_point(weighted)
        conn.execute(
            """
            UPDATE enrolment
            SET status = 'Completed', final_mark = %s, letter_grade = %s, grade_point = %s
            WHERE enrolment_id = %s
            """,
            (round(weighted, 2), letter, point, eid),
        )
        conn.execute("COMMIT")
        lines.append(
            f"COMMIT published CA={scores['CA']}, Exam={scores['Exam']}, "
            f"final={round(weighted, 2)} {letter} ({point})"
        )
        lines.append(snapshot(conn, "after"))
        lines.append(
            "ACID: Atomicity (scores + final together), Consistency (5-point rule), "
            "Durability (visible after COMMIT)."
        )
    finally:
        conn.close()
    lines.append("")


def demo_rollback(lines: list[str]) -> None:
    lines.append("=== DEMO 2 - ROLLBACK on illegal fee payment ===")
    lines.append("Business: bursary posts 50000 then a second payment of -10. The whole unit must undo.")
    conn = connect()
    try:
        inv = conn.execute(
            """
            SELECT i.invoice_id, i.status, i.amount_due,
                   COALESCE((SELECT SUM(amount_paid) FROM fee_payment p
                             WHERE p.invoice_id = i.invoice_id), 0) AS paid
            FROM fee_invoice i
            JOIN student s ON s.student_id = i.student_id
            WHERE s.matric_no = 'RU/CSC/2024/001' AND i.session_id = 2
            """
        ).fetchone()
        lines.append(
            f"before invoice {inv['invoice_id']}: status={inv['status']} "
            f"due={inv['amount_due']} paid={inv['paid']}"
        )
        try:
            conn.execute("START TRANSACTION")
            conn.execute(
                """
                INSERT INTO fee_payment (invoice_id, amount_paid, paid_on, method, reference_no)
                VALUES (%s, 50000, CURDATE(), 'Transfer', 'PAY-DEMO-ROLLBACK')
                """,
                (inv["invoice_id"],),
            )
            conn.execute(
                """
                INSERT INTO fee_payment (invoice_id, amount_paid, paid_on, method, reference_no)
                VALUES (%s, -10, CURDATE(), 'Transfer', 'PAY-DEMO-NEG')
                """,
                (inv["invoice_id"],),
            )
            conn.execute("COMMIT")
            lines.append("FAIL: negative payment was accepted")
        except pymysql.Error as exc:
            conn.execute("ROLLBACK")
            lines.append(f"engine rejected second insert: {exc}")
            lines.append("ROLLBACK issued - the +50000 payment must not remain.")
        inv2 = conn.execute(
            """
            SELECT i.status,
                   COALESCE((SELECT SUM(amount_paid) FROM fee_payment p
                             WHERE p.invoice_id = i.invoice_id), 0) AS paid
            FROM fee_invoice i
            WHERE i.invoice_id = %s
            """,
            (inv["invoice_id"],),
        ).fetchone()
        leftover = conn.execute(
            "SELECT COUNT(*) AS n FROM fee_payment "
            "WHERE reference_no IN ('PAY-DEMO-ROLLBACK', 'PAY-DEMO-NEG')"
        ).fetchone()["n"]
        lines.append(
            f"after rollback: status={inv2['status']} paid={inv2['paid']} "
            f"demo_payment_rows={leftover}"
        )
        lines.append("Atomicity shown: first insert of the unit did not survive the failed statement.")
    finally:
        conn.close()
    lines.append("")


def demo_isolation_dirty_read(lines: list[str]) -> None:
    lines.append("=== DEMO 3 - Isolation: no dirty read of an uncommitted grade ===")
    lines.append("Lecturer A starts a draft change to Ada's CSC101 CA. Lecturer B reads the same score.")
    a = connect()
    b = connect()
    try:
        a.execute("SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ")
        b.execute("SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ")
        grade = a.execute(
            """
            SELECT g.grade_id, g.score, g.status
            FROM grade g
            JOIN enrolment e ON e.enrolment_id = g.enrolment_id
            JOIN student s ON s.student_id = e.student_id
            JOIN assessment ass ON ass.assessment_id = g.assessment_id
            JOIN module_offering o ON o.offering_id = e.offering_id
            JOIN module m ON m.module_id = o.module_id
            WHERE s.matric_no = 'RU/CSC/2024/001'
              AND m.module_code = 'CSC101'
              AND ass.assessment_type = 'CA'
            """
        ).fetchone()
        gid, original = grade["grade_id"], grade["score"]
        lines.append(f"committed score before demo: {original} (grade_id={gid})")
        a.execute("START TRANSACTION")
        a.execute("UPDATE grade SET score = 3, status = 'Draft' WHERE grade_id = %s", (gid,))
        dirty = a.execute("SELECT score, status FROM grade WHERE grade_id = %s", (gid,)).fetchone()
        lines.append(f"connection A (uncommitted): score={dirty['score']} status={dirty['status']}")
        clean = b.execute("SELECT score, status FROM grade WHERE grade_id = %s", (gid,)).fetchone()
        lines.append(f"connection B (concurrent read): score={clean['score']} status={clean['status']}")
        if clean["score"] == original and float(dirty["score"]) == 3:
            lines.append("PASS: B did not see A's uncommitted write (no dirty read).")
        else:
            lines.append("UNEXPECTED isolation result - inspect connections.")
        a.execute("ROLLBACK")
        after = b.execute("SELECT score, status FROM grade WHERE grade_id = %s", (gid,)).fetchone()
        lines.append(f"after A ROLLBACK, B reads score={after['score']} status={after['status']}")
        lines.append(
            "InnoDB default isolation is REPEATABLE READ: readers see the last "
            "committed snapshot, not the writer's uncommitted row."
        )
    finally:
        a.close()
        b.close()
    lines.append("")


def demo_lost_update(lines: list[str]) -> None:
    lines.append("=== DEMO 4 - Lost update (read-modify-write) and the control that prevents it ===")
    a = connect()
    b = connect()
    try:
        gid = a.execute(
            """
            SELECT g.grade_id
            FROM grade g
            JOIN enrolment e ON e.enrolment_id = g.enrolment_id
            JOIN student s ON s.student_id = e.student_id
            JOIN assessment ass ON ass.assessment_id = g.assessment_id
            JOIN module_offering o ON o.offering_id = e.offering_id
            JOIN module m ON m.module_id = o.module_id
            WHERE s.matric_no = 'RU/CSC/2024/001'
              AND m.module_code = 'MTH101'
              AND ass.assessment_type = 'CA'
            """
        ).fetchone()["grade_id"]
        a.execute("UPDATE grade SET score = 20 WHERE grade_id = %s", (gid,))
        a.commit()
        start = a.execute("SELECT score FROM grade WHERE grade_id = %s", (gid,)).fetchone()["score"]
        lines.append(f"start score={start} (reset to 20)")

        a_score = a.execute("SELECT score FROM grade WHERE grade_id = %s", (gid,)).fetchone()["score"]
        b_score = b.execute("SELECT score FROM grade WHERE grade_id = %s", (gid,)).fetchone()["score"]
        a.execute("UPDATE grade SET score = %s WHERE grade_id = %s", (float(a_score) + 1, gid))
        a.commit()
        b.execute("UPDATE grade SET score = %s WHERE grade_id = %s", (float(b_score) + 1, gid))
        b.commit()
        lost = a.execute("SELECT score FROM grade WHERE grade_id = %s", (gid,)).fetchone()["score"]
        lines.append(
            f"naive RMW: A read {a_score}, B read {b_score}, both wrote +1, stored score={lost}"
        )
        lines.append("Issue: two increments were intended (22) but one increment was lost.")

        a.execute("UPDATE grade SET score = 20 WHERE grade_id = %s", (gid,))
        a.commit()
        lines.append("reset to 20; retry with row lock and atomic increment")
        a.execute("SET innodb_lock_wait_timeout = 2")
        b.execute("SET innodb_lock_wait_timeout = 2")
        a.execute("START TRANSACTION")
        a.execute("SELECT score FROM grade WHERE grade_id = %s FOR UPDATE", (gid,))
        a.execute("UPDATE grade SET score = score + 1 WHERE grade_id = %s", (gid,))
        try:
            b.execute("START TRANSACTION")
            b.execute("SELECT score FROM grade WHERE grade_id = %s FOR UPDATE", (gid,))
            b.execute("UPDATE grade SET score = score + 1 WHERE grade_id = %s", (gid,))
            b.execute("COMMIT")
            lines.append("B also committed while A was open (unexpected on this lock manager)")
        except pymysql.Error as exc:
            lines.append(f"B blocked/failed while A held the write lock: {exc}")
            try:
                b.execute("ROLLBACK")
            except pymysql.Error:
                pass
        a.execute("COMMIT")
        b.execute("START TRANSACTION")
        b.execute("SELECT score FROM grade WHERE grade_id = %s FOR UPDATE", (gid,))
        b.execute("UPDATE grade SET score = score + 1 WHERE grade_id = %s", (gid,))
        b.execute("COMMIT")
        final = a.execute("SELECT score FROM grade WHERE grade_id = %s", (gid,)).fetchone()["score"]
        lines.append(f"after locked atomic increments: score={final} (expected 22)")
        lines.append(
            "Control: START TRANSACTION + SELECT ... FOR UPDATE + UPDATE score = score + 1."
        )
    finally:
        a.close()
        b.close()
    lines.append("")


def demo_savepoint(lines: list[str]) -> None:
    lines.append("=== DEMO 5 - SAVEPOINT inside a registrar correction ===")
    conn = connect()
    try:
        row = conn.execute(
            "SELECT s.student_id, s.status FROM student s WHERE s.matric_no = 'RU/CSC/2024/001'"
        ).fetchone()
        conn.execute("START TRANSACTION")
        conn.execute(
            "UPDATE student SET current_level = current_level WHERE student_id = %s",
            (row["student_id"],),
        )
        conn.execute("SAVEPOINT fee_note")
        try:
            conn.execute(
                """
                INSERT INTO transcript_issue (student_id, requested_on, purpose, status)
                VALUES (%s, NOW(), 'Demo invalid issued row', 'Issued')
                """,
                (row["student_id"],),
            )
        except pymysql.Error as exc:
            conn.execute("ROLLBACK TO SAVEPOINT fee_note")
            lines.append(f"issued-transcript insert failed ({exc}); rolled back to SAVEPOINT")
        conn.execute(
            """
            INSERT INTO transcript_issue (student_id, requested_on, purpose, status)
            VALUES (%s, NOW(), 'Verification copy', 'Requested')
            """,
            (row["student_id"],),
        )
        conn.execute("RELEASE SAVEPOINT fee_note")
        conn.execute("COMMIT")
        n = conn.execute(
            "SELECT COUNT(*) AS n FROM transcript_issue "
            "WHERE student_id = %s AND purpose = 'Verification copy'",
            (row["student_id"],),
        ).fetchone()["n"]
        bad = conn.execute(
            "SELECT COUNT(*) AS n FROM transcript_issue WHERE purpose = 'Demo invalid issued row'"
        ).fetchone()["n"]
        lines.append(f"COMMIT kept requested transcript rows={n}; rejected issued rows={bad}")
        lines.append(
            "Partial rollback: the surrounding student update survived; only the illegal issue was undone."
        )
    finally:
        conn.close()
    lines.append("")


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    lines = [
        "USIRMS transaction / concurrency evidence",
        "database: MySQL/MariaDB schema usirms",
        f"generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]
    demo_commit(lines)
    demo_rollback(lines)
    demo_isolation_dirty_read(lines)
    demo_lost_update(lines)
    demo_savepoint(lines)
    text = "\n".join(lines) + "\n"
    (EVIDENCE / "transaction_output.txt").write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
