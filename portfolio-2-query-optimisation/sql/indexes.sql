-- Secondary indexes for USIRMS reporting (Portfolio 2).
-- InnoDB already indexes PRIMARY KEY, UNIQUE, and FOREIGN KEY columns.
-- These extras target filters (status, letter_grade) and covering composites.

CREATE INDEX idx_student_status_programme
    ON student (status, programme_id);

CREATE INDEX idx_enrolment_student_status
    ON enrolment (student_id, status);

CREATE INDEX idx_enrolment_offering_status
    ON enrolment (offering_id, status);

CREATE INDEX idx_enrolment_letter
    ON enrolment (letter_grade, status);

CREATE INDEX idx_grade_enrolment_status
    ON grade (enrolment_id, status);

CREATE INDEX idx_offering_semester_lecturer
    ON module_offering (semester_id, lecturer_staff_id);

CREATE INDEX idx_attendance_student_status
    ON attendance (student_id, status);

CREATE INDEX idx_invoice_session_status
    ON fee_invoice (session_id, status);

ANALYZE TABLE
    student, enrolment, grade, module_offering, attendance, fee_invoice,
    programme, department, academic_session, semester, module;
