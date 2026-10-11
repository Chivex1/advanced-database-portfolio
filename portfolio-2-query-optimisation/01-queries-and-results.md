# Queries and results

All queries use the locked USIRMS case study. They are registrar, HoD, advisor, bursary, or student operations — not toy `SELECT *` examples.

SQL source: [`sql/queries.sql`](sql/queries.sql)  
Captured result sets: [`evidence/results/`](evidence/results/)

## Query inventory

| ID | User | Operation | Why it is a join/aggregation problem |
| --- | --- | --- | --- |
| Q1 | Student / Registrar | Official transcript | Six-way join through `v_transcript_line` |
| Q2 | Advisor / HoD | CSC CGPA ranking | Filter + aggregation view + sort |
| Q3 | Registrar | Module failure rates | `GROUP BY` / `HAVING` on completed enrolments |
| Q4 | Bursary | Outstanding fees | Derived balance view, current session |
| Q5 | HoD | Lecturer load, open semester | Staff × offering × enrolment |
| Q6 | Advisor | Attendance below 75% | Grouped attendance with a threshold |
| Q7 | Registrar | Enrolment census | Multi-dimension count |
| Q8a/b | Registry quality | CSC students with an F | Nested subquery vs rewritten join |

## Relational algebra (selected queries)

The module represents SQL internally as relational algebra / a query tree before physical planning.

**Q1 (transcript)**

```text
π session, semester, code, title, cu, mark, letter, gp (
  σ matric_no = 'RU/CSC/2024/001' (
      student ⋈ enrolment ⋈ module_offering ⋈ module ⋈ semester ⋈ academic_session
  )
)
```

Heuristic from the module: apply **selection** (`matric_no`) and **projection** as early as possible so intermediate results stay small. The view expands to those joins; the optimiser should push the matric predicate to `student` (unique index already exists).

**Q8 rewrite (module worked example, applied to USIRMS)**

The notes rewrite

```sql
SELECT name FROM Employees
WHERE dept_id IN (SELECT id FROM Departments WHERE location = 'NY');
```

as a join. Q8a is the nested form (“active students who failed a CSC module”). Q8b is the join form. Both must return the same 20-row sample; plans and timings are compared in `02-execution-plans-and-indexing.md`.

## Result evidence (what to inspect)

After `scripts/run_optimisation.py`:

- `evidence/results/Q1_transcript.txt` — Ada Okonkwo’s lines, including in-progress CSC102
- `evidence/results/Q2_csc_cgpa_rank.txt` — top 15 active CSC CGPAs
- `evidence/results/Q3_failure_rates.txt` — fail % by module
- `evidence/results/Q4_outstanding_fees.txt` — unpaid / partial invoices
- `evidence/results/Q5_lecturer_load.txt` — open-semester teaching load
- `evidence/results/Q6_low_attendance.txt` — advisees below 75%
- `evidence/results/Q7_enrolment_census.txt` — headcount by programme/semester
- `evidence/results/Q8a_nested_subquery.txt` and `Q8b_rewritten_join.txt` — same student identifiers

If Q8a and Q8b identifiers differ, the rewrite is wrong. The runner keeps both result files so that check is visible.
