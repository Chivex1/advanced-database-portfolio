# Execution plans and indexing

## How MySQL / MariaDB plans a query (module mapping)

| Module concept | What this portfolio shows |
| --- | --- |
| Parsing → translation → optimisation → execution | SQL is compiled; `EXPLAIN` shows the chosen physical plan |
| Query tree / join order | One row per joined table (or derived table / subquery) in join order |
| Rule-based heuristics | Selection on unique `matric_no`; avoid cartesian products |
| Cost-based optimisation | `ANALYZE TABLE` refreshes index statistics the optimiser uses for row estimates |
| Access path | `type=ALL` (full table/index walk) vs `const` / `eq_ref` / `ref` (B-tree lookup) |
| File organisation | InnoDB clusters each table on its PRIMARY KEY; secondary indexes are separate B-trees that point back to the PK |

MySQL’s plain `EXPLAIN` does **not** print a PostgreSQL-style total cost. The comparable evidence is the **plan shape** (`type`, `key`, `rows`, `Extra`) plus **measured wall time**. Those times are captured with `time.perf_counter()`; they are not invented.

## Why secondary indexes are needed

PRIMARY KEY, UNIQUE, and FOREIGN KEY columns are already indexed by InnoDB (`student.matric_no`, `enrolment.offering_id` → `fk_enrol_offering`, …). Reporting queries also filter on `student.status`, `enrolment.letter_grade`, `enrolment.status`, `fee_invoice.status`, and join offerings by `(semester_id, lecturer_staff_id)`. Those predicates are not covered well by the automatic FK indexes alone, so composite secondary indexes are added.

Index DDL: [`sql/indexes.sql`](sql/indexes.sql)

## Before / after method

1. Rebuild USIRMS at `--scale full` (1,200 students).
2. Drop any leftover secondary indexes named `idx_%`.
3. `EXPLAIN` + time each query (15 runs, one warmup).
4. Create the indexes and `ANALYZE TABLE`.
5. Repeat plans and timings.

Artefacts:

- `evidence/plans_before/*.txt`
- `evidence/plans_after/*.txt`
- `evidence/indexes_created.txt`
- `evidence/timings.txt`

## What a good change looks like

Typical before line (full walk of a large fact table):

```text
id=1 select_type=SIMPLE table=e type=ALL key=None rows=3650 Extra=Using where; Using temporary; Using filesort
```

Typical after line (secondary index used for a selective predicate):

```text
id=1 select_type=SIMPLE table=e type=ref key=idx_enrolment_letter rows=23 Extra=Using index condition
```

Q1 should already use `type=const key=uk_matric_no` on `student` even before extra indexes — that is the unique business key doing its job. Enrolment then uses the unique `(student_id, offering_id)` index (`uk_student_offering`), and the dimension tables use `eq_ref` on PRIMARY KEY.

Q8a often keeps a subquery / MATERIALIZED shape. Q8b is a single join tree and is the form the module recommends. The important claim is **plan/shape and rewrite**, not that every query becomes faster on a database that still fits in the buffer pool. If a timing delta is near zero or worse, that is reported honestly: an extra index can be ignored, or can steer the optimiser into a worse join order.

## Covering / composite choices

| Index | Supports |
| --- | --- |
| `idx_student_status_programme` | Q2, Q2b status + programme access |
| `idx_enrolment_student_status` | Q2b completed-enrolment filter by student |
| `idx_enrolment_offering_status` | Q5 join from offering → enrolment with status |
| `idx_enrolment_letter` | Q8 letter-grade filter (`F`) |
| `idx_attendance_student_status` | Q6 |
| `idx_invoice_session_status` | Q4 session/status filter on invoices |
| `idx_offering_semester_lecturer` | Q5 open-semester load |

These are secondary (non-clustered) B-tree indexes. InnoDB’s table is clustered on the integer PK, which is efficient for PK lookups (`eq_ref`) but not for selective filters on `letter_grade` or `(status, programme_id)` without a matching secondary index.
