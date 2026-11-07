-- DEMO 1 COMMIT — put cursor on ONE statement, Ctrl+Enter, next…
-- Screenshot after the last SELECT (Completed / 74 / A / 5).

START TRANSACTION;

INSERT INTO grade (enrolment_id, assessment_id, score, entered_by, status)
SELECT 2, a.assessment_id,
       CASE a.assessment_type WHEN 'CA' THEN 24.0 WHEN 'Exam' THEN 50.0 END,
       1, 'Published'
FROM assessment a
JOIN enrolment e ON e.offering_id = a.offering_id
WHERE e.enrolment_id = 2
ON DUPLICATE KEY UPDATE
    score = VALUES(score), status = 'Published',
    entered_by = VALUES(entered_by), entered_at = CURRENT_TIMESTAMP;

UPDATE enrolment
SET status = 'Completed', final_mark = 74.00, letter_grade = 'A', grade_point = 5
WHERE enrolment_id = 2;

COMMIT;

SELECT enrolment_id, status, final_mark, letter_grade, grade_point
FROM enrolment WHERE enrolment_id = 2;
