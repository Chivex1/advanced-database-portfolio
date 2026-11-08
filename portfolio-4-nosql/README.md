# Portfolio 4 — NoSQL and Advanced Data Models

**Case study:** USIRMS — document (primary), key-value, graph (JSON + Python reads; not SQL at query time)

## Write-ups and scripts

| Path | Content |
| --- | --- |
| [01-model-and-suitability.md](01-model-and-suitability.md) | Model choice, BASE vs ACID, column-family discussed |
| [scripts/export_and_query.py](scripts/export_and_query.py) | Export from MySQL → JSON, run lookups |
| [data/documents/](data/documents/), [data/kv_store.json](data/kv_store.json), [data/graph.json](data/graph.json) | Artefacts |

## Recreate

```text
python portfolio-4-nosql/scripts/export_and_query.py
```

## Evidence (assessor)

| File | What it shows |
| --- | --- |
| [evidence/document_ada.json](evidence/document_ada.json) | Nested student document (`RU/CSC/2024/001`) |
| [evidence/nosql_queries.txt](evidence/nosql_queries.txt) | CGPA from document, KV get, graph path `CSC101 → MIT8103` |

After Portfolio 3, Ada’s live timetable key may be empty; `nosql_queries.txt` includes a non-empty sample timetable key for KV evidence. Official marks remain on the relational write path.

Optional DBeaver: open JSON files only — see [sql/README.md](sql/README.md) (relational contrast, not P4 query evidence).
