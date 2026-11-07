-- DEMO 3 TAB A (writer) — leave open until after Tab B screenshot.
-- Ctrl+Enter each statement. Do NOT COMMIT. Screenshot after the SELECT (score=3).

SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;

START TRANSACTION;

UPDATE grade SET score = 3, status = 'Draft' WHERE grade_id = 1;

SELECT score, status FROM grade WHERE grade_id = 1;

-- After Tab B screenshot:
ROLLBACK;
