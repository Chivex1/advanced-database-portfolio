# Portfolio 4 — NoSQL and Advanced Data Models

**Case study:** USIRMS / Riverside University  
**Marks targeted:** 7/7  
**Primary NoSQL model:** document store (student aggregates), plus key-value and graph

## Contents

| Artefact | Purpose |
| --- | --- |
| [01-model-and-suitability.md](01-model-and-suitability.md) | Choice, BASE vs ACID, comparison with the relational design |
| [scripts/export_and_query.py](scripts/export_and_query.py) | Export + document/KV/graph queries |
| [data/documents/](data/documents/) | Sample student documents |
| [data/kv_store.json](data/kv_store.json) | Timetable and fee keys |
| [data/graph.json](data/graph.json) | Prerequisite graph |
| [evidence/](evidence/) | Ada’s document and query output |

## How to recreate / test

```text
python portfolio-4-nosql/scripts/export_and_query.py
```

Requires the `usirms` MySQL schema. The script writes 12 sample student documents (including Ada), a key-value file, and the module graph, then queries them **without SQL**.

Check:

- `evidence/document_ada.json` contains nested enrolments for `RU/CSC/2024/001`
- `evidence/nosql_queries.txt` shows CGPA from the document, a KV fee/timetable get, and a `CSC101 → MIT8103` path

## Self-grade

**Portfolio 4: 7/7** — gaps: first run failed (`module` join missing); Ada’s timetable key empty after P3. — fixes applied: join restored; sample non-empty KV key (`timetable:RU/ENG/2022/0005`) captured; suitability write-up keeps relational ACID as the write path. — revised: **7/7**.

| Expected evidence (CA table) | Present | Path |
| --- | --- | --- |
| Same case study | Yes | Student / module / fee documents from USIRMS |
| Document / KV / column / graph | Yes | Document primary; KV + graph implemented; column-family discussed |
| Implementation evidence | Yes | `data/documents/`, `data/kv_store.json`, `data/graph.json` |
| Suitability vs relational | Yes | `01-model-and-suitability.md` |
