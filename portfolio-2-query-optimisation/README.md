# Portfolio 2 — Query Processing and Optimisation

**Case study:** USIRMS (same schema as Portfolio 1)  
**DBMS:** MySQL / MariaDB — `EXPLAIN`, secondary indexes, `ANALYZE TABLE`

## Write-ups and scripts

| Path | Content |
| --- | --- |
| [01-queries-and-results.md](01-queries-and-results.md) | Q1–Q8b purpose |
| [02-execution-plans-and-indexing.md](02-execution-plans-and-indexing.md), [03-performance-analysis.md](03-performance-analysis.md) | Plans, indexes, honest timings |
| [sql/queries.sql](sql/queries.sql), [sql/indexes.sql](sql/indexes.sql) | Reporting SQL and indexes |
| [scripts/run_optimisation.py](scripts/run_optimisation.py) | Full rebuild + plans + timings |

## Recreate

```text
python portfolio-2-query-optimisation/scripts/run_optimisation.py
```

## Evidence (assessor)

| Path | What it shows |
| --- | --- |
| [evidence/results/](evidence/results/) | Query result sets (Q8a and Q8b must list the same matrics) |
| [evidence/plans_before/](evidence/plans_before/) vs [evidence/plans_after/](evidence/plans_after/) | `EXPLAIN` before/after indexes |
| [evidence/indexes_created.txt](evidence/indexes_created.txt) | Indexes applied |
| [evidence/timings.txt](evidence/timings.txt) | Mean of 15 runs (`time.perf_counter`) — includes queries that did not speed up |

Optional DBeaver screenshots: `evidence/explain_Q1.PNG`, `evidence/indexes_created.PNG`.
