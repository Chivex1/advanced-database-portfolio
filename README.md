# Advanced Database Portfolio

MIT 8103 — Advanced Database Systems (individual practical portfolio, 40 marks).

## Selected case study

**University Student Information and Results Management System (USIRMS)** — Riverside University (MAIN / Lagos, NORTH / Kaduna). OLTP student records, grades, fees, transcripts, and reporting. Same organisation in every portfolio folder (see `portfolio-1-database-design/00-case-study.md`).

## Recreate on a clean machine

Requirements: Python 3.10+, local MySQL/MariaDB, `python -m pip install -r requirements.txt`. Create schema `usirms` per `portfolio-1-database-design/dbeaver-connection.md` (default `127.0.0.1:3306`, user `root`, empty password unless `.env` overrides).

```text
python portfolio-1-database-design/scripts/build_database.py --scale full
python portfolio-2-query-optimisation/scripts/run_optimisation.py
python portfolio-3-transactions-concurrency/scripts/run_transactions.py
python portfolio-4-nosql/scripts/export_and_query.py
python portfolio-5-distributed-cloud/scripts/run_distributed.py
```

Portfolio 2 rebuilds `usirms` at full scale (1,200 students). Portfolios 3–5 expect that database to exist.

## Where to verify (assessor quick path)

| Folder | CA topic | Start here |
| --- | --- | --- |
| [portfolio-1-database-design/](portfolio-1-database-design/) | Design & modelling | `README.md`, `evidence/constraint_violations.txt` |
| [portfolio-2-query-optimisation/](portfolio-2-query-optimisation/) | Queries & plans | `evidence/timings.txt`, `evidence/plans_after/` |
| [portfolio-3-transactions-concurrency/](portfolio-3-transactions-concurrency/) | Transactions | `evidence/transaction_output.txt` |
| [portfolio-4-nosql/](portfolio-4-nosql/) | NoSQL models | `evidence/nosql_queries.txt`, `01-model-and-suitability.md` |
| [portfolio-5-distributed-cloud/](portfolio-5-distributed-cloud/) | Distributed / cloud | `evidence/distributed_run.txt`, `01-architecture.md` |
| [final-documentation/](final-documentation/) | LMS summary | [portfolio-summary.md](final-documentation/portfolio-summary.md) |

Component-level pointers: [SCORECARD.md](SCORECARD.md).

## Repository layout

```text
advanced-database-portfolio/
├── README.md
├── SCORECARD.md
├── requirements.txt
├── shared/mysql_db.py
├── portfolio-1-database-design/ … portfolio-5-distributed-cloud/
└── final-documentation/
```

Course brief copies (`mit-8103-*.md`, `plan.md`, `.cursor/`) stay local and are listed in `.gitignore` — not part of the GitHub submission.
