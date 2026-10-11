-- USIRMS logical/physical schema (MySQL / MariaDB, InnoDB)
-- University Student Information and Results Management System
-- Riverside University — Portfolio 1
--
-- Engine: InnoDB (row-level locks, FK enforcement, ACID).
-- DBeaver: connect to host 127.0.0.1, port 3306, database usirms.

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP VIEW IF EXISTS v_invoice_balance;
DROP VIEW IF EXISTS v_student_cgpa;
DROP VIEW IF EXISTS v_semester_gpa;
DROP VIEW IF EXISTS v_transcript_line;

DROP TABLE IF EXISTS transcript_issue;
DROP TABLE IF EXISTS fee_payment;
DROP TABLE IF EXISTS fee_invoice;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS timetable_slot;
DROP TABLE IF EXISTS grade;
DROP TABLE IF EXISTS assessment;
DROP TABLE IF EXISTS enrolment;
DROP TABLE IF EXISTS module_offering;
DROP TABLE IF EXISTS semester;
DROP TABLE IF EXISTS academic_session;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS module_prerequisite;
DROP TABLE IF EXISTS programme_module;
DROP TABLE IF EXISTS module;
DROP TABLE IF EXISTS programme;
DROP TABLE IF EXISTS department_head;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS campus;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE campus (
    campus_id     INT          NOT NULL AUTO_INCREMENT,
    campus_code   VARCHAR(8)   NOT NULL,
    campus_name   VARCHAR(80)  NOT NULL,
    city          VARCHAR(80)  NOT NULL,
    PRIMARY KEY (campus_id),
    UNIQUE KEY uk_campus_code (campus_code),
    UNIQUE KEY uk_campus_name (campus_name),
    CONSTRAINT chk_campus_code_len CHECK (CHAR_LENGTH(campus_code) BETWEEN 2 AND 8)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE department (
    department_id   INT          NOT NULL AUTO_INCREMENT,
    department_code VARCHAR(8)   NOT NULL,
    department_name VARCHAR(120) NOT NULL,
    faculty_name    VARCHAR(120) NOT NULL,
    campus_id       INT          NOT NULL,
    created_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (department_id),
    UNIQUE KEY uk_department_code (department_code),
    UNIQUE KEY uk_department_name (department_name),
    CONSTRAINT fk_department_campus
        FOREIGN KEY (campus_id) REFERENCES campus (campus_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE staff (
    staff_id      INT          NOT NULL AUTO_INCREMENT,
    staff_number  VARCHAR(16)  NOT NULL,
    first_name    VARCHAR(60)  NOT NULL,
    last_name     VARCHAR(60)  NOT NULL,
    email         VARCHAR(120) NOT NULL,
    phone         VARCHAR(32)  NULL,
    role          VARCHAR(16)  NOT NULL,
    department_id INT          NULL,
    is_active     TINYINT      NOT NULL DEFAULT 1,
    hired_date    DATE         NOT NULL,
    PRIMARY KEY (staff_id),
    UNIQUE KEY uk_staff_number (staff_number),
    UNIQUE KEY uk_staff_email (email),
    CONSTRAINT chk_staff_role CHECK (role IN ('Lecturer', 'Advisor', 'HoD', 'Registrar', 'Admin')),
    CONSTRAINT chk_staff_active CHECK (is_active IN (0, 1)),
    CONSTRAINT chk_staff_dept CHECK (
        (role IN ('Registrar', 'Admin') AND department_id IS NULL)
        OR (role IN ('Lecturer', 'Advisor', 'HoD') AND department_id IS NOT NULL)
    ),
    CONSTRAINT fk_staff_department
        FOREIGN KEY (department_id) REFERENCES department (department_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE department_head (
    department_id  INT  NOT NULL,
    staff_id       INT  NOT NULL,
    appointed_date DATE NOT NULL,
    PRIMARY KEY (department_id),
    UNIQUE KEY uk_hod_staff (staff_id),
    CONSTRAINT fk_hod_department
        FOREIGN KEY (department_id) REFERENCES department (department_id),
    CONSTRAINT fk_hod_staff
        FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE programme (
    programme_id   INT          NOT NULL AUTO_INCREMENT,
    programme_code VARCHAR(16)  NOT NULL,
    programme_name VARCHAR(160) NOT NULL,
    award_type     VARCHAR(8)   NOT NULL,
    duration_years INT          NOT NULL,
    department_id  INT          NOT NULL,
    PRIMARY KEY (programme_id),
    UNIQUE KEY uk_programme_code (programme_code),
    UNIQUE KEY uk_programme_name_dept (department_id, programme_name),
    CONSTRAINT chk_award_type CHECK (award_type IN ('BSc', 'BA', 'MSc', 'MIT', 'PGD')),
    CONSTRAINT chk_duration CHECK (duration_years BETWEEN 1 AND 6),
    CONSTRAINT fk_programme_department
        FOREIGN KEY (department_id) REFERENCES department (department_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE module (
    module_id     INT          NOT NULL AUTO_INCREMENT,
    module_code   VARCHAR(16)  NOT NULL,
    module_title  VARCHAR(160) NOT NULL,
    credit_units  INT          NOT NULL,
    department_id INT          NOT NULL,
    PRIMARY KEY (module_id),
    UNIQUE KEY uk_module_code (module_code),
    CONSTRAINT chk_credit_units CHECK (credit_units BETWEEN 1 AND 6),
    CONSTRAINT fk_module_department
        FOREIGN KEY (department_id) REFERENCES department (department_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE programme_module (
    programme_id INT     NOT NULL,
    module_id    INT     NOT NULL,
    level_year   INT     NOT NULL,
    semester_no  INT     NOT NULL,
    is_core      TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (programme_id, module_id),
    CONSTRAINT chk_pm_level CHECK (level_year BETWEEN 1 AND 6),
    CONSTRAINT chk_pm_semester CHECK (semester_no IN (1, 2)),
    CONSTRAINT chk_pm_core CHECK (is_core IN (0, 1)),
    CONSTRAINT fk_pm_programme
        FOREIGN KEY (programme_id) REFERENCES programme (programme_id),
    CONSTRAINT fk_pm_module
        FOREIGN KEY (module_id) REFERENCES module (module_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE module_prerequisite (
    module_id              INT NOT NULL,
    prerequisite_module_id INT NOT NULL,
    PRIMARY KEY (module_id, prerequisite_module_id),
    CONSTRAINT chk_no_self_prereq CHECK (module_id <> prerequisite_module_id),
    CONSTRAINT fk_prereq_module
        FOREIGN KEY (module_id) REFERENCES module (module_id),
    CONSTRAINT fk_prereq_required
        FOREIGN KEY (prerequisite_module_id) REFERENCES module (module_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE student (
    student_id       INT          NOT NULL AUTO_INCREMENT,
    matric_no        VARCHAR(32)  NOT NULL,
    first_name       VARCHAR(60)  NOT NULL,
    last_name        VARCHAR(60)  NOT NULL,
    email            VARCHAR(120) NOT NULL,
    date_of_birth    DATE         NOT NULL,
    gender           CHAR(1)      NOT NULL,
    admission_year   INT          NOT NULL,
    programme_id     INT          NOT NULL,
    current_level    INT          NOT NULL,
    status           VARCHAR(16)  NOT NULL,
    advisor_staff_id INT          NULL,
    campus_id        INT          NOT NULL,
    PRIMARY KEY (student_id),
    UNIQUE KEY uk_matric_no (matric_no),
    UNIQUE KEY uk_student_email (email),
    CONSTRAINT chk_gender CHECK (gender IN ('F', 'M', 'X')),
    CONSTRAINT chk_admission_year CHECK (admission_year BETWEEN 2000 AND 2100),
    CONSTRAINT chk_current_level CHECK (current_level BETWEEN 1 AND 6),
    CONSTRAINT chk_student_status CHECK (status IN ('Active', 'Suspended', 'Graduated', 'Withdrawn')),
    CONSTRAINT fk_student_programme
        FOREIGN KEY (programme_id) REFERENCES programme (programme_id),
    CONSTRAINT fk_student_advisor
        FOREIGN KEY (advisor_staff_id) REFERENCES staff (staff_id),
    CONSTRAINT fk_student_campus
        FOREIGN KEY (campus_id) REFERENCES campus (campus_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE academic_session (
    session_id    INT         NOT NULL AUTO_INCREMENT,
    session_label VARCHAR(16) NOT NULL,
    start_date    DATE        NOT NULL,
    end_date      DATE        NOT NULL,
    is_current    TINYINT     NOT NULL DEFAULT 0,
    PRIMARY KEY (session_id),
    UNIQUE KEY uk_session_label (session_label),
    CONSTRAINT chk_session_current CHECK (is_current IN (0, 1)),
    CONSTRAINT chk_session_dates CHECK (end_date > start_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE semester (
    semester_id INT         NOT NULL AUTO_INCREMENT,
    session_id  INT         NOT NULL,
    semester_no INT         NOT NULL,
    start_date  DATE        NOT NULL,
    end_date    DATE        NOT NULL,
    status      VARCHAR(16) NOT NULL,
    PRIMARY KEY (semester_id),
    UNIQUE KEY uk_session_semester (session_id, semester_no),
    CONSTRAINT chk_semester_no CHECK (semester_no IN (1, 2)),
    CONSTRAINT chk_semester_status CHECK (status IN ('Planned', 'Open', 'Closed')),
    CONSTRAINT chk_semester_dates CHECK (end_date > start_date),
    CONSTRAINT fk_semester_session
        FOREIGN KEY (session_id) REFERENCES academic_session (session_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE module_offering (
    offering_id       INT NOT NULL AUTO_INCREMENT,
    module_id         INT NOT NULL,
    semester_id       INT NOT NULL,
    lecturer_staff_id INT NOT NULL,
    capacity          INT NOT NULL,
    PRIMARY KEY (offering_id),
    UNIQUE KEY uk_module_semester (module_id, semester_id),
    CONSTRAINT chk_capacity CHECK (capacity > 0),
    CONSTRAINT fk_offering_module
        FOREIGN KEY (module_id) REFERENCES module (module_id),
    CONSTRAINT fk_offering_semester
        FOREIGN KEY (semester_id) REFERENCES semester (semester_id),
    CONSTRAINT fk_offering_lecturer
        FOREIGN KEY (lecturer_staff_id) REFERENCES staff (staff_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE enrolment (
    enrolment_id INT         NOT NULL AUTO_INCREMENT,
    student_id   INT         NOT NULL,
    offering_id  INT         NOT NULL,
    enrolled_on  DATE        NOT NULL,
    status       VARCHAR(16) NOT NULL,
    final_mark   DECIMAL(5,2) NULL,
    letter_grade CHAR(1)      NULL,
    grade_point  INT          NULL,
    PRIMARY KEY (enrolment_id),
    UNIQUE KEY uk_student_offering (student_id, offering_id),
    CONSTRAINT chk_enrol_status CHECK (status IN ('Registered', 'Dropped', 'Completed')),
    CONSTRAINT chk_final_mark CHECK (final_mark IS NULL OR (final_mark >= 0 AND final_mark <= 100)),
    CONSTRAINT chk_letter_grade CHECK (letter_grade IS NULL OR letter_grade IN ('A', 'B', 'C', 'D', 'E', 'F')),
    CONSTRAINT chk_grade_point CHECK (grade_point IS NULL OR (grade_point >= 0 AND grade_point <= 5)),
    CONSTRAINT fk_enrol_student
        FOREIGN KEY (student_id) REFERENCES student (student_id),
    CONSTRAINT fk_enrol_offering
        FOREIGN KEY (offering_id) REFERENCES module_offering (offering_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE assessment (
    assessment_id   INT           NOT NULL AUTO_INCREMENT,
    offering_id     INT           NOT NULL,
    assessment_type VARCHAR(16)   NOT NULL,
    title           VARCHAR(160)  NOT NULL,
    weight_percent  DECIMAL(5,2)  NOT NULL,
    max_score       DECIMAL(6,2)  NOT NULL,
    due_date        DATE          NOT NULL,
    PRIMARY KEY (assessment_id),
    CONSTRAINT chk_assess_type CHECK (assessment_type IN ('CA', 'Exam', 'Project', 'Practical')),
    CONSTRAINT chk_weight CHECK (weight_percent > 0 AND weight_percent <= 100),
    CONSTRAINT chk_max_score CHECK (max_score > 0),
    CONSTRAINT fk_assess_offering
        FOREIGN KEY (offering_id) REFERENCES module_offering (offering_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE grade (
    grade_id      INT           NOT NULL AUTO_INCREMENT,
    enrolment_id  INT           NOT NULL,
    assessment_id INT           NOT NULL,
    score         DECIMAL(6,2)  NOT NULL,
    entered_by    INT           NOT NULL,
    entered_at    DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status        VARCHAR(16)   NOT NULL,
    PRIMARY KEY (grade_id),
    UNIQUE KEY uk_enrol_assess (enrolment_id, assessment_id),
    CONSTRAINT chk_score CHECK (score >= 0),
    CONSTRAINT chk_grade_status CHECK (status IN ('Draft', 'Submitted', 'Published')),
    CONSTRAINT fk_grade_enrolment
        FOREIGN KEY (enrolment_id) REFERENCES enrolment (enrolment_id),
    CONSTRAINT fk_grade_assessment
        FOREIGN KEY (assessment_id) REFERENCES assessment (assessment_id),
    CONSTRAINT fk_grade_entered_by
        FOREIGN KEY (entered_by) REFERENCES staff (staff_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE timetable_slot (
    slot_id     INT         NOT NULL AUTO_INCREMENT,
    offering_id INT         NOT NULL,
    day_of_week CHAR(3)     NOT NULL,
    start_time  TIME        NOT NULL,
    end_time    TIME        NOT NULL,
    venue       VARCHAR(40) NOT NULL,
    slot_type   VARCHAR(16) NOT NULL,
    PRIMARY KEY (slot_id),
    CONSTRAINT chk_dow CHECK (day_of_week IN ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')),
    CONSTRAINT chk_slot_type CHECK (slot_type IN ('Lecture', 'Tutorial', 'Lab')),
    CONSTRAINT chk_slot_times CHECK (end_time > start_time),
    CONSTRAINT fk_slot_offering
        FOREIGN KEY (offering_id) REFERENCES module_offering (offering_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE attendance (
    attendance_id   INT         NOT NULL AUTO_INCREMENT,
    slot_id         INT         NOT NULL,
    student_id      INT         NOT NULL,
    attendance_date DATE        NOT NULL,
    status          VARCHAR(16) NOT NULL,
    PRIMARY KEY (attendance_id),
    UNIQUE KEY uk_slot_student_date (slot_id, student_id, attendance_date),
    CONSTRAINT chk_attend_status CHECK (status IN ('Present', 'Absent', 'Late', 'Excused')),
    CONSTRAINT fk_attend_slot
        FOREIGN KEY (slot_id) REFERENCES timetable_slot (slot_id),
    CONSTRAINT fk_attend_student
        FOREIGN KEY (student_id) REFERENCES student (student_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE fee_invoice (
    invoice_id INT            NOT NULL AUTO_INCREMENT,
    student_id INT            NOT NULL,
    session_id INT            NOT NULL,
    amount_due DECIMAL(12,2)  NOT NULL,
    due_date   DATE           NOT NULL,
    status     VARCHAR(16)    NOT NULL,
    PRIMARY KEY (invoice_id),
    UNIQUE KEY uk_student_session_fee (student_id, session_id),
    CONSTRAINT chk_amount_due CHECK (amount_due >= 0),
    CONSTRAINT chk_invoice_status CHECK (status IN ('Unpaid', 'Partial', 'Paid')),
    CONSTRAINT fk_invoice_student
        FOREIGN KEY (student_id) REFERENCES student (student_id),
    CONSTRAINT fk_invoice_session
        FOREIGN KEY (session_id) REFERENCES academic_session (session_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE fee_payment (
    payment_id   INT            NOT NULL AUTO_INCREMENT,
    invoice_id   INT            NOT NULL,
    amount_paid  DECIMAL(12,2)  NOT NULL,
    paid_on      DATE           NOT NULL,
    method       VARCHAR(16)    NOT NULL,
    reference_no VARCHAR(40)    NOT NULL,
    PRIMARY KEY (payment_id),
    UNIQUE KEY uk_payment_ref (reference_no),
    CONSTRAINT chk_amount_paid CHECK (amount_paid > 0),
    CONSTRAINT chk_pay_method CHECK (method IN ('Transfer', 'Card', 'Cash', 'Scholarship')),
    CONSTRAINT fk_payment_invoice
        FOREIGN KEY (invoice_id) REFERENCES fee_invoice (invoice_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE transcript_issue (
    issue_id     INT          NOT NULL AUTO_INCREMENT,
    student_id   INT          NOT NULL,
    requested_on DATETIME     NOT NULL,
    issued_on    DATETIME     NULL,
    issued_by    INT          NULL,
    purpose      VARCHAR(160) NOT NULL,
    status       VARCHAR(16)  NOT NULL,
    PRIMARY KEY (issue_id),
    CONSTRAINT chk_issue_status CHECK (status IN ('Requested', 'Approved', 'Issued', 'Rejected')),
    CONSTRAINT chk_issued_complete CHECK (
        (status = 'Issued' AND issued_on IS NOT NULL AND issued_by IS NOT NULL)
        OR (status <> 'Issued')
    ),
    CONSTRAINT fk_issue_student
        FOREIGN KEY (student_id) REFERENCES student (student_id),
    CONSTRAINT fk_issue_staff
        FOREIGN KEY (issued_by) REFERENCES staff (staff_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE VIEW v_transcript_line AS
SELECT
    s.student_id,
    s.matric_no,
    sess.session_label,
    sem.semester_no,
    m.module_code,
    m.module_title,
    m.credit_units,
    e.final_mark,
    e.letter_grade,
    e.grade_point,
    e.status AS enrolment_status
FROM enrolment e
JOIN student s             ON s.student_id = e.student_id
JOIN module_offering o     ON o.offering_id = e.offering_id
JOIN module m              ON m.module_id = o.module_id
JOIN semester sem          ON sem.semester_id = o.semester_id
JOIN academic_session sess ON sess.session_id = sem.session_id;

CREATE VIEW v_semester_gpa AS
SELECT
    e.student_id,
    o.semester_id,
    ROUND(SUM(e.grade_point * m.credit_units) / SUM(m.credit_units), 2) AS semester_gpa,
    SUM(m.credit_units) AS credit_units
FROM enrolment e
JOIN module_offering o ON o.offering_id = e.offering_id
JOIN module m          ON m.module_id = o.module_id
WHERE e.status = 'Completed'
  AND e.grade_point IS NOT NULL
GROUP BY e.student_id, o.semester_id;

CREATE VIEW v_student_cgpa AS
SELECT
    e.student_id,
    ROUND(SUM(e.grade_point * m.credit_units) / SUM(m.credit_units), 2) AS cgpa,
    SUM(m.credit_units) AS credit_units_completed
FROM enrolment e
JOIN module_offering o ON o.offering_id = e.offering_id
JOIN module m          ON m.module_id = o.module_id
WHERE e.status = 'Completed'
  AND e.grade_point IS NOT NULL
GROUP BY e.student_id;

CREATE VIEW v_invoice_balance AS
SELECT
    i.invoice_id,
    i.student_id,
    i.session_id,
    i.amount_due,
    COALESCE(SUM(p.amount_paid), 0) AS amount_paid,
    ROUND(i.amount_due - COALESCE(SUM(p.amount_paid), 0), 2) AS balance,
    i.status
FROM fee_invoice i
LEFT JOIN fee_payment p ON p.invoice_id = i.invoice_id
GROUP BY i.invoice_id, i.student_id, i.session_id, i.amount_due, i.status;
