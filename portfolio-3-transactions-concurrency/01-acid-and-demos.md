# Transactions on USIRMS

Grade entry, fee posting, and transcript issue are the operations that must not be left half-done. This portfolio maps **ACID** onto those operations and records live **MySQL/MariaDB InnoDB** output.

## Why ACID applies here (and BASE does not)

Official marks and fee balances are **integrity-critical**. BASE/eventual consistency is evaluated in Portfolios 4 and 5 for caches and replicas — not for the system of record.

| Property | USIRMS meaning | Demo |
| --- | --- | --- |
| Atomicity | Scores and the cached final mark commit together; a bad payment undoes the whole fee unit | 1, 2, 5 |
| Consistency | CHECK constraints + 5-point rule + invoice maths stay valid | 1, 2 |
| Isolation | Concurrent readers do not see uncommitted draft scores | 3 |
| Durability | Rows are visible after COMMIT (InnoDB redo log) | 1 |

## Isolation (module vs InnoDB)

Default session isolation is **REPEATABLE READ**: readers see the last committed snapshot (Demo 3 — no dirty read).

Demo 4 uses **READ COMMITTED** for the naive read–modify–write so a stale write can commit (score 21). The control path uses `SELECT … FOR UPDATE` and `UPDATE score = score + 1` to reach 22.

Manual SQL steps: `sql/*.sql` and [sql/README.md](sql/README.md). Automated run:

```text
python portfolio-3-transactions-concurrency/scripts/run_transactions.py
```

Requires schema `usirms` from Portfolio 1/2. Output: `evidence/transaction_output.txt`.

## Demonstrations

| Demo | What it shows |
| --- | --- |
| 1 COMMIT | Publish CSC102 scores and `enrolment.final_mark` together |
| 2 ROLLBACK | Illegal payment CHECK fails; demo payment rows gone after rollback |
| 3 Isolation | B reads committed 26 while A holds uncommitted draft 3 |
| 4 Lost update / control | Naive 21; locked atomic increments → 22 |
| 5 SAVEPOINT | Legal transcript request kept; illegal issued row rolled back |
