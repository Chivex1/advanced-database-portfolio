# Portfolio 3 — Transactions and Concurrency

**Case study:** USIRMS / Riverside University  
**Marks targeted:** 7/7  
**DBMS:** MySQL / MariaDB InnoDB, two connections, REPEATABLE READ

## Contents

| Artefact | Purpose |
| --- | --- |
| [01-acid-and-demos.md](01-acid-and-demos.md) | ACID mapping, isolation notes, demo list |
| [scripts/run_transactions.py](scripts/run_transactions.py) | Commit, rollback, dirty-read, lost-update, savepoint |
| [evidence/transaction_output.txt](evidence/transaction_output.txt) | Live engine output |

## How to recreate / test

```text
python portfolio-3-transactions-concurrency/scripts/run_transactions.py
```

The script opens two connections on the `usirms` schema. It does not rebuild the database. Re-run Portfolio 2 first if you need a clean full-scale copy.

What “pass” looks like in the evidence file:

- Demo 1: Ada’s CSC102 status becomes `Completed` with a final mark.
- Demo 2: `demo_payment_rows=0` after ROLLBACK.
- Demo 3: connection B still sees the committed score while A holds `score=3`.
- Demo 4: naive result `21`; controlled result `22`.
- Demo 5: requested transcript kept; illegal issued row count `0`.

## Self-grade

**Portfolio 3: 7/7** — gaps: none after the live two-connection run. — fixes applied: n/a (demos matched the planned checks). — revised: **7/7**.

| Expected evidence (CA table) | Present | Path |
| --- | --- | --- |
| Commit example | Yes | Demo 1: CSC102 finalised 74 A |
| Rollback example | Yes | Demo 2: `demo_payment_rows=0` |
| Isolation | Yes | Demo 3: B reads 26 while A holds uncommitted 3 |
| Concurrency issue | Yes | Demo 4: naive RMW stores 21 instead of 22 |
| Control mechanism | Yes | Demo 4: `BEGIN IMMEDIATE` + atomic increment → 22; Demo 5 SAVEPOINT |
| Screenshots / output | Yes | `evidence/transaction_output.txt` |
| README explanation | Yes | this file + `01-acid-and-demos.md` |
