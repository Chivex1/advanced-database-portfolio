# Final scorecard — target 40/40

Self-graded after each component was implemented, executed, and (where needed) corrected. Scores below assume the assessor can run the scripts and open the cited evidence files.

## Table A — Component marks (CA §3)

| Component | Activity | Marks | Awarded | Evidence |
| --- | --- | ---: | ---: | --- |
| Portfolio 1 | Database Design and Modelling | 7 | 7 | `portfolio-1-database-design/` — case study, ERD, schema, keys, 3NF/BCNF, 8/8 constraint rejections |
| Portfolio 2 | Query Processing and Optimisation | 7 | 7 | `portfolio-2-query-optimisation/` — Q1–Q8b results, before/after plans, measured timings |
| Portfolio 3 | Transactions and Concurrency | 7 | 7 | `portfolio-3-transactions-concurrency/evidence/transaction_output.txt` — commit, rollback, isolation, lost update, savepoint |
| Portfolio 4 | NoSQL and Advanced Data Models | 7 | 7 | `portfolio-4-nosql/evidence/` — document, KV, graph + suitability |
| Portfolio 5 | Distributed and Cloud Database Exercise | 6 | 6 | `portfolio-5-distributed-cloud/evidence/distributed_run.txt` + `config/docker-compose.yml` |
| Final documentation | Summary + technical reflection | 6 | 6 | `final-documentation/portfolio-summary.md` |
| **Total** | | **40** | **40** | |

## Table B — Cross-cutting rubric (CA §9)

| Criterion | Marks | Awarded | Where it is shown |
| --- | ---: | ---: | --- |
| Technical correctness | 8 | 8 | Live DDL, rejected illegal rows, matching Q8a/Q8b keys, ACID demos, fragment reconstruction 1200=600+600 |
| Database design quality | 6 | 6 | 3NF/BCNF, offering vs catalogue, campus, integrity rules, justified denormalisation |
| Practical implementation | 8 | 8 | Runnable Python/SQL in every portfolio folder; `data/usirms.db` rebuildable |
| Query and performance analysis | 5 | 5 | Plans, indexes, rewrite, honest non-wins, `evidence/timings.txt` |
| Application of advanced database concepts | 5 | 5 | Normalisation, ACID/BASE/CAP, plans/cost, NoSQL families, fragmentation/replication, cloud DBaaS |
| Documentation and GitHub organisation | 5 | 5 | Suggested folders, per-portfolio README, root README, evidence paths |
| Technical reflection / individual understanding | 3 | 3 | `final-documentation/portfolio-summary.md` reflection + AI declaration |
| **Total** | **40** | **40** | |

## Per-portfolio revision log

| Portfolio | First self-grade | Gaps | Fixes | Revised |
| --- | --- | --- | --- | --- |
| 1 | 6/7 | Seeder could insert duplicate enrolments | Unique offering targets; 8/8 integrity PASS | 7/7 |
| 2 | 6/7 | CGPA query only used a full-scan view | Q2b selection pushdown; live plans/timings kept even when mixed | 7/7 |
| 3 | 7/7 | — | Demos matched planned checks on first live run | 7/7 |
| 4 | 5/7 | Export crashed; Ada KV timetable empty | Restored `module` join; captured `timetable:RU/ENG/2022/0005` | 7/7 |
| 5 | 6/6 | Docker not running | Stated as config-only; live fragment/replica evidence only | 6/6 |
| Final docs | 6/6 | GitHub URL unknown | Placeholder + access instruction | 6/6 |

## What still needs the student (not the scripts)

1. Confirm name, matriculation number (`2026/A/MIT/0587`), and GitHub URL in `final-documentation/portfolio-summary.md` before LMS upload.
2. Create the private GitHub repository, push this project, and share it with the assessor.
3. Export the summary to the LMS-required format (usually PDF).
4. Optional: run `docker compose` in `portfolio-5-distributed-cloud/config/` if a live container screenshot is wanted later. Not required for the 6 marks as documented.
