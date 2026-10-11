"""Build the USIRMS MySQL/MariaDB database, seed it, and prove integrity rules.

Usage (from repository root):
    python portfolio-1-database-design/scripts/build_database.py
    python portfolio-1-database-design/scripts/build_database.py --scale full

--scale small  ~80 students  (default, fast rebuild)
--scale full   1200 students (used by Portfolio 2 plan comparisons)

Requires a running MySQL/MariaDB server. See ../dbeaver-connection.md
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

import pymysql

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(REPO))
from shared.mysql_db import Connection, connect, ensure_database  # noqa: E402

SQL_DIR = ROOT / "sql"
EVIDENCE = ROOT / "evidence"
SCHEMA = SQL_DIR / "schema.sql"
INTEGRITY = SQL_DIR / "integrity_tests.sql"

FIRST = [
    "Ada", "Chidi", "Fatima", "Ifeanyi", "Amina", "Tunde", "Ngozi", "Yusuf",
    "Blessing", "Emeka", "Hauwa", "Kunle", "Chioma", "Bala", "Funke", "Ibrahim",
    "Amaka", "Seyi", "Zainab", "Olu", "Kelechi", "Maryam", "Gbenga", "Ruth",
]
LAST = [
    "Okonkwo", "Adeyemi", "Bello", "Okeke", "Sule", "Musa", "Nwosu", "Lawal",
    "Eze", "Abdullahi", "Balogun", "Okafor", "Yakubu", "Adebayo", "Ibrahim",
    "Chukwu", "Mohammed", "Ojo", "Umar", "Nnamdi",
]


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


def load_schema(conn: Connection) -> None:
    conn.executescript(SCHEMA.read_text(encoding="utf-8"))


def seed(conn: Connection, student_count: int, rng: random.Random) -> None:
    cur = conn.cursor()

    campuses = [
        (1, "MAIN", "Main Campus", "Lagos"),
        (2, "NORTH", "North Campus", "Kaduna"),
    ]
    cur.executemany(
        "INSERT INTO campus VALUES (%s, %s, %s, %s)",
        campuses,
    )

    departments = [
        (1, "CSC", "Computer Science", "Computing and Informatics", 1),
        (2, "MTH", "Mathematics", "Science", 1),
        (3, "ACC", "Accounting", "Management Sciences", 1),
        (4, "ENG", "English", "Arts", 2),
        (5, "BIO", "Biological Sciences", "Science", 2),
        (6, "EDU", "Education", "Education", 2),
    ]
    cur.executemany(
        """INSERT INTO department
           (department_id, department_code, department_name, faculty_name, campus_id)
           VALUES (%s, %s, %s, %s, %s)""",
        departments,
    )

    staff_rows = [
        (1, "STF1001", "Halima", "Bello", "h.bello@riverside.test", "0802-222-0002", "Lecturer", 1, 1, "2016-09-01"),
        (2, "STF1002", "Chinedu", "Okeke", "c.okeke@riverside.test", "0802-222-0003", "HoD", 1, 1, "2012-02-01"),
        (3, "STF1003", "Aisha", "Sule", "a.sule@riverside.test", "0802-222-0004", "Advisor", 1, 1, "2018-01-15"),
        (4, "STF1004", "Peter", "Nwosu", "p.nwosu@riverside.test", "0802-222-0005", "Lecturer", 2, 1, "2015-04-01"),
        (5, "STF1005", "Lami", "Lawal", "l.lawal@riverside.test", "0802-222-0006", "HoD", 2, 1, "2013-09-01"),
        (6, "STF1006", "Grace", "Eze", "g.eze@riverside.test", "0802-222-0007", "Lecturer", 3, 1, "2017-01-10"),
        (7, "STF1007", "Umar", "Abdullahi", "u.abdullahi@riverside.test", "0802-222-0008", "HoD", 3, 1, "2011-11-01"),
        (8, "STF1008", "Tola", "Balogun", "t.balogun@riverside.test", "0802-222-0009", "Lecturer", 4, 1, "2019-03-01"),
        (9, "STF1009", "Karen", "Okafor", "k.okafor@riverside.test", "0802-222-0010", "HoD", 4, 1, "2014-06-01"),
        (10, "STF1010", "Musa", "Yakubu", "m.yakubu@riverside.test", "0802-222-0011", "Lecturer", 5, 1, "2016-02-01"),
        (11, "STF1011", "Funke", "Adebayo", "f.adebayo@riverside.test", "0802-222-0012", "HoD", 5, 1, "2010-08-01"),
        (12, "STF1012", "David", "Chukwu", "d.chukwu@riverside.test", "0802-222-0013", "Lecturer", 6, 1, "2018-10-01"),
        (13, "STF1013", "Rahila", "Mohammed", "r.mohammed@riverside.test", "0802-222-0014", "HoD", 6, 1, "2015-01-01"),
        (14, "STF1014", "Segun", "Ojo", "s.ojo@riverside.test", "0802-222-0015", "Advisor", 3, 1, "2019-09-01"),
        (15, "STF1015", "Nkechi", "Nnamdi", "n.nnamdi@riverside.test", "0802-222-0016", "Lecturer", 1, 1, "2020-01-08"),
        (16, "STF1016", "Yahaya", "Umar", "y.umar@riverside.test", "0802-222-0017", "Lecturer", 2, 1, "2021-02-01"),
        (17, "STF9001", "Ngozi", "Adeyemi", "registrar@riverside.test", "0803-333-0001", "Registrar", None, 1, "2010-03-01"),
        (18, "STF9002", "Ibrahim", "Musa", "admin@riverside.test", "0803-333-0002", "Admin", None, 1, "2011-07-01"),
    ]
    cur.executemany(
        """INSERT INTO staff
           (staff_id, staff_number, first_name, last_name, email, phone, role,
            department_id, is_active, hired_date)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        staff_rows,
    )

    cur.executemany(
        "INSERT INTO department_head VALUES (%s, %s, %s)",
        [(1, 2, "2022-08-01"), (2, 5, "2021-09-01"), (3, 7, "2020-01-01"),
         (4, 9, "2023-01-01"), (5, 11, "2019-08-01"), (6, 13, "2022-01-01")],
    )

    programmes = [
        (1, "BSC-CSC", "BSc Computer Science", "BSc", 4, 1),
        (2, "MIT-ADS", "MIT Advanced Database Systems", "MIT", 2, 1),
        (3, "BSC-MTH", "BSc Mathematics", "BSc", 4, 2),
        (4, "BSC-ACC", "BSc Accounting", "BSc", 4, 3),
        (5, "BA-ENG", "BA English", "BA", 4, 4),
        (6, "BSC-BIO", "BSc Biological Sciences", "BSc", 4, 5),
        (7, "BSC-EDU", "BSc Education", "BSc", 4, 6),
        (8, "PGD-ICT", "PGD Information Technology", "PGD", 1, 1),
    ]
    cur.executemany("INSERT INTO programme VALUES (%s, %s, %s, %s, %s, %s)", programmes)

    modules = [
        (1, "CSC101", "Introduction to Computing", 3, 1),
        (2, "CSC102", "Programming Fundamentals", 3, 1),
        (3, "CSC201", "Data Structures", 3, 1),
        (4, "CSC202", "Database Systems", 3, 1),
        (5, "MIT8103", "Advanced Database Systems", 3, 1),
        (6, "MIT8104", "Distributed Systems", 3, 1),
        (7, "MTH101", "Elementary Mathematics I", 3, 2),
        (8, "MTH102", "Elementary Mathematics II", 3, 2),
        (9, "MTH201", "Linear Algebra", 3, 2),
        (10, "ACC101", "Principles of Accounting", 3, 3),
        (11, "ACC201", "Financial Accounting", 3, 3),
        (12, "ENG101", "Use of English", 2, 4),
        (13, "ENG201", "Introduction to Literature", 3, 4),
        (14, "BIO101", "General Biology", 3, 5),
        (15, "BIO201", "Genetics", 3, 5),
        (16, "EDU101", "Foundations of Education", 3, 6),
        (17, "EDU201", "Curriculum Studies", 3, 6),
        (18, "GST101", "Communication in English", 2, 4),
        (19, "CSC301", "Operating Systems", 3, 1),
        (20, "CSC302", "Software Engineering", 3, 1),
        (21, "ACC301", "Management Accounting", 3, 3),
        (22, "MTH301", "Real Analysis", 3, 2),
        (23, "BIO301", "Microbiology", 3, 5),
        (24, "EDU301", "Educational Measurement", 3, 6),
    ]
    cur.executemany("INSERT INTO module VALUES (%s, %s, %s, %s, %s)", modules)

    curriculum = [
        (1, 1, 1, 1, 1), (1, 2, 1, 2, 1), (1, 7, 1, 1, 1), (1, 18, 1, 1, 1),
        (1, 3, 2, 1, 1), (1, 4, 2, 2, 1), (1, 19, 3, 1, 1), (1, 20, 3, 2, 1),
        (2, 5, 1, 1, 1), (2, 6, 1, 2, 1), (2, 4, 1, 1, 1),
        (3, 7, 1, 1, 1), (3, 8, 1, 2, 1), (3, 9, 2, 1, 1), (3, 22, 3, 1, 1),
        (4, 10, 1, 1, 1), (4, 11, 2, 1, 1), (4, 21, 3, 1, 1), (4, 18, 1, 1, 1),
        (5, 12, 1, 1, 1), (5, 13, 2, 1, 1), (5, 18, 1, 2, 1),
        (6, 14, 1, 1, 1), (6, 15, 2, 1, 1), (6, 23, 3, 1, 1),
        (7, 16, 1, 1, 1), (7, 17, 2, 1, 1), (7, 24, 3, 1, 1), (7, 18, 1, 1, 1),
        (8, 1, 1, 1, 1), (8, 4, 1, 1, 1),
    ]
    cur.executemany("INSERT INTO programme_module VALUES (%s, %s, %s, %s, %s)", curriculum)

    cur.executemany(
        "INSERT INTO module_prerequisite VALUES (%s, %s)",
        [(3, 1), (3, 2), (4, 1), (5, 4), (6, 5), (11, 10), (15, 14), (19, 3), (20, 3)],
    )

    cur.executemany(
        "INSERT INTO academic_session VALUES (%s, %s, %s, %s, %s)",
        [
            (1, "2024/2025", "2024-09-01", "2025-07-31", 0),
            (2, "2025/2026", "2025-09-01", "2026-07-31", 1),
        ],
    )
    cur.executemany(
        "INSERT INTO semester VALUES (%s, %s, %s, %s, %s, %s)",
        [
            (1, 1, 1, "2024-09-01", "2025-01-31", "Closed"),
            (2, 1, 2, "2025-02-01", "2025-07-31", "Closed"),
            (3, 2, 1, "2025-09-01", "2026-01-31", "Closed"),
            (4, 2, 2, "2026-02-01", "2026-07-31", "Open"),
        ],
    )

    lecturers_by_dept = {
        1: [1, 15],
        2: [4, 16],
        3: [6],
        4: [8],
        5: [10],
        6: [12],
    }
    offering_id = 0
    offerings: list[tuple[int, int, int, int, int]] = []
    for semester_id in (1, 2, 3, 4):
        for module_id, _code, _title, _cu, dept_id in modules:
            offering_id += 1
            lecturer = rng.choice(lecturers_by_dept[dept_id])
            offerings.append((offering_id, module_id, semester_id, lecturer, 120))
    cur.executemany("INSERT INTO module_offering VALUES (%s, %s, %s, %s, %s)", offerings)

    assessments: list[tuple] = []
    assessment_id = 0
    assessments_by_offering: dict[int, list[int]] = {}
    for oid, _mid, semester_id, _lec, _cap in offerings:
        due = {
            1: ("2024-11-15", "2025-01-18"),
            2: ("2025-04-15", "2025-06-20"),
            3: ("2025-11-15", "2026-01-20"),
            4: ("2026-04-15", "2026-06-20"),
        }[semester_id]
        assessment_id += 1
        ca_id = assessment_id
        assessments.append((ca_id, oid, "CA", f"CA offering {oid}", 30, 30, due[0]))
        assessment_id += 1
        ex_id = assessment_id
        assessments.append((ex_id, oid, "Exam", f"Exam offering {oid}", 70, 70, due[1]))
        assessments_by_offering[oid] = [ca_id, ex_id]
    cur.executemany("INSERT INTO assessment VALUES (%s, %s, %s, %s, %s, %s, %s)", assessments)

    advisors = [3, 14]
    students = []
    for i in range(1, student_count + 1):
        prog_id = ((i - 1) % 8) + 1
        campus_id = 1 if prog_id <= 4 else 2
        first = FIRST[(i - 1) % len(FIRST)]
        last = LAST[(i - 1) % len(LAST)]
        year = 2022 + ((i - 1) % 4)
        dept_code = {1: "CSC", 2: "CSC", 3: "MTH", 4: "ACC", 5: "ENG", 6: "BIO", 7: "EDU", 8: "CSC"}[prog_id]
        matric = f"RU/{dept_code}/{year}/{i:04d}"
        if i == 1:
            first, last, matric = "Ada", "Okonkwo", "RU/CSC/2024/001"
        level = min(4, 1 + ((i - 1) % 4))
        status = "Active" if i % 37 else "Suspended"
        students.append(
            (
                i,
                matric,
                first,
                last,
                f"student{i:04d}@riverside.test",
                f"{2000 + (i % 8):04d}-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
                ("F", "M", "X")[i % 3],
                year,
                prog_id,
                level,
                status,
                advisors[i % 2],
                campus_id,
            )
        )
    cur.executemany(
        """INSERT INTO student VALUES
           (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        students,
    )

    offering_by_mod_sem = {(row[1], row[2]): row[0] for row in offerings}
    enrolment_id = 0
    enrolments: list[tuple] = []
    grades: list[tuple] = []
    grade_id = 0

    for student in students:
        sid, _mat, _fn, _ln, _em, _dob, _g, _yr, prog_id, level, status, _adv, _cam = student
        if status != "Active":
            continue
        cur_mods = [
            row for row in curriculum
            if row[0] == prog_id and row[2] <= level
        ]
        # Closed semesters 1-3 get completed results; semester 4 is current.
        for pm in cur_mods:
            _pid, module_id, level_year, semester_no, _core = pm
            targets: set[int] = set()
            if level_year < level:
                targets.add(1 if semester_no == 1 else 2)
            elif level_year == level:
                targets.add(3 if semester_no == 1 else 4)
            for sem_id in sorted(targets):
                oid = offering_by_mod_sem[(module_id, sem_id)]
                enrolment_id += 1
                completed = sem_id < 4
                ca_id, ex_id = assessments_by_offering[oid]
                if completed:
                    ca_score = rng.randint(12, 30)
                    ex_score = rng.randint(25, 70)
                    final = round(ca_score / 30 * 30 + ex_score / 70 * 70, 2)
                    letter, point = letter_and_point(final)
                    enrolments.append(
                        (enrolment_id, sid, oid, "2024-09-10", "Completed", final, letter, point)
                    )
                    grade_id += 1
                    grades.append((grade_id, enrolment_id, ca_id, ca_score, 1, "2024-11-20", "Published"))
                    grade_id += 1
                    grades.append((grade_id, enrolment_id, ex_id, ex_score, 1, "2025-01-22", "Published"))
                else:
                    enrolments.append(
                        (enrolment_id, sid, oid, "2026-02-05", "Registered", None, None, None)
                    )
                    if rng.random() < 0.6:
                        ca_score = rng.randint(10, 30)
                        grade_id += 1
                        grades.append((grade_id, enrolment_id, ca_id, ca_score, 1, "2026-04-16", "Submitted"))

    cur.executemany("INSERT INTO enrolment VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", enrolments)
    cur.executemany(
        """INSERT INTO grade
           (grade_id, enrolment_id, assessment_id, score, entered_by, entered_at, status)
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        grades,
    )

    slot_id = 0
    slots = []
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for oid, _mid, semester_id, _lec, _cap in offerings:
        if semester_id != 4:
            continue
        slot_id += 1
        day = days[oid % 5]
        hour = 8 + (oid % 8)
        slots.append(
            (
                slot_id,
                oid,
                day,
                f"{hour:02d}:00",
                f"{hour + 2:02d}:00",
                f"LT{(oid % 12) + 1}",
                "Lecture",
            )
        )
    cur.executemany("INSERT INTO timetable_slot VALUES (%s, %s, %s, %s, %s, %s, %s)", slots)

    attendance_rows = []
    attendance_id = 0
    slot_by_offering = {row[1]: row[0] for row in slots}
    meeting_dates = ["2026-02-10", "2026-02-17", "2026-02-24", "2026-03-03"]
    for enr in enrolments:
        _eid, sid, oid, _on, status, *_rest = enr
        if status != "Registered" or oid not in slot_by_offering:
            continue
        for meet_date in meeting_dates:
            attendance_id += 1
            attendance_rows.append(
                (
                    attendance_id,
                    slot_by_offering[oid],
                    sid,
                    meet_date,
                    rng.choice(["Present", "Present", "Present", "Late", "Absent"]),
                )
            )
    cur.executemany("INSERT INTO attendance VALUES (%s, %s, %s, %s, %s)", attendance_rows)

    invoices = []
    payments = []
    payment_id = 0
    for student in students:
        sid = student[0]
        status = student[10]
        amount = 250000 if student[8] in (1, 3, 4, 5, 6, 7) else 350000
        paid_ratio = 1.0 if sid % 5 else (0.0 if sid % 7 == 0 else 0.5)
        if status == "Suspended":
            paid_ratio = 0.0
        paid = round(amount * paid_ratio, 2)
        inv_status = "Paid" if paid_ratio == 1 else ("Unpaid" if paid_ratio == 0 else "Partial")
        invoices.append((sid, sid, 2, amount, "2025-10-01", inv_status))
        if paid > 0:
            payment_id += 1
            payments.append((payment_id, sid, paid, "2025-09-20", "Transfer", f"PAY-REF-{sid:05d}"))
    cur.executemany("INSERT INTO fee_invoice VALUES (%s, %s, %s, %s, %s, %s)", invoices)
    cur.executemany("INSERT INTO fee_payment VALUES (%s, %s, %s, %s, %s, %s)", payments)

    cur.execute(
        """INSERT INTO transcript_issue
           (issue_id, student_id, requested_on, issued_on, issued_by, purpose, status)
           VALUES (1, 1, '2026-02-01', '2026-02-03', 17, 'Internship application', 'Issued')"""
    )
    conn.commit()


def table_counts(conn: Connection) -> list[tuple[str, int]]:
    names = [
        "campus", "department", "staff", "department_head", "programme", "module",
        "programme_module", "module_prerequisite", "student", "academic_session",
        "semester", "module_offering", "enrolment", "assessment", "grade",
        "timetable_slot", "attendance", "fee_invoice", "fee_payment", "transcript_issue",
    ]
    return [(n, conn.execute(f"SELECT COUNT(*) AS n FROM {n}").fetchone()["n"]) for n in names]


def run_integrity_tests(conn: Connection) -> list[str]:
    raw = INTEGRITY.read_text(encoding="utf-8")
    statements: list[str] = []
    buf: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("--"):
            continue
        buf.append(line)
        if stripped.endswith(";"):
            statements.append("\n".join(buf).strip())
            buf = []

    lines = ["USIRMS integrity tests - each case must be REJECTED by MySQL/MariaDB", ""]
    passed = 0
    for i, stmt in enumerate(statements, start=1):
        try:
            conn.execute(stmt)
            conn.commit()
            lines.append(f"[{i}] FAIL — statement was accepted (constraint missing)")
            lines.append(stmt)
            lines.append("")
        except pymysql.Error as exc:
            conn.rollback()
            passed += 1
            lines.append(f"[{i}] PASS — rejected as required")
            lines.append(f"    error: {exc}")
            preview = " ".join(stmt.split())[:140]
            lines.append(f"    sql: {preview}")
            lines.append("")
    lines.append(f"Result: {passed}/{len(statements)} illegal operations rejected.")
    if passed != len(statements):
        raise SystemExit("Integrity tests did not all fail as required.")
    return lines


def write_evidence(conn: Connection, integrity_lines: list[str]) -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    schema_info = conn.execute(
        """
        SELECT TABLE_NAME AS name,
               CASE TABLE_TYPE WHEN 'BASE TABLE' THEN 'table' ELSE 'view' END AS type
        FROM information_schema.TABLES
        WHERE TABLE_SCHEMA = DATABASE()
        ORDER BY type, name
        """
    ).fetchall()
    (EVIDENCE / "schema_created.txt").write_text(
        "USIRMS objects created (MySQL/MariaDB)\n\n"
        + "\n".join(f"{row['type']:5} {row['name']}" for row in schema_info)
        + "\n",
        encoding="utf-8",
    )
    counts = table_counts(conn)
    (EVIDENCE / "seed_counts.txt").write_text(
        "Row counts after seed\n\n"
        + "\n".join(f"{name:22} {count}" for name, count in counts)
        + f"\n\nTotal rows: {sum(c for _, c in counts)}\n",
        encoding="utf-8",
    )
    (EVIDENCE / "constraint_violations.txt").write_text(
        "\n".join(integrity_lines) + "\n",
        encoding="utf-8",
    )

    ada = conn.execute(
        """
        SELECT s.matric_no, s.first_name, s.last_name, p.programme_name,
               c.cgpa, c.credit_units_completed
        FROM student s
        JOIN programme p ON p.programme_id = s.programme_id
        LEFT JOIN v_student_cgpa c ON c.student_id = s.student_id
        WHERE s.matric_no = 'RU/CSC/2024/001'
        """
    ).fetchone()
    lines = conn.execute(
        """
        SELECT session_label, semester_no, module_code, module_title,
               credit_units, final_mark, letter_grade, grade_point
        FROM v_transcript_line
        WHERE matric_no = 'RU/CSC/2024/001'
        ORDER BY session_label, semester_no, module_code
        """
    ).fetchall()
    out = [
        "Worked example: Ada Okonkwo (from the normalisation discussion)",
        f"Matric: {ada['matric_no']}  {ada['first_name']} {ada['last_name']}",
        f"Programme: {ada['programme_name']}",
        f"CGPA: {ada['cgpa']} on {ada['credit_units_completed']} credit units",
        "",
        "Transcript lines",
        "session  sem  code    title                          cu  mark  lg  gp",
    ]
    for row in lines:
        out.append(
            f"{row['session_label']}  {row['semester_no']}    {row['module_code']:7} "
            f"{row['module_title'][:28]:28}  {row['credit_units']}  "
            f"{row['final_mark']!s:>5}  {row['letter_grade']}   {row['grade_point']}"
        )
    (EVIDENCE / "ada_okonkwo_transcript.txt").write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", choices=("small", "full"), default="small")
    args = parser.parse_args()
    student_count = 80 if args.scale == "small" else 1200
    rng = random.Random(8103)

    ensure_database()
    conn = connect()
    try:
        load_schema(conn)
        conn.commit()
        seed(conn, student_count, rng)
        integrity_lines = run_integrity_tests(conn)
        write_evidence(conn, integrity_lines)
    finally:
        conn.close()

    print("Database written to MySQL/MariaDB schema `usirms`")
    print(f"Evidence written to {EVIDENCE}")
    print(f"Scale={args.scale} students={student_count}")
    print("Open in DBeaver: 127.0.0.1:3306 / database usirms (see dbeaver-connection.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
