-- DEMO 2 ROLLBACK — same SQL editor tab for the whole demo.
-- DBeaver: turn Auto-commit OFF (toolbar) or use Manual commit, then Ctrl+Enter each line.
-- Expect: error on -10 INSERT → run ROLLBACK → last SELECT shows demo_payment_rows = 0.

START TRANSACTION;

INSERT INTO fee_payment (invoice_id, amount_paid, paid_on, method, reference_no)
VALUES (1, 50000, CURDATE(), 'Transfer', 'PAY-DEMO-ROLLBACK');

INSERT INTO fee_payment (invoice_id, amount_paid, paid_on, method, reference_no)
VALUES (1, -10, CURDATE(), 'Transfer', 'PAY-DEMO-NEG');

ROLLBACK;

SELECT COUNT(*) AS demo_payment_rows
FROM fee_payment
WHERE reference_no IN ('PAY-DEMO-ROLLBACK', 'PAY-DEMO-NEG');
