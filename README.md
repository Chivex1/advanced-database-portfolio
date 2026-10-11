# Advanced Database Portfolio

MIT 8103: Advanced Database Systems — individual practical portfolio (40 marks).

## Selected case study

### University Student Information and Results Management System (USIRMS)

**Organisation:** Riverside University (MAIN campus, Lagos; NORTH campus, Kaduna).

- **Nature of the system:** Operational student-information and results platform (OLTP) with reporting queries.
- **Users:** students, lecturers, academic advisors, heads of department, registrar staff, administrators.
- **Major data:** students, departments, programmes, modules, lecturers, enrolments, assessments, grades, timetables, attendance, fees, transcripts.
- **Key operations:** course registration, grade entry, GPA/CGPA, transcript issue, timetable tracking, record updates, reporting.

This organisation is used in every portfolio folder.

## Status

All six assessed pieces are implemented with runnable scripts and captured evidence. Self-grade: **40/40** (see [SCORECARD.md](SCORECARD.md)).

Replace the GitHub URL and student details in [final-documentation/portfolio-summary.md](final-documentation/portfolio-summary.md) before LMS submission.

## Recreate on a clean machine

Python 3.10+ and a local MySQL/MariaDB server are required (developed on Python 3.12 / MariaDB). Install `PyMySQL`, then open `usirms` in DBeaver (`127.0.0.1:3306`). See `portfolio-1-database-design/dbeaver-connection.md`.

```text
python portfolio-1-database-design/scripts/build_database.py --scale full
python portfolio-2-query-optimisation/scripts/run_optimisation.py
python portfolio-3-transactions-concurrency/scripts/run_transactions.py
python portfolio-4-nosql/scripts/export_and_query.py
python portfolio-5-distributed-cloud/scripts/run_distributed.py
```

Portfolio 2 rebuilds the `usirms` schema at full scale. Portfolios 3–5 reuse that schema.

## Portfolio components

| Folder | Activity | Marks | What to open first |
| --- | --- | ---: | --- |
| [portfolio-1-database-design/](portfolio-1-database-design/) | Database design and modelling | 7 | `README.md`, `02-erd.md`, `evidence/constraint_violations.txt` |
| [portfolio-2-query-optimisation/](portfolio-2-query-optimisation/) | Query processing and optimisation | 7 | `README.md`, `evidence/timings.txt` |
| [portfolio-3-transactions-concurrency/](portfolio-3-transactions-concurrency/) | Transactions and concurrency | 7 | `evidence/transaction_output.txt` |
| [portfolio-4-nosql/](portfolio-4-nosql/) | NoSQL and advanced data models | 7 | `01-model-and-suitability.md`, `evidence/nosql_queries.txt` |
| [portfolio-5-distributed-cloud/](portfolio-5-distributed-cloud/) | Distributed and cloud databases | 6 | `01-architecture.md`, `evidence/distributed_run.txt` |
| [final-documentation/](final-documentation/) | LMS summary and reflection | 6 | `portfolio-summary.md` |

## Repository structure

```text
advanced-database-portfolio/
├── README.md
├── SCORECARD.md
├── shared/mysql_db.py                    MySQL connection helper
├── requirements.txt                      PyMySQL
├── portfolio-1-database-design/
├── portfolio-2-query-optimisation/
├── portfolio-3-transactions-concurrency/
├── portfolio-4-nosql/
├── portfolio-5-distributed-cloud/
└── final-documentation/
```

## Assessment alignment

The work follows the CA requirement for practical evidence plus explanation: schemas and scripts, execution plans, transaction output, NoSQL artefacts, fragmentation/replication results, and an individual reflection with an AI-use declaration. Screenshots or copied code are not the primary evidence.
