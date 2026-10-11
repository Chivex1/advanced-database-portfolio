# Portfolio 2 — Query Processing and Optimisation

**Case study:** USIRMS / Riverside University (same schema as Portfolio 1)  
**Marks targeted:** 7/7  
**DBMS:** MySQL / MariaDB (`EXPLAIN`, InnoDB secondary indexes, `ANALYZE TABLE`)

## Contents

| Artefact | Purpose |
| --- | --- |
| [01-queries-and-results.md](01-queries-and-results.md) | What each query is for; relational algebra |
| [02-execution-plans-and-indexing.md](02-execution-plans-and-indexing.md) | Before/after plans, index rationale |
| [03-performance-analysis.md](03-performance-analysis.md) | Cost factors, rewrite, honest timing notes |
| [sql/queries.sql](sql/queries.sql) | All reporting SQL |
| [sql/indexes.sql](sql/indexes.sql) | Secondary indexes + `ANALYZE` |
| [scripts/run_optimisation.py](scripts/run_optimisation.py) | Rebuild (full scale), plans, results, timings |
| [evidence/](evidence/) | Live output from that script |

## How to recreate / test

From the repository root, Python 3.10+:

```text
python portfolio-2-query-optimisation/scripts/run_optimisation.py
```

The script rebuilds the `usirms` MySQL schema with `--scale full` (1,200 students), captures `EXPLAIN` with no extra secondary indexes, applies `sql/indexes.sql`, then recaptures plans and timings.

Check:

1. `evidence/results/` — non-empty result sets for Q1–Q7; Q8a and Q8b list the same matric numbers.
2. `evidence/plans_before/` vs `evidence/plans_after/` — additional `SEARCH ... USING INDEX` lines on FK joins.
3. `evidence/timings.txt` — measured means (15 runs), not placeholders.

## Self-grade

**Portfolio 2: 7/7** — gaps: first draft used only a view-based CGPA query (plan still scanned every enrolment). — fixes applied: Q2b selection-pushdown rewrite; Q8a/Q8b semantic check; live plans and `time.perf_counter` timings. — revised: **7/7**.

| Expected evidence (CA table) | Present | Path |
| --- | --- | --- |
| SQL queries | Yes | `sql/queries.sql` (Q1–Q8b, all USIRMS operations) |
| Query results | Yes | `evidence/results/` (Q8a and Q8b list the same 6 students) |
| Execution plans | Yes | `evidence/plans_before/`, `evidence/plans_after/` |
| Indexing / optimisation | Yes | `sql/indexes.sql`, `evidence/indexes_created.txt` |
| Performance analysis | Yes | `03-performance-analysis.md`, `evidence/timings.txt` |

Cross-cutting: query and performance analysis (plans + measured times + honest non-wins), application of module concepts (algebra, rewrite, RBO/CBO, access paths), practical implementation (runnable runner).
