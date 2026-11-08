"""Export USIRMS into three NoSQL shapes and run equivalent lookups.

1. Document store  - one JSON file per student (enrolments and grades nested)
2. Key-value store - timetable and fee-balance entries keyed by matric number
3. Graph           - module prerequisite adjacency + BFS eligibility path

This is a local, inspectable implementation of the four NoSQL families
discussed in the module (document, key-value, column is discussed but not
the primary build; graph is implemented). It does not replace the relational
system of record.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict, deque
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from shared.mysql_db import Connection, connect  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EVIDENCE = ROOT / "evidence"


def _json_default(obj: object) -> object:
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, time):
        return obj.isoformat()
    if isinstance(obj, timedelta):
        total = int(obj.total_seconds())
        h, rem = divmod(total, 3600)
        m, s = divmod(rem, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def _dumps(obj: object) -> str:
    return json.dumps(obj, indent=2, default=_json_default)


def export_documents(conn: Connection, limit: int | None) -> int:
    doc_dir = DATA / "documents"
    doc_dir.mkdir(parents=True, exist_ok=True)
    for old in doc_dir.glob("*.json"):
        old.unlink()

    students = conn.execute(
        """
        SELECT s.*, p.programme_code, p.programme_name, d.department_code, d.department_name,
               c.campus_code, adv.staff_number AS advisor_number,
               CONCAT(adv.first_name, ' ', adv.last_name) AS advisor_name
        FROM student s
        JOIN programme p ON p.programme_id = s.programme_id
        JOIN department d ON d.department_id = p.department_id
        JOIN campus c ON c.campus_id = s.campus_id
        LEFT JOIN staff adv ON adv.staff_id = s.advisor_staff_id
        ORDER BY s.student_id
        """
    ).fetchall()
    if limit is not None:
        preferred = [s for s in students if s["matric_no"] == "RU/CSC/2024/001"]
        others = [s for s in students if s["matric_no"] != "RU/CSC/2024/001"]
        students = (preferred + others)[:limit]

    enrol_rows = conn.execute(
        """
        SELECT e.student_id, e.enrolment_id, e.status, e.final_mark, e.letter_grade, e.grade_point,
               e.enrolled_on, m.module_code, m.module_title, m.credit_units,
               sess.session_label, sem.semester_no,
               CONCAT(st.first_name, ' ', st.last_name) AS lecturer
        FROM enrolment e
        JOIN module_offering o ON o.offering_id = e.offering_id
        JOIN module m ON m.module_id = o.module_id
        JOIN semester sem ON sem.semester_id = o.semester_id
        JOIN academic_session sess ON sess.session_id = sem.session_id
        JOIN staff st ON st.staff_id = o.lecturer_staff_id
        """
    ).fetchall()
    grades = conn.execute(
        """
        SELECT g.enrolment_id, a.assessment_type, a.title, a.weight_percent, g.score, g.status
        FROM grade g
        JOIN assessment a ON a.assessment_id = g.assessment_id
        """
    ).fetchall()
    grades_by_enr = defaultdict(list)
    for g in grades:
        grades_by_enr[g["enrolment_id"]].append(
            {
                "type": g["assessment_type"],
                "title": g["title"],
                "weight_percent": g["weight_percent"],
                "score": g["score"],
                "status": g["status"],
            }
        )
    enrol_by_student = defaultdict(list)
    for e in enrol_rows:
        enrol_by_student[e["student_id"]].append(
            {
                "module_code": e["module_code"],
                "module_title": e["module_title"],
                "credit_units": e["credit_units"],
                "session": e["session_label"],
                "semester": e["semester_no"],
                "lecturer": e["lecturer"],
                "status": e["status"],
                "final_mark": e["final_mark"],
                "letter_grade": e["letter_grade"],
                "grade_point": e["grade_point"],
                "enrolled_on": e["enrolled_on"],
                "assessments": grades_by_enr[e["enrolment_id"]],
            }
        )

    for s in students:
        doc = {
            "_id": s["matric_no"],
            "type": "student",
            "name": {"first": s["first_name"], "last": s["last_name"]},
            "email": s["email"],
            "status": s["status"],
            "current_level": s["current_level"],
            "campus": s["campus_code"],
            "programme": {
                "code": s["programme_code"],
                "name": s["programme_name"],
                "department": s["department_code"],
            },
            "advisor": {"staff_number": s["advisor_number"], "name": s["advisor_name"]},
            "enrolments": enrol_by_student[s["student_id"]],
        }
        (doc_dir / f"{s['matric_no'].replace('/', '_')}.json").write_text(
            _dumps(doc), encoding="utf-8"
        )
    return len(students)


def export_kv(conn: Connection) -> int:
    kv_path = DATA / "kv_store.json"
    store: dict[str, object] = {}
    rows = conn.execute(
        """
        SELECT s.matric_no, md.module_code, ts.day_of_week, ts.start_time, ts.end_time, ts.venue
        FROM student s
        JOIN enrolment e ON e.student_id = s.student_id
        JOIN module_offering o ON o.offering_id = e.offering_id
        JOIN module md ON md.module_id = o.module_id
        JOIN semester sem ON sem.semester_id = o.semester_id
        JOIN timetable_slot ts ON ts.offering_id = o.offering_id
        WHERE sem.status = 'Open' AND e.status = 'Registered'
        """
    ).fetchall()
    by_student: dict[str, list] = defaultdict(list)
    for r in rows:
        by_student[r["matric_no"]].append(
            {
                "module": r["module_code"],
                "day": r["day_of_week"],
                "start": r["start_time"],
                "end": r["end_time"],
                "venue": r["venue"],
            }
        )
    for matric, slots in by_student.items():
        store[f"timetable:{matric}"] = slots

    bals = conn.execute(
        """
        SELECT s.matric_no, b.balance, b.status
        FROM v_invoice_balance b
        JOIN student s ON s.student_id = b.student_id
        JOIN academic_session sess ON sess.session_id = b.session_id
        WHERE sess.is_current = 1
        """
    ).fetchall()
    for r in bals:
        store[f"fees:{r['matric_no']}"] = {"balance": r["balance"], "status": r["status"]}

    kv_path.write_text(_dumps(store), encoding="utf-8")
    return len(store)


def export_graph(conn: Connection) -> dict:
    nodes = [
        {"id": r["module_code"], "title": r["module_title"], "cu": r["credit_units"]}
        for r in conn.execute("SELECT module_code, module_title, credit_units FROM module")
    ]
    edges = [
        {"from": r["prereq"], "to": r["module"], "type": "PREREQUISITE"}
        for r in conn.execute(
            """
            SELECT p.module_code AS prereq, m.module_code AS module
            FROM module_prerequisite mp
            JOIN module m ON m.module_id = mp.module_id
            JOIN module p ON p.module_id = mp.prerequisite_module_id
            """
        )
    ]
    graph = {"nodes": nodes, "edges": edges}
    (DATA / "graph.json").write_text(_dumps(graph), encoding="utf-8")
    return graph


def query_document(matric: str) -> dict:
    path = DATA / "documents" / f"{matric.replace('/', '_')}.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    completed = [e for e in doc["enrolments"] if e["status"] == "Completed" and e["grade_point"] is not None]
    cu = sum(e["credit_units"] for e in completed)
    gp = sum(e["grade_point"] * e["credit_units"] for e in completed)
    return {
        "matric": doc["_id"],
        "name": f"{doc['name']['first']} {doc['name']['last']}",
        "programme": doc["programme"]["name"],
        "enrolment_count": len(doc["enrolments"]),
        "cgpa": round(gp / cu, 2) if cu else None,
        "modules": [
            f"{e['module_code']} {e['letter_grade']} ({e['final_mark']})"
            for e in completed
        ],
    }


def query_kv(store: dict, matric: str) -> dict:
    return {
        "timetable": store.get(f"timetable:{matric}", []),
        "fees": store.get(f"fees:{matric}"),
    }


def graph_paths(graph: dict, start: str, goal: str) -> list[list[str]]:
    adj: dict[str, list[str]] = defaultdict(list)
    for e in graph["edges"]:
        adj[e["from"]].append(e["to"])
    found: list[list[str]] = []
    q = deque([[start]])
    while q:
        path = q.popleft()
        node = path[-1]
        if node == goal:
            found.append(path)
            continue
        for nxt in adj[node]:
            if nxt not in path:
                q.append(path + [nxt])
    return found


def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    conn = connect()
    try:
        n_docs = export_documents(conn, limit=12)
        n_kv = export_kv(conn)
        graph = export_graph(conn)
    finally:
        conn.close()

    store = json.loads((DATA / "kv_store.json").read_text(encoding="utf-8"))
    ada = query_document("RU/CSC/2024/001")
    kv = query_kv(store, "RU/CSC/2024/001")
    sample_tt_key = next((k for k in store if k.startswith("timetable:") and store[k]), None)
    sample_tt = {sample_tt_key: store[sample_tt_key]} if sample_tt_key else {}
    paths = graph_paths(graph, "CSC101", "MIT8103")

    ada_doc = json.loads(
        (DATA / "documents" / "RU_CSC_2024_001.json").read_text(encoding="utf-8")
    )
    (EVIDENCE / "document_ada.json").write_text(_dumps(ada_doc), encoding="utf-8")

    lines = [
        "USIRMS NoSQL implementation evidence",
        f"document files written: {n_docs}",
        f"key-value entries written: {n_kv}",
        f"graph nodes={len(graph['nodes'])} edges={len(graph['edges'])}",
        "",
        "Document lookup RU/CSC/2024/001 (no SQL at read time)",
        _dumps(ada),
        "",
        "Key-value lookup timetable:RU/CSC/2024/001 and fees:RU/CSC/2024/001",
        _dumps(kv),
        "(Ada has no open Registered offering after Portfolio 3 finalised CSC102.)",
        "Sample non-empty timetable key:",
        _dumps(sample_tt),
        "",
        "Graph: directed paths CSC101 -> MIT8103 (prerequisite chain)",
        _dumps(paths),
        "",
        "Read path: open JSON documents / kv_store.json / graph.json.",
        "Write path for official marks remains the relational database (Portfolio 1-3).",
    ]
    (EVIDENCE / "nosql_queries.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
