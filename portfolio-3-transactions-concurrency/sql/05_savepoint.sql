-- DEMO 5 SAVEPOINT — Ctrl+Enter each. Expect error on Issued insert, then continue.
-- Screenshot after the final SELECT (requested kept, issued = 0).

START TRANSACTION;

UPDATE student SET current_level = current_level WHERE student_id = 1;

SAVEPOINT fee_note;

INSERT INTO transcript_issue (student_id, requested_on, purpose, status)
VALUES (1, NOW(), 'Demo invalid issued row', 'Issued');

ROLLBACK TO SAVEPOINT fee_note;

INSERT INTO transcript_issue (student_id, requested_on, purpose, status)
VALUES (1, NOW(), 'Verification copy', 'Requested');

RELEASE SAVEPOINT fee_note;

COMMIT;

SELECT
  (SELECT COUNT(*) FROM transcript_issue
   WHERE student_id = 1 AND purpose = 'Verification copy') AS requested_rows,
  (SELECT COUNT(*) FROM transcript_issue
   WHERE purpose = 'Demo invalid issued row') AS rejected_issued_rows;
