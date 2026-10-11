# Performance analysis

This note interprets the **measured** plans and timings. Numbers are copied from `evidence/timings.txt` after a live run on this machine (mean of 15 runs, `time.perf_counter()`).

## Workload type

USIRMS is **OLTP** with a reporting overlay (module: OLTP vs OLAP). Registration and grade entry are short transactions (Portfolio 3). Q1–Q8 are the OLAP-style queries that share the same schema. They are the queries that justify secondary indexes; they are not an excuse to denormalise the system of record.

## Cost factors from the module, applied here

| Cost factor | Observation on USIRMS |
| --- | --- |
| Disk I/O | Dominant in theory; on this MariaDB instance the working set is largely cached, so plan shape matters more than raw milliseconds |
| Size of intermediate results | Q3/Q7 aggregate completed enrolments; early `status = 'Completed'` / letter-grade filters reduce the bag |
| Indexes | Secondary indexes change `type=ALL` or weak access into `type=ref` when the optimiser chooses them |
| Join order | Q8b lets the planner start from `department_code = 'CSC'` (`const`) instead of scanning every student first |
| Query complexity | Q8a nested `IN` is harder to flatten by hand; the rewrite is explicit |
| Statistics | `ANALYZE TABLE` after index creation refreshes cardinality estimates |
| Network cost | Single-node MariaDB on localhost: negligible. Reappears in Portfolio 5 when fragments sit on different campuses |

## Query rewrite (Q8)

Same business question: *active students who have a failed completed enrolment on a Computer Science module*.

- Q8a: two nested `IN` subqueries (module’s original form).
- Q8b: equi-joins with the CSC predicate applied to `department` (module’s rewritten form).

Result files must list the same matric numbers. If they do, the rewrite is semantically safe. The plan files show whether MariaDB still materialises a subquery or builds a join that can use `idx_enrolment_letter`.

## Indexing outcome

Secondary indexes are a **physical-design** change (module stage 4). They do not change 3NF. They change access paths.

Measured result (`evidence/timings.txt`):

| Query | Rows | Before (ms) | After (ms) | What changed |
| --- | ---: | ---: | ---: | --- |
| Q1 transcript | 4 | 1.572 | 1.679 | Already `const` on `uk_matric_no`; secondary indexes unused |
| Q2 CGPA via view | 15 | 21.255 | 20.093 | After: `idx_student_status_programme` on student; derived CGPA still per student |
| Q2b pushed selection | 15 | 14.417 | 20.926 | After plan uses `idx_student_status_programme` + `idx_enrolment_student_status`; wall-clock slightly worse |
| Q3 failure rates | 18 | 25.952 | 97.873 | Still `type=ALL` on enrolment (~3650 rows); no plan win, timing regression |
| Q4 outstanding fees | 20 | 1044.839 | 1088.999 | Dominated by student scan + lateral payment join; `idx_invoice_session_status` not the bottleneck |
| Q5 lecturer load | 8 | 3.182 | 2.652 | After: `idx_offering_semester_lecturer` + `idx_enrolment_offering_status` |
| Q6 low attendance | 58 | 12.197 | 26.032 | No material win at this cardinality |
| Q7 census | 15 | 25.423 | 26.491 | Already `ref`/`eq_ref` on FK/unique keys before extras |
| Q8a nested IN | 6 | 5.097 | 1.397 | After: starts from `idx_enrolment_letter` (`type=ref`) |
| Q8b join rewrite | 6 | 14.442 | 1.472 | Same 6 matric numbers as Q8a; after uses `idx_enrolment_letter` |

Q8 is the clearest physical win: before indexes Q8a materialises a subquery over modules/offerings/enrolments; after, both Q8a and Q8b drive from `idx_enrolment_letter` and mean times fall to about 1.4 ms.

Q5 is a smaller but clean plan change: after indexes, offerings use `idx_offering_semester_lecturer` and enrolments use `idx_enrolment_offering_status` (covering `Using index` on both).

Q2 vs Q2b is the selection-pushdown lesson. Both start from one department row (`uk_department_code`, `const`). Q2b’s **after** plan also uses the new student/enrolment status indexes. On this cached workload that rewrite is not faster than the view path — the wall-clock is slightly worse — but the plan is the one the module’s heuristics describe. At a larger university the scan of every completed enrolment inside `v_student_cgpa` would dominate.

Q3 shows the honesty check: `idx_enrolment_letter` exists, yet `EXPLAIN` still chooses `type=ALL` on enrolment because the query aggregates almost the whole completed-enrolment set. Extra indexes can also add optimiser choice overhead; the measured regression is left in the table rather than hidden.

Timings vary between runs (buffer pool, other processes). Plan inspection matters more than a single millisecond figure: **an extra index can be ignored, or can be a worse access path for a query that must read most rows**.

## What was not claimed

- No invented milliseconds.
- No PostgreSQL `EXPLAIN ANALYZE` cost figures (this DBMS is MySQL / MariaDB; evidence is `EXPLAIN` + wall time).
- No assertion that every query improved; regressions on Q3/Q4/Q6 are reported as measured.

## How a DBA would continue

1. Keep `ANALYZE TABLE` in the build after bulk loads.
2. Add covering columns only if a plan still visits the clustered table for a few output fields (`Using index` in `Extra` is the covering signal).
3. For Q4-style payment rollups, consider an index on `fee_payment(invoice_id)` usage in the derived join, or a reporting summary table — not denormalising the OLTP invoice row.
4. If reporting grows (full-university degree audit), copy into a warehouse/mart (module Session 3) rather than denormalising OLTP tables.
