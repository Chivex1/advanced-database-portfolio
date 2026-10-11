# Performance analysis

This note interprets the **measured** plans and timings. Numbers are copied from `evidence/timings.txt` after a live run on this machine (mean of 15 runs, `time.perf_counter()`).

## Workload type

USIRMS is **OLTP** with a reporting overlay (module: OLTP vs OLAP). Registration and grade entry are short transactions (Portfolio 3). Q1–Q8 are the OLAP-style queries that share the same schema. They are the queries that justify secondary indexes; they are not an excuse to denormalise the system of record.

## Cost factors from the module, applied here

| Cost factor | Observation on USIRMS |
| --- | --- |
| Disk I/O | Dominant in theory; on this SQLite file the DB is cached, so plan shape matters more than milliseconds |
| Size of intermediate results | Q3/Q7 aggregate all completed enrolments; early `status = 'Completed'` reduces the bag |
| Indexes | FK indexes change `SCAN enrolment` into `SEARCH` |
| Join order | Q8b lets the planner start from `department_code = 'CSC'` (1 row) instead of scanning every student |
| Query complexity | Q8a nested `IN` is harder to flatten by hand; the rewrite is explicit |
| Statistics | `ANALYZE` after index creation updates sqlite_stat1 |
| Network cost | Single-node SQLite: zero. Reappears in Portfolio 5 when fragments sit on different campuses |

## Query rewrite (Q8)

Same business question: *active students who have a failed completed enrolment on a Computer Science module*.

- Q8a: two nested `IN` subqueries (module’s original form).
- Q8b: equi-joins with the CSC predicate applied to `department` (module’s rewritten form).

Result files must list the same matric numbers. If they do, the rewrite is semantically safe. The plan files show whether SQLite still correlated the subquery or built a join.

## Indexing outcome

Secondary indexes are a **physical-design** change (module stage 4). They do not change 3NF. They change access paths.

Measured result (`evidence/timings.txt`):

| Query | Rows | Before (ms) | After (ms) | What changed |
| --- | ---: | ---: | ---: | --- |
| Q1 transcript | 4 | 0.075 | 0.072 | Already a unique `matric_no` lookup |
| Q2 CGPA via view | 15 | 8.139 | 8.283 | View still scans every enrolment (see plans) |
| Q2b pushed selection | 15 | 9.385 | 13.034 | After indexes the plan is all `SEARCH`, starting at `department_code = 'CSC'` |
| Q3 failure rates | 18 | 8.311 | 7.529 | Slightly faster |
| Q4 outstanding fees | 20 | 7.269 | 4.459 | Invoice/session index used |
| Q5 lecturer load | 8 | 8.820 | 0.525 | Persistent covering indexes replace per-query automatic indexes |
| Q6 low attendance | 58 | 5.109 | 5.733 | No material win at this cardinality |
| Q7 census | 15 | 36.454 | 22.235 | FK indexes on enrolment/offering |
| Q8a nested IN | 6 | 1.844 | 0.190 | Letter-grade index |
| Q8b join rewrite | 6 | 4.894 | 0.178 | Same 6 matric numbers as Q8a; all `SEARCH` |

Q5 is the clearest physical win: before indexes SQLite built **automatic covering indexes** for that statement (see `plans_before/Q5_lecturer_load.txt`); after, it uses `idx_offering_semester_lecturer` and `idx_enrolment_offering_status` and the mean time falls from 8.820 ms to 0.525 ms.

Q2 vs Q2b is the selection-pushdown lesson. Q2b’s **after** plan starts from one department row and never scans `enrolment`. On a RAM-resident file that rewrite is not faster than scanning a compact B-tree — the wall-clock is slightly worse — but the plan is the one the module’s heuristics describe. At a larger university the scan of every completed enrolment in `v_student_cgpa` would dominate.

Timings vary between runs (OS cache, other processes). The first execution of this script showed a larger Q2 regression when the planner chose `idx_enrolment_student_status` to scan the whole enrolment table. That is left in the narrative as a warning: **an extra index can be a worse access path for a query that must read every row**. Plan inspection matters more than a single millisecond figure.

## What was not claimed

- No invented milliseconds.
- No PostgreSQL `EXPLAIN ANALYZE` cost figures (this DBMS is SQLite).
- No assertion that every query improved; a small regression on an already-indexed unique lookup would be normal.

## How a DBA would continue

1. Keep `ANALYZE` in the build after bulk loads.
2. Add covering columns only if a plan still visits the table for a few output fields.
3. If reporting grows (full-university degree audit), copy into a warehouse/mart (module Session 3) rather than denormalising OLTP tables.
