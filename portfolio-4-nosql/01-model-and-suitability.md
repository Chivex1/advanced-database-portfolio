# NoSQL models for USIRMS

The same Riverside University case study is remodelled here. The relational schema remains the **system of record** for grades and fees (ACID, Portfolios 1–3). NoSQL is used where the module says it fits: flexible aggregates, fast key lookup, and relationship traversal.

## Choice and justification

The module lists four primary NoSQL families. USIRMS uses three of them in this folder; the fourth is discussed and rejected as the primary store.

| Family | Chosen for | USIRMS payload | Why it fits | Why it does not replace SQL |
| --- | --- | --- | --- | --- |
| **Document** (primary build) | Student transcript aggregate | One JSON document per student: profile + nested enrolments + assessments | A registrar read is “this student, all modules”. Embedding avoids the six-way join of Q1 | Cross-student failure rates and referential integrity still need relations |
| **Key-value** | Session cache | `timetable:{matric}`, `fees:{matric}` | Mobile self-service: one get, no join | No secondary filters (“all students with balance > 0”) without a scan |
| **Graph** | Academic dependence | Modules as nodes, `PREREQUISITE` as directed edges | Eligibility is a path question (`CSC101 → … → MIT8103`) | Marks and money are not graphs |
| Column-family | Discussed only | Wide rows of (student, session) → assessment columns | Would help scan-heavy result analytics | Overkill for this OLTP size; would weaken row-level grade transactions |

Document store is the **implemented primary alternative** because the dominant extra-relational access pattern is student-centric (transcript, advisee file, portal home). MongoDB / CouchDB are the module’s examples; this portfolio implements the same shape as JSON documents plus a document-style query (no SQL at read time).

## Document schema (Ada Okonkwo)

```json
{
  "_id": "RU/CSC/2024/001",
  "type": "student",
  "name": { "first": "Ada", "last": "Okonkwo" },
  "programme": { "code": "BSC-CSC", "department": "CSC" },
  "enrolments": [
    {
      "module_code": "CSC101",
      "final_mark": 82.0,
      "letter_grade": "A",
      "assessments": [{ "type": "CA", "score": 26 }]
    }
  ]
}
```

Live export: `evidence/document_ada.json`.

This is **controlled denormalisation**. Student name and programme sit inside the document so a transcript read does not join. The cost is the same update anomaly the normalisation write-up removed: renaming a programme requires rewriting every student document. That is acceptable for a read replica / portal cache, not for the registrar’s write path.

## BASE / DBASE vs ACID (module terms)

Document and key-value copies are **Basically Available** and **Eventually Consistent** with the relational store:

- Export is a batch (ETL-like) from SQLite → JSON.
- A mark committed in Portfolio 3 appears in the document only after the next export.
- Soft state: two readers can see different generations of `document_ada.json` during an export.

That is the correct trade-off for a student portal. It is the wrong trade-off for entering an exam score.

## Graph operations

`graph.json` stores the prerequisite DAG. The script runs a BFS from `CSC101` to `MIT8103`. The path is an academic rule (“Advanced Database Systems requires Database Systems, which requires Introduction to Computing”), not a mark.

Column-family (Cassandra/HBase) would store `(matric, session)` as the row key and one column per assessment. Useful for a results warehouse. It is not implemented as a second full database because the document aggregate already covers the student-shaped read, and the relational tables already cover the write.

## Suitability verdict

| Workload | Preferred model |
| --- | --- |
| Grade entry, fee posting, registration | Relational ACID (Portfolios 1–3) |
| Student portal transcript / profile | Document |
| “What is my timetable / balance?” | Key-value |
| “Can this student take MIT8103?” | Graph |
| University-wide fail-rate cubes | Relational now; column-family or warehouse later |

Hybrid is the honest design: one case study, several models, each used for the access pattern it matches.
