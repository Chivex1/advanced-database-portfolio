# Case study statement

This statement is the single organisational context used in every portfolio in this repository.

## Organisation / scenario

**Riverside University** is a multi-faculty tertiary institution. It operates the **University Student Information and Results Management System (USIRMS)** as its operational student-records and results platform.

USIRMS is an **OLTP** academic administration system: many concurrent users perform short, integrity-critical updates (registration, grade entry, fee posting, record amendments) and a smaller set of users run reporting queries (GPA, transcripts, departmental summaries).

The system is **not** a data warehouse. Historical analysis is supported by reporting queries and, later, by optional analytical copies (Portfolios 4 and 5). The system of record for grades, fees, and enrolment remains the relational database designed here.

## Nature of the system

USIRMS stores and protects the official academic record of each student from admission through graduation. It must:

- keep student, programme, and module data consistent across departments
- support semester registration without duplicate or conflicting enrolments
- accept assessment scores and derive module marks, letter grades, and GPA
- produce official transcripts that match stored results
- record timetables, attendance, and fee invoices/payments
- restrict each class of user to the operations they are authorised to perform

Because results and fees are official records, the relational design follows **ACID** transaction properties (Portfolio 3). Complementary NoSQL and distributed models are evaluated later for specific workloads, not as a replacement for the system of record.

## Users of the database

| Role | Typical access | Typical operations |
| --- | --- | --- |
| Student | Own record only | View enrolment, timetable, grades once published, fee balance, request a transcript |
| Lecturer | Assigned module offerings | Enter and amend assessment scores; view class lists and attendance |
| Academic advisor | Assigned advisees | Review advisee enrolment, GPA, and academic status |
| Head of Department (HoD) | Own department | Approve offerings, review departmental results and workload |
| Registrar staff | Institution-wide academic records | Register students, open/close semesters, issue transcripts, correct records |
| Administrator | System-wide | Maintain departments, staff, programmes, modules, security, and reference data |

Staff are stored in one `staff` table with a `role` domain. A lecturer may also act as an advisor (`student.advisor_staff_id`). A department has at most one current HoD (`department_head`).

## Major data stored

Students, departments, campuses, programmes, modules and prerequisites, lecturers and other staff, academic sessions and semesters, module offerings, enrolments, assessments, grades, timetables, attendance, fee invoices, fee payments, and transcript issues.

Derived facts (module final mark, letter grade, grade point, semester GPA, CGPA) are computed from stored scores and credit units using published rules. They may be cached on `enrolment` after a controlled results-finalisation transaction so that an issued transcript cannot drift from the mark that was approved.

## Key operations the database supports

1. **Registration** — enrol an eligible student on a module offering for a semester.
2. **Grade entry** — record assessment scores, then finalise the module result.
3. **GPA / CGPA** — compute credit-weighted grade points for a semester or the full record.
4. **Transcript generation and issue** — produce the official academic record and log issuance.
5. **Timetable tracking** — store teaching slots and detect venue/lecturer clashes.
6. **Attendance recording** — mark presence against a scheduled slot and date.
7. **Record updates** — amend student, staff, programme, and module data under constraints.
8. **Reporting** — departmental result summaries, failure rates, outstanding fees, lecturer workload, enrolment census.

## Why this case study supports the full module

| Portfolio | Why USIRMS is a fit |
| --- | --- |
| 1 Design | Many entities, composite relationships, and integrity rules that must be normalised |
| 2 Query optimisation | Multi-join reporting (transcripts, GPA rankings, fees) that benefit from indexes and plan analysis |
| 3 Transactions | Grade finalisation and registration must commit or roll back as a unit |
| 4 NoSQL | Student-centric documents, session key-value cache, and prerequisite graphs are natural alternatives for *some* reads |
| 5 Distributed / cloud | Multi-campus fragmentation, registrar replicas, and CAP trade-offs around results vs read replicas |

## Design stages applied (module Session 1)

The work in this folder follows the module’s database-design stages:

1. **Requirements analysis** — users, data, and operations listed above.
2. **Conceptual design** — ERD in `02-erd.md` (implementation-independent).
3. **Logical design** — relational schema, keys, constraints, and normalisation in `03`–`05`.
4. **Physical design** — MySQL/MariaDB (InnoDB) implementation, indexes introduced where justified (Portfolio 2). Open in DBeaver.
5. **Testing and evaluation** — integrity scripts and recreate steps in this folder’s README.
6. **Deployment and maintenance** — scripts are versioned so the database can be rebuilt from source.
