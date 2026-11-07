# Portfolio 3 SQL (evidence)

Connect DBeaver to **`usirms`**. Turn **Auto-commit off** for demos 2–5. Same tab for one demo. Cursor on **one** statement → **Ctrl+Enter**.

| File | Screenshot |
| --- | --- |
| `01_commit.sql` | Last SELECT: Completed / 74 / A / 5 |
| `02_rollback.sql` | Error on −10, then `demo_payment_rows = 0` |
| `03a_isolation_writer.sql` + `03b_isolation_reader.sql` | Two tabs: A=3 Draft, B=26 Published |
| `04_lock_increment.sql` | Last SELECT after locked +1 |
| `05_savepoint.sql` | `requested_rows` kept, `rejected_issued_rows = 0` |

Or all demos at once:

```text
python portfolio-3-transactions-concurrency/scripts/run_transactions.py
```
