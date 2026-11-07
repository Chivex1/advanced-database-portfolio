-- DEMO 3 TAB B (reader) — second connection, while Tab A still open.
-- Screenshot this result: score should still be 26 Published (no dirty read).

SELECT score, status FROM grade WHERE grade_id = 1;
