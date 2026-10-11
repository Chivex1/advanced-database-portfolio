# Transactions on USIRMS

Grade entry, fee posting, and transcript issue are the operations that must not be left half-done. This portfolio maps the module’s **ACID** properties onto those operations and records live SQLite output.

## Why ACID applies here (and BASE does not)

The module contrasts ACID (RDBMS) with DBASE/BASE (distributed NoSQL). Official marks and fee balances are **integrity-critical**. A student cannot have a published exam score and a missing CA because the second insert failed. That is Atomicity. A published letter grade must match the 5-point rule. That is Consistency. Two lecturers must not each increment a remark and lose one increment. That is Isolation. After COMMIT, a power loss must not drop the mark. That is Durability.

BASE/eventual consistency is evaluated in Portfolios 4 and 5 for catalogue caches and campus replicas — not for the system of record.

| Property | USIRMS meaning | Demo |
| --- | --- | --- |
| Atomicity | Scores and the cached final mark commit together; a bad payment undoes the whole fee unit | 1, 2, 5 |
| Consistency | CHECK constraints + 5-point rule + invoice maths stay valid | 1, 2 |
| Isolation | Concurrent readers do not see uncommitted draft scores | 3 |
| Durability | Rows are present after COMMIT (WAL file + later checkpoint) | 1 |

## Isolation levels (module vs SQLite)

Textbook levels: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE.

SQLite’s lock manager is closer to **SERIALIZABLE** for writers: one writer at a time, plus WAL snapshots for readers. `BEGIN IMMEDIATE` takes the reserved/write lock at the start of the transaction so a second writer fails or waits instead of interleaving.

This portfolio therefore demonstrates:

1. **No dirty read** (Demo 3) — the property READ COMMITTED already guarantees, and SQLite’s snapshot satisfies.
2. **Lost update** under application-level read–modify–write (Demo 4) — still possible if two sessions write a previously read value.
3. **Lock + atomic increment** as the control mechanism (Demo 4).

A PostgreSQL `SET TRANSACTION ISOLATION LEVEL` script is *not* claimed as live evidence. SQLite is the DBMS that actually ran.

## Demonstrations

| Demo | What it shows | Why it matters in the university |
| --- | --- | --- |
| 1 COMMIT | Publish CA + exam and write `enrolment.final_mark` in one transaction | Transcript cache cannot drift from published scores |
| 2 ROLLBACK | Second payment fails CHECK (`amount_paid > 0`); first payment disappears | Bursary never posts a partial illegal batch |
| 3 Isolation | Connection B reads the committed CA while A holds an uncommitted draft of 3 | Advisors never see a half-typed mark |
| 4 Lost update / control | Two +1 remark adjustments; naive RMW loses one; `BEGIN IMMEDIATE` + `score = score + 1` keeps both | Concurrent remarking |
| 5 SAVEPOINT | Illegal `Issued` transcript rolls back; a legal `Requested` row commits | Registrar can abort one step without abandoning the session |

## How to run

```text
python portfolio-3-transactions-concurrency/scripts/run_transactions.py
```

Requires `data/usirms.db` from Portfolio 1 or 2. Output: `evidence/transaction_output.txt`.
