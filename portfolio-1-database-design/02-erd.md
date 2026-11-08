# Conceptual design — Entity-Relationship model

This ERD is the **conceptual** model from the module design stages: it is independent of physical storage details. The logical schema in `03-relational-schema.md` is the mapped relational form (implemented on MySQL/MariaDB InnoDB).

Chen-style notation used in the module:

- Entity — rectangle
- Relationship — diamond (shown here as labelled connectors)
- Attribute — ellipse (listed under each entity)
- Multi-valued / composite attributes are avoided; repeating data is modelled as entities

## Cardinality summary

| Relationship | Cardinality | Rule |
| --- | --- | --- |
| Campus hosts Department | 1 : N | A campus has many departments; a department belongs to one home campus |
| Department employs Staff | 1 : N | Staff (except Registrar/Admin) belong to one department |
| Department headed-by Staff | 1 : 0..1 | At most one current HoD |
| Department offers Programme | 1 : N | A programme belongs to one department |
| Department owns Module | 1 : N | A module has one owning department |
| Programme includes Module | M : N | Via `programme_module` (level, semester, core/elective) |
| Module requires Module | M : N | Prerequisites (no self-prerequisite) |
| Student belongs-to Programme | N : 1 | A student has one registered programme |
| Staff advises Student | 1 : N | An advisor may have many advisees |
| Session contains Semester | 1 : 2 | Two semesters per session |
| Module offered-in Semester | M : N | Via `module_offering` with one lecturer |
| Student enrols-on Offering | M : N | Via `enrolment` |
| Offering has Assessment | 1 : N | CA, exam, project, practical |
| Enrolment receives Grade | 1 : N | One score per assessment |
| Offering scheduled-as Slot | 1 : N | Timetable rows |
| Student attends Slot | M : N | Via `attendance` on a date |
| Student billed-by Invoice | 1 : N | One invoice per student per session |
| Invoice collected-as Payment | 1 : N | Partial payments allowed |
| Student requests TranscriptIssue | 1 : N | Issuance is logged, not stored as a duplicate of results |

## ERD (logical-level Crow’s Foot)

```mermaid
erDiagram
    CAMPUS ||--o{ DEPARTMENT : hosts
    DEPARTMENT ||--o{ STAFF : employs
    DEPARTMENT ||--o| DEPARTMENT_HEAD : has
    STAFF ||--o| DEPARTMENT_HEAD : appointed_as
    DEPARTMENT ||--o{ PROGRAMME : offers
    DEPARTMENT ||--o{ MODULE : owns
    PROGRAMME ||--o{ PROGRAMME_MODULE : structures
    MODULE ||--o{ PROGRAMME_MODULE : included_in
    MODULE ||--o{ MODULE_PREREQUISITE : has
    MODULE ||--o{ MODULE_PREREQUISITE : required_by
    PROGRAMME ||--o{ STUDENT : registers
    STAFF ||--o{ STUDENT : advises
    CAMPUS ||--o{ STUDENT : studies_at
    ACADEMIC_SESSION ||--o{ SEMESTER : contains
    MODULE ||--o{ MODULE_OFFERING : offered_as
    SEMESTER ||--o{ MODULE_OFFERING : schedules
    STAFF ||--o{ MODULE_OFFERING : teaches
    STUDENT ||--o{ ENROLMENT : makes
    MODULE_OFFERING ||--o{ ENROLMENT : receives
    MODULE_OFFERING ||--o{ ASSESSMENT : sets
    ENROLMENT ||--o{ GRADE : earns
    ASSESSMENT ||--o{ GRADE : scored_as
    STAFF ||--o{ GRADE : enters
    MODULE_OFFERING ||--o{ TIMETABLE_SLOT : timetabled
    TIMETABLE_SLOT ||--o{ ATTENDANCE : marked_on
    STUDENT ||--o{ ATTENDANCE : records
    STUDENT ||--o{ FEE_INVOICE : billed
    ACADEMIC_SESSION ||--o{ FEE_INVOICE : for
    FEE_INVOICE ||--o{ FEE_PAYMENT : collected
    STUDENT ||--o{ TRANSCRIPT_ISSUE : requests
    STAFF ||--o{ TRANSCRIPT_ISSUE : issues

    CAMPUS {
        int campus_id PK
        string campus_code UK
        string campus_name
        string city
    }
    DEPARTMENT {
        int department_id PK
        string department_code UK
        string department_name UK
        string faculty_name
        int campus_id FK
    }
    STAFF {
        int staff_id PK
        string staff_number UK
        string first_name
        string last_name
        string email UK
        string role
        int department_id FK
    }
    DEPARTMENT_HEAD {
        int department_id PK_FK
        int staff_id FK
        date appointed_date
    }
    PROGRAMME {
        int programme_id PK
        string programme_code UK
        string programme_name
        string award_type
        int duration_years
        int department_id FK
    }
    MODULE {
        int module_id PK
        string module_code UK
        string module_title
        int credit_units
        int department_id FK
    }
    PROGRAMME_MODULE {
        int programme_id PK_FK
        int module_id PK_FK
        int level_year
        int semester_no
        int is_core
    }
    MODULE_PREREQUISITE {
        int module_id PK_FK
        int prerequisite_module_id PK_FK
    }
    STUDENT {
        int student_id PK
        string matric_no UK
        string first_name
        string last_name
        string email UK
        string gender
        int programme_id FK
        int current_level
        string status
        int advisor_staff_id FK
        int campus_id FK
    }
    ACADEMIC_SESSION {
        int session_id PK
        string session_label UK
        date start_date
        date end_date
        int is_current
    }
    SEMESTER {
        int semester_id PK
        int session_id FK
        int semester_no
        string status
    }
    MODULE_OFFERING {
        int offering_id PK
        int module_id FK
        int semester_id FK
        int lecturer_staff_id FK
        int capacity
    }
    ENROLMENT {
        int enrolment_id PK
        int student_id FK
        int offering_id FK
        string status
        float final_mark
        string letter_grade
        int grade_point
    }
    ASSESSMENT {
        int assessment_id PK
        int offering_id FK
        string assessment_type
        float weight_percent
        float max_score
    }
    GRADE {
        int grade_id PK
        int enrolment_id FK
        int assessment_id FK
        float score
        int entered_by FK
        string status
    }
    TIMETABLE_SLOT {
        int slot_id PK
        int offering_id FK
        string day_of_week
        string start_time
        string end_time
        string venue
    }
    ATTENDANCE {
        int attendance_id PK
        int slot_id FK
        int student_id FK
        date attendance_date
        string status
    }
    FEE_INVOICE {
        int invoice_id PK
        int student_id FK
        int session_id FK
        float amount_due
        string status
    }
    FEE_PAYMENT {
        int payment_id PK
        int invoice_id FK
        float amount_paid
        string reference_no UK
    }
    TRANSCRIPT_ISSUE {
        int issue_id PK
        int student_id FK
        string purpose
        string status
        int issued_by FK
    }
```

## Design notes that affect later portfolios

- **Campus** is a first-class entity so Portfolio 5 can fragment students and offerings by site without inventing a new schema.
- **Module offering** separates the catalogue module from a taught instance. Grades attach to the instance, which is required for historical transcripts.
- **Transcript issue** is a request/audit entity. The transcript *content* is a query over enrolments (Portfolio 2), not a second copy of every grade.
- **Fee invoice + payment** models a one-to-many collection so partial payments do not violate 1NF.
- Weak/associative entities (`programme_module`, `enrolment`, `grade`, `attendance`) carry their own attributes and therefore appear as relations, not as attributes of a parent.
