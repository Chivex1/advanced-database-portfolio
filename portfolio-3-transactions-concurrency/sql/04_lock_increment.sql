-- DEMO 4 control — Ctrl+Enter each statement. Screenshot last SELECT.

UPDATE grade SET score = 20 WHERE grade_id = 4;

START TRANSACTION;

SELECT score FROM grade WHERE grade_id = 4 FOR UPDATE;

UPDATE grade SET score = score + 1 WHERE grade_id = 4;

COMMIT;

SELECT score FROM grade WHERE grade_id = 4;
