# Portfolio 3 — Transactions and Concurrency

**Case study:** USIRMS  
**DBMS:** MySQL / MariaDB InnoDB — two connections, `REPEATABLE READ` (default)

## Write-ups and scripts

| Path | Content |
| --- | --- |
| [01-acid-and-demos.md](01-acid-and-demos.md) | ACID mapping and demo list |
| [scripts/run_transactions.py](scripts/run_transactions.py) | Automated five demos |
| [sql/](sql/) | Same demos step-by-step in DBeaver ([sql/README.md](sql/README.md)) |

## Recreate

```text
python portfolio-3-transactions-concurrency/scripts/run_transactions.py
```

Requires existing `usirms` (run Portfolio 2 first if the database was dropped).

## Evidence (assessor)

| File | What it shows |
| --- | --- |
| [evidence/transaction_output.txt](evidence/transaction_output.txt) | **Primary** — commit, rollback, isolation, lost update (21 vs 22), savepoint |
| [evidence/01_commit.png](evidence/01_commit.png) … [05_savepoint.png](evidence/05_savepoint.png) | Optional DBeaver screenshots aligned with `sql/*.sql` |

Pass checks in `transaction_output.txt`: `demo_payment_rows=0`; dirty read blocked; naive score 21 then locked path 22; `rejected issued rows=0`.
