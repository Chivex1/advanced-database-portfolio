# Normalisation

Normalisation is applied as part of **logical design** (module Session 1). The objective is to remove redundancy and insertion/update/deletion anomalies while keeping the model usable for registration, grading, and reporting.

Target: **Third Normal Form, and Boyce–Codd Normal Form where determinants are candidate keys**. 4NF/5NF are not required: there are no independent multi-valued facts left inside a single relation after 3NF.

## Starting point — unnormalised registry extract

A typical legacy results sheet stores repeating groups and transitive facts in one row:

| MatricNo | StudentName | Programme | DeptPhone | ModulesAndScores | Lecturer | LecturerPhone | Session |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RU/CSC/2024/001 | Ada Okonkwo | BSc Computer Science | 0801-111-0001 | CSC101:CA 18/20; CSC101:Exam 54/80; MTH101:CA 14/20; MTH101:Exam 50/80 | Dr Bello; Dr Bello | 0802-222-0002; 0802-222-0002 | 2025/2026 |

Problems:

- **Repeating group** — several modules and several assessments in one cell.
- **Redundancy** — department phone and lecturer phone copied on every student row.
- **Update anomaly** — changing a lecturer’s phone requires many row edits.
- **Insertion anomaly** — a new module cannot be recorded until a student takes it.
- **Deletion anomaly** — deleting the last enrolled student can lose the lecturer’s phone.

## 1NF — atomic values, no repeating groups

Split repeating assessments into rows. Each cell holds one value.

| MatricNo | StudentName | Programme | DeptPhone | Module | AssessType | Score | MaxScore | Lecturer | LecturerPhone | Session |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RU/CSC/2024/001 | Ada Okonkwo | BSc Computer Science | 0801-111-0001 | CSC101 | CA | 18 | 20 | Dr Bello | 0802-222-0002 | 2025/2026 |
| RU/CSC/2024/001 | Ada Okonkwo | BSc Computer Science | 0801-111-0001 | CSC101 | Exam | 54 | 80 | Dr Bello | 0802-222-0002 | 2025/2026 |
| RU/CSC/2024/001 | Ada Okonkwo | BSc Computer Science | 0801-111-0001 | MTH101 | CA | 14 | 20 | Dr Bello | 0802-222-0002 | 2025/2026 |

1NF is satisfied (atomic values) but **partial and transitive dependencies** remain if the key is `(MatricNo, Module, AssessType, Session)`.

## 2NF — full dependence on the whole key

Non-key attributes that depend only on `MatricNo` (student name, programme) or only on `Module` (title, credit units) must leave this table.

After 2NF the facts live in:

- `student` — depends on student identity
- `module` — depends on module identity
- `enrolment` — student takes a module offering
- `grade` — score depends on `(enrolment, assessment)`

`StudentName` no longer sits on a grade row. Updating Ada’s name is one write.

## 3NF — no transitive dependencies

In the 1NF sheet, `DeptPhone` depends on Department, which depends on Programme, which depends on Student. `LecturerPhone` depends on Lecturer, not on the grade key.

3NF moves those attributes:

- `department` holds department contact/site data (here, campus — not a phone on every student)
- `staff` holds lecturer identity and phone
- `module_offering` links lecturer to a taught instance

`grade` now contains only attributes that describe the score itself (`score`, `entered_by`, `entered_at`, `status`) plus the two FKs that identify it.

## BCNF

BCNF requires every determinant to be a candidate key.

Worked example that was rejected:

> “Lecturer determines LecturerPhone, but Lecturer is not a candidate key of the grade sheet.”

That determinant is now the PK of `staff`.

Another potential BCNF issue: if `module_code` determined `module_title` inside `enrolment`, `module_code` would be a determinant that is not a key of enrolment. Titles stay on `module`; enrolment stores `offering_id` only.

`programme_module` uses `(programme_id, module_id)` as the key. `level_year` and `semester_no` describe that pair, not a subset, so BCNF holds.

## Justification of the target NF

| Form | Status in USIRMS | Evidence |
| --- | --- | --- |
| 1NF | Yes | No repeating groups; payments and assessments are rows |
| 2NF | Yes | No composite-key table stores attributes of only one key part |
| 3NF | Yes | Non-key attributes depend only on keys; lecturer/department facts are not copied onto grades |
| BCNF | Yes for designed relations | Determinants (`matric_no`, `module_code`, `staff_number`, `(module_id, semester_id)`) are unique keys |
| Beyond BCNF | Not required | No independent multi-valued attributes remain in one relation |

The module notes that **excessive normalisation can increase join cost**. That trade-off is accepted for the OLTP system of record and revisited in Portfolio 2 (indexes, plans) and Portfolio 4 (document embedding of a student transcript for read-heavy access).

## Controlled denormalisation (declared, not accidental)

`enrolment.final_mark`, `letter_grade`, and `grade_point` cache the approved module result. This is a deliberate 3NF relaxation:

- **Why** — an issued transcript must show the mark that the registrar approved, even if someone later edits a draft assessment.
- **How integrity is kept** — values are written only by the finalisation transaction (Portfolio 3) from published grades and the 5-point rule.
- **What is *not* denormalised** — student name, lecturer phone, and department name are never stored on `grade`.

## Anomaly check against the implemented schema

| Anomaly | Unnormalised sheet | USIRMS schema |
| --- | --- | --- |
| Insert a new module before anyone enrols | Impossible | Insert into `module` |
| Change a lecturer phone | Many grade rows | One `staff` row |
| Delete last enrolment | May lose lecturer/module facts | Module and staff remain |
| Two scores for the same CA | Silent overwrite or extra cell | `UNIQUE (enrolment_id, assessment_id)` rejects the second insert |
