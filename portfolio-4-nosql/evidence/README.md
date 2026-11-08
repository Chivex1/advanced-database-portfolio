# Portfolio 4 — evidence checklist (NoSQL, not SQL)

## What the CA wants

| Item | Evidence |
| --- | --- |
| Document model | Student JSON with nested enrolments |
| Key-value | `fees:{matric}`, `timetable:{matric}` lookups |
| Graph | Prerequisite path e.g. CSC101 → MIT8103 |
| Suitability | `../01-model-and-suitability.md` |

Reads are **from JSON files**, not from SQL at query time (`nosql_queries.txt` states this).

## Regenerate outputs

```text
python portfolio-4-nosql/scripts/export_and_query.py
```

Check: `document_ada.json`, `nosql_queries.txt`, `../data/kv_store.json`, `../data/graph.json`.

---

## Using DBeaver (files only — no SQL for this portfolio)

DBeaver is a **viewer** here, not where you “run NoSQL queries” for this project.

1. **File → Open file** (or drag into DBeaver) and open:
   - `../data/documents/RU_CSC_2024_001.json` — document model
   - `evidence/document_ada.json` — copy placed in evidence
   - `../data/graph.json` — nodes + edges (small file)
2. **Key-value store** (`../data/kv_store.json` is large):
   - In DBeaver: open the file → **Ctrl+F** search `fees:RU/CSC/2024/001` and `timetable:RU/CSC/2022/0009` (or the sample key printed in `nosql_queries.txt`).
   - Screenshot the matching JSON fragment.
3. **`nosql_queries.txt`** — open in DBeaver or Cursor; screenshot the **document lookup**, **KV**, and **graph path** sections (proves three models in one run).

You can also use **Cursor** or **Notepad** for the same JSON/txt screenshots; the assessor cares about the **artefacts**, not which app framed them.

---

## Suggested screenshot names (`evidence/`)

| File | What to show |
| --- | --- |
| `01_export_terminal.png` | Terminal after `export_and_query.py` (12 docs, KV count, graph edges) |
| `02_document_ada.png` | `document_ada.json` — `_id`, nested `enrolments` |
| `03_nosql_queries.png` | `nosql_queries.txt` — CGPA 4.64 + graph path |
| `04_kv_fees.png` | KV snippet: `fees:RU/CSC/2024/001` |
| `05_kv_timetable.png` | KV snippet: non-empty `timetable:…` from `nosql_queries.txt` |
| `06_graph.png` | `graph.json` or path array in `nosql_queries.txt` |

---

## Write-up

`../01-model-and-suitability.md` — document primary; column-family discussed; ACID write path vs BASE read replicas.
