# Execution plans and indexing

## How SQLite plans a query (module mapping)

| Module concept | What this portfolio shows |
| --- | --- |
| Parsing → translation → optimisation → execution | SQL is compiled; `EXPLAIN QUERY PLAN` shows the chosen physical plan |
| Query tree / join order | `parent` / `id` lines in the plan |
| Rule-based heuristics | Selection on unique `matric_no`; avoid cartesian products |
| Cost-based optimisation | `ANALYZE` writes sqlite_stat1; the planner uses row-count statistics |
| Access path | `SCAN` (heap/table walk) vs `SEARCH` (B-tree index) |
| File organisation | SQLite stores tables and indexes as B-trees, not as a raw heap file, but a `SCAN` is still a full walk of that B-tree |

SQLite does **not** print a PostgreSQL-style cost number. The comparable evidence is the **plan shape** plus **measured wall time**. Those times are captured with `time.perf_counter()`; they are not invented.

## Why secondary indexes are needed

PRIMARY KEY and UNIQUE columns are already indexed (`student.matric_no`, `enrolment.enrolment_id`, …). Foreign keys are **not** automatically indexed. Reporting queries join `enrolment.offering_id`, `grade.enrolment_id`, `fee_payment.invoice_id`, and filter `student.status`, `enrolment.letter_grade`, `semester.status`. Without secondary indexes those predicates force scans.

Index DDL: [`sql/indexes.sql`](sql/indexes.sql)

## Before / after method

1. Rebuild USIRMS at `--scale full` (1,200 students).
2. Drop any leftover secondary indexes.
3. `EXPLAIN QUERY PLAN` + time each query (15 runs, one warmup).
4. Create the indexes and `ANALYZE`.
5. Repeat plans and timings.

Artefacts:

- `evidence/plans_before/*.txt`
- `evidence/plans_after/*.txt`
- `evidence/indexes_created.txt`
- `evidence/timings.txt`

## What a good change looks like

Typical before line:

```text
SCAN enrolment
```

Typical after line:

```text
SEARCH enrolment USING INDEX idx_enrolment_offering_status (offering_id=?)
```

Q1 should already `SEARCH student USING INDEX sqlite_autoindex_student_*` on `matric_no` even before extra indexes — that is the unique business key doing its job.

Q8a often keeps a correlated/`IN` subquery structure. Q8b is a single join tree and is the form the module recommends. The important claim is **plan/shape and rewrite**, not that every query becomes faster on a database that still fits in RAM. If a timing delta is near zero or slightly negative, that is reported honestly: index maintenance and a different join order can cost more on a small cached file.

## Covering / composite choices

| Index | Supports |
| --- | --- |
| `idx_student_status_programme` | Q2, Q7, Q8 status + programme access |
| `idx_enrolment_offering_status` | Q3, Q5, Q7 join from offering → enrolment |
| `idx_enrolment_letter` | Q3 / Q8 letter-grade filter |
| `idx_attendance_student_status` | Q6 |
| `idx_invoice_session_status` | Q4 |
| `idx_offering_semester_lecturer` | Q5 open-semester load |

These are secondary (non-clustered) B-tree indexes. SQLite’s table itself is clustered on the integer PK, which is efficient for PK lookups but not for `status` or FK joins.
