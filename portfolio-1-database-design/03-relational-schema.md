# Logical design — relational schema

The ERD is mapped to relations using the standard rules from the module:

- Each strong entity becomes a relation.
- Each 1:N relationship is implemented as a foreign key on the N side.
- Each M:N relationship becomes an associative relation with its own attributes.
- 1:1 optional relationships (`department_head`) use the entity that is optional as the dependent relation, with the parent key as primary key.

Physical DBMS for this portfolio: **MySQL / MariaDB (InnoDB)**, so the schema can be opened in DBeaver as a server database. The logical model is DBMS-neutral; types are `INT` / `VARCHAR` / `DATE` / `DECIMAL`.

Full DDL: [`sql/schema.sql`](sql/schema.sql)

## Relations and attributes

### campus
`campus(campus_id, campus_code, campus_name, city)`

Supports multi-site allocation used in Portfolio 5 (horizontal fragmentation by campus).

### department
`department(department_id, department_code, department_name, faculty_name, campus_id, created_at)`

### staff
`staff(staff_id, staff_number, first_name, last_name, email, phone, role, department_id, is_active, hired_date)`

One relation for all human actors who are not students. Role is a domain (`Lecturer`, `Advisor`, `HoD`, `Registrar`, `Admin`). Registrar and Admin have no home department.

### department_head
`department_head(department_id, staff_id, appointed_date)`

Separates the “current HoD” fact from staff so a department cannot have two current heads and a staff member cannot head two departments.

### programme
`programme(programme_id, programme_code, programme_name, award_type, duration_years, department_id)`

### module
`module(module_id, module_code, module_title, credit_units, department_id)`

Catalogue entry. Teaching instance is `module_offering`.

### programme_module
`programme_module(programme_id, module_id, level_year, semester_no, is_core)`

Curriculum map: which module appears in which programme, at which level and semester.

### module_prerequisite
`module_prerequisite(module_id, prerequisite_module_id)`

Graph of academic dependence. Used in Portfolio 4 as a graph-model comparison.

### student
`student(student_id, matric_no, first_name, last_name, email, date_of_birth, gender, admission_year, programme_id, current_level, status, advisor_staff_id, campus_id)`

### academic_session / semester
`academic_session(session_id, session_label, start_date, end_date, is_current)`  
`semester(semester_id, session_id, semester_no, start_date, end_date, status)`

### module_offering
`module_offering(offering_id, module_id, semester_id, lecturer_staff_id, capacity)`

A module taught in a specific semester by a named lecturer.

### enrolment
`enrolment(enrolment_id, student_id, offering_id, enrolled_on, status, final_mark, letter_grade, grade_point)`

`final_mark` / `letter_grade` / `grade_point` are **controlled caches** written by the results-finalisation transaction (Portfolio 3). They are not a second source of assessment scores.

### assessment
`assessment(assessment_id, offering_id, assessment_type, title, weight_percent, max_score, due_date)`

### grade
`grade(grade_id, enrolment_id, assessment_id, score, entered_by, entered_at, status)`

Atomic score. One row per enrolment per assessment.

### timetable_slot
`timetable_slot(slot_id, offering_id, day_of_week, start_time, end_time, venue, slot_type)`

### attendance
`attendance(attendance_id, slot_id, student_id, attendance_date, status)`

### fee_invoice / fee_payment
`fee_invoice(invoice_id, student_id, session_id, amount_due, due_date, status)`  
`fee_payment(payment_id, invoice_id, amount_paid, paid_on, method, reference_no)`

### transcript_issue
`transcript_issue(issue_id, student_id, requested_on, issued_on, issued_by, purpose, status)`

Audit of official copies. Content comes from `v_transcript_line`.

## Derived views

| View | Purpose |
| --- | --- |
| `v_transcript_line` | Official module lines for a student |
| `v_semester_gpa` | Credit-weighted GPA per student per semester |
| `v_student_cgpa` | Credit-weighted CGPA |
| `v_invoice_balance` | Amount due minus payments |

## Grade-point rule (Nigerian 5-point scale)

Used consistently in views, seed data, and later portfolios.

| Final mark | Letter | Grade point |
| ---: | --- | ---: |
| 70–100 | A | 5 |
| 60–69 | B | 4 |
| 50–59 | C | 3 |
| 45–49 | D | 2 |
| 40–44 | E | 1 |
| 0–39 | F | 0 |

GPA = Σ(grade_point × credit_units) / Σ(credit_units) for completed enrolments.

## Mapping from conceptual to logical

| Conceptual construct | Relational implementation |
| --- | --- |
| Entity | Base table |
| 1:N relationship | FK on child |
| M:N relationship | Associative table with composite PK or surrogate + UNIQUE |
| Attribute | Column with domain CHECK |
| Derived attribute (GPA) | View, not a stored column on `student` |
| Multi-valued payment history | Separate `fee_payment` rows |
| Identifying relationship (offering) | `UNIQUE (module_id, semester_id)` |
