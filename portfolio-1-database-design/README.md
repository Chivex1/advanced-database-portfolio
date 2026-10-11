# Portfolio 1 — Database Design and Modelling

**Case study:** University Student Information and Results Management System (USIRMS), Riverside University  
**Marks targeted:** 7/7  
**DBMS:** MySQL / MariaDB (InnoDB). Open in DBeaver: see [dbeaver-connection.md](dbeaver-connection.md).

## What this folder contains

| Artefact | Purpose |
| --- | --- |
| [00-case-study.md](00-case-study.md) | Locked organisation statement used in every later portfolio |
| [02-erd.md](02-erd.md) | Conceptual ERD and cardinalities |
| [03-relational-schema.md](03-relational-schema.md) | Logical schema, views, grade-point rule |
| [04-keys-constraints-integrity.md](04-keys-constraints-integrity.md) | Keys, CHECKs, FKs, business rules |
| [05-normalisation.md](05-normalisation.md) | UNF → 1NF → 2NF → 3NF / BCNF with justification |
| [sql/schema.sql](sql/schema.sql) | Executable DDL |
| [sql/seed_reference.sql](sql/seed_reference.sql) | Hand-written mini-seed (Ada Okonkwo worked example) |
| [sql/integrity_tests.sql](sql/integrity_tests.sql) | Illegal statements that must be rejected |
| [scripts/build_database.py](scripts/build_database.py) | Recreate database, seed, run integrity tests, write evidence |
| [evidence/](evidence/) | Object list, row counts, constraint rejections, sample transcript |

The generated database is the MySQL/MariaDB schema `usirms` (created by the build script; not hand-edited).

## How to recreate

From the repository root, with Python 3.10+:

```text
python portfolio-1-database-design/scripts/build_database.py
```

Larger population (used by Portfolio 2):

```text
python portfolio-1-database-design/scripts/build_database.py --scale full
```

The script:

1. Applies `sql/schema.sql` (drops and recreates all objects).
2. Inserts a deterministic seed (`random.Random(8103)`).
3. Runs every statement in `sql/integrity_tests.sql` and **requires** each to fail.
4. Writes evidence files under `evidence/`.

Minimal alternative without the generator (schema + worked example only), in DBeaver or the mysql client:

```text
CREATE DATABASE usirms CHARACTER SET utf8mb4;
USE usirms;
SOURCE portfolio-1-database-design/sql/schema.sql;
SOURCE portfolio-1-database-design/sql/seed_reference.sql;
```

## How to test

After a successful build, in DBeaver against `usirms`:

```sql
SELECT COUNT(*) FROM student;
SELECT s.matric_no, c.cgpa
FROM student s
JOIN v_student_cgpa c ON c.student_id = s.student_id
WHERE s.matric_no = 'RU/CSC/2024/001';
```

Expected integrity evidence (already captured):

- `evidence/constraint_violations.txt` — 8/8 illegal operations rejected
- `evidence/seed_counts.txt` — non-zero counts for every operational table
- `evidence/ada_okonkwo_transcript.txt` — worked example from the normalisation write-up

Re-run `sql/integrity_tests.sql` against a live connection with foreign keys on: every statement must error.

## Design decisions (short)

- One staff relation with a role domain, not six near-identical people tables.
- Module catalogue vs module offering so historical grades stay attached to the semester in which they were earned.
- Transcript *content* is a view; transcript *issuance* is an audit table.
- Campus is modelled now so Portfolio 5 can fragment by site without redesign.
- Target normal form is 3NF/BCNF, with a declared cache of approved module results on `enrolment`.

## Self-grade

**Portfolio 1: 7/7** — gaps: none remaining after the live rebuild. — fixes applied: unique enrolment targeting in the seeder; integrity runner now requires 8/8 rejections. — revised: **7/7**.

| Expected evidence (CA table) | Present | Path |
| --- | --- | --- |
| Case study description | Yes | `00-case-study.md` |
| ER diagram | Yes | `02-erd.md` |
| Relational schema | Yes | `03-relational-schema.md`, `sql/schema.sql` |
| Keys | Yes | `04-keys-constraints-integrity.md` |
| Constraints / integrity | Yes | `sql/integrity_tests.sql`, `evidence/constraint_violations.txt` (8/8 rejected) |
| Normalisation explanation | Yes | `05-normalisation.md` (UNF→3NF/BCNF, justified) |
| Recreate / test README | Yes | this file |

Cross-cutting criteria touched here: technical correctness (live DDL + rejected illegal rows), database design quality (3NF/BCNF, offering vs catalogue), practical implementation (`scripts/build_database.py`), documentation/GitHub organisation (folder + evidence).
