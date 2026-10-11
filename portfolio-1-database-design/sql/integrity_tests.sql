-- Integrity tests for USIRMS.
-- Each statement below is INTENTIONALLY illegal.
-- scripts/build_database.py runs them one by one and records the engine error.
-- A pass means the engine rejected the row. A fail means the constraint is missing.

-- 1. Duplicate business key (entity integrity / UNIQUE)
INSERT INTO student (
    matric_no, first_name, last_name, email, date_of_birth, gender,
    admission_year, programme_id, current_level, status, campus_id
) VALUES (
    'RU/CSC/2024/001', 'Copy', 'Cat', 'copy.cat@riverside.test', '2002-01-01', 'F',
    2024, 1, 2, 'Active', 1
);

-- 2. Orphan grade (referential integrity)
INSERT INTO grade (enrolment_id, assessment_id, score, entered_by, status)
VALUES (999999, 1, 10, 1, 'Draft');

-- 3. Negative score (domain CHECK)
INSERT INTO grade (enrolment_id, assessment_id, score, entered_by, status)
VALUES (1, 1, -5, 1, 'Draft');

-- 4. Double enrolment (UNIQUE student + offering)
INSERT INTO enrolment (student_id, offering_id, enrolled_on, status)
SELECT student_id, offering_id, CURDATE(), 'Registered'
FROM enrolment
WHERE enrolment_id = 1;

-- 5. Self-prerequisite
INSERT INTO module_prerequisite (module_id, prerequisite_module_id)
VALUES (1, 1);

-- 6. Issued transcript without issuer
INSERT INTO transcript_issue (student_id, requested_on, purpose, status)
VALUES (1, NOW(), 'Job application', 'Issued');

-- 7. Academic staff without a department
INSERT INTO staff (staff_number, first_name, last_name, email, role, hired_date)
VALUES ('STF9999', 'No', 'Dept', 'no.dept@riverside.test', 'Lecturer', '2020-01-01');

-- 8. Duplicate payment reference
INSERT INTO fee_payment (invoice_id, amount_paid, paid_on, method, reference_no)
SELECT invoice_id, 1000, CURDATE(), 'Transfer', reference_no
FROM fee_payment
WHERE payment_id = 1;
