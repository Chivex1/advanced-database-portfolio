# Keys, constraints, and integrity rules

Integrity is a characteristic of a good database in the module (accuracy, consistency, controlled redundancy). USIRMS enforces it in the schema, not only in application code.

## Primary keys

Every relation has a single-column integer surrogate PK except:

| Relation | Primary key | Why |
| --- | --- | --- |
| `programme_module` | `(programme_id, module_id)` | A module appears at most once in a programme |
| `module_prerequisite` | `(module_id, prerequisite_module_id)` | Pair is the fact |
| `department_head` | `department_id` | At most one current head |

Surrogate keys are used on transactional tables (`enrolment`, `grade`, `fee_payment`) so history rows can be referenced without a wide composite key.

## Candidate / unique keys (business identifiers)

| Relation | Unique key | Business meaning |
| --- | --- | --- |
| `campus` | `campus_code`, `campus_name` | Site codes |
| `department` | `department_code`, `department_name` | Faculty codes |
| `staff` | `staff_number`, `email` | HR identity |
| `programme` | `programme_code` | Catalogue code |
| `module` | `module_code` | Catalogue code |
| `student` | `matric_no`, `email` | Registry identity |
| `academic_session` | `session_label` | e.g. 2025/2026 |
| `semester` | `(session_id, semester_no)` | First/second only |
| `module_offering` | `(module_id, semester_id)` | One offering per module per semester |
| `enrolment` | `(student_id, offering_id)` | No double registration |
| `grade` | `(enrolment_id, assessment_id)` | One score per assessment |
| `attendance` | `(slot_id, student_id, attendance_date)` | One mark per meeting |
| `fee_invoice` | `(student_id, session_id)` | One bill per session |
| `fee_payment` | `reference_no` | Bank/receipt identity |
| `department_head` | `staff_id` | One department per HoD |

## Foreign keys (referential integrity)

All FKs are declared in `sql/schema.sql` and enabled with `PRAGMA foreign_keys = ON`.

Notable rules:

- A student must belong to an existing programme and campus.
- An enrolment must point to an existing student and offering.
- A grade must point to an existing enrolment and assessment.
- A payment must point to an existing invoice.
- An issued transcript must name the registrar staff member who issued it.

InnoDB default FK action is `RESTRICT` / `NO ACTION`, which is correct for official records: you cannot delete a student who has enrolments.

## Domain / CHECK constraints

| Rule | Constraint |
| --- | --- |
| Staff roles | `role IN ('Lecturer','Advisor','HoD','Registrar','Admin')` |
| Registrar/Admin have no department; academic staff must have one | table-level CHECK on `staff` |
| Gender / student status / invoice status | enumerated CHECK lists |
| Credit units 1–6 | `credit_units BETWEEN 1 AND 6` |
| Assessment weight (0, 100] | `weight_percent > 0 AND weight_percent <= 100` |
| Score ≥ 0; final mark 0–100 | CHECK on `grade.score` and `enrolment.final_mark` |
| Grade point 0–5 | CHECK on `enrolment.grade_point` |
| Dates ordered | `end_date > start_date`, `end_time > start_time` |
| No self-prerequisite | `module_id <> prerequisite_module_id` |
| Issued transcript complete | `status = 'Issued'` requires `issued_on` and `issued_by` |

## Entity integrity

No primary-key column is nullable. Business identifiers (`matric_no`, `email`, `module_code`) are `NOT NULL UNIQUE`.

## Referential actions and deletion policy

USIRMS prefers **restrict** over cascade for academic facts. Cascading a student delete would silently remove grades and payments. Administrative withdrawal is a *status change* (`Withdrawn`), not a physical delete.

## User-defined / business integrity (enforced in scripts)

Schema CHECKs cannot easily express cross-row rules. These are tested in `sql/integrity_tests.sql` and/or application transactions:

| Rule | Where enforced |
| --- | --- |
| Assessment weights for an offering should sum to 100 | Integrity test + results-finalisation transaction |
| Grade score must not exceed `assessment.max_score` | Integrity test + Portfolio 3 transaction |
| Enrolment only if student status is `Active` | Registration transaction (Portfolio 3) |
| Cannot finalise a result until all assessments have published grades | Results-finalisation transaction |
| Invoice status matches payment total | `v_invoice_balance` plus update in payment transaction |
| Lecturer on an offering should be an academic staff member | Seed/test convention; role checked in transaction scripts |

## Integrity demonstrated (not only declared)

`scripts/build_database.py` loads the schema, seeds legal rows, then runs `sql/integrity_tests.sql`. That script *expects* selected illegal statements to fail. Evidence is written to `evidence/`.

Examples of rejected operations:

1. Duplicate `matric_no`
2. Grade for a non-existent enrolment (FK)
3. Score below 0 (CHECK)
4. Two enrolments of the same student on the same offering (UNIQUE)
5. Payment with a duplicate `reference_no`
6. Self-prerequisite
7. Issued transcript without `issued_by`

## Security note (module CIA triad)

This portfolio enforces **integrity** in the schema. Confidentiality (role-based access) and availability (replication) are addressed in Portfolios 3 and 5. The schema still records `entered_by` / `issued_by` so an audit trail exists for privilege review.
