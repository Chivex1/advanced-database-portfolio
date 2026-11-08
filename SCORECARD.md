# Component checklist (MIT 8103 CA §3)

Student self-check against the continuous-assessment table. An assessor can verify each row from the paths below without running code; run the root README recreate block to reproduce outputs.

| Component | Marks | Evidence to open |
| --- | ---: | --- |
| Portfolio 1 — Database design | 7 | `portfolio-1-database-design/README.md`, `evidence/constraint_violations.txt`, `02-erd.md`, `sql/schema.sql` |
| Portfolio 2 — Query optimisation | 7 | `portfolio-2-query-optimisation/evidence/timings.txt`, `plans_before/` vs `plans_after/`, `03-performance-analysis.md` |
| Portfolio 3 — Transactions | 7 | `portfolio-3-transactions-concurrency/evidence/transaction_output.txt`, optional `evidence/*.png` |
| Portfolio 4 — NoSQL | 7 | `portfolio-4-nosql/evidence/nosql_queries.txt`, `document_ada.json`, `data/kv_store.json`, `data/graph.json` |
| Portfolio 5 — Distributed / cloud | 6 | `portfolio-5-distributed-cloud/evidence/distributed_run.txt`, `01-architecture.md`, `config/docker-compose.yml` |
| Final documentation | 6 | `final-documentation/portfolio-summary.md` |
| **Total** | **40** | |

**Stack:** Python 3.10+, MySQL/MariaDB schema `usirms` (InnoDB). Connection: `portfolio-1-database-design/dbeaver-connection.md`.

**Before LMS upload:** confirm GitHub access for the assessor and export `portfolio-summary.md` if the institution requires PDF/DOCX.
