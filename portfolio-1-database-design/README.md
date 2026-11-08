# Portfolio 1 — Database Design and Modelling

**Case study:** USIRMS / Riverside University  
**DBMS:** MySQL / MariaDB (InnoDB) — [dbeaver-connection.md](dbeaver-connection.md)

## Write-ups and scripts

| Path | Content |
| --- | --- |
| [00-case-study.md](00-case-study.md) | Organisation statement |
| [02-erd.md](02-erd.md), [03-relational-schema.md](03-relational-schema.md) | ERD and logical schema |
| [04-keys-constraints-integrity.md](04-keys-constraints-integrity.md), [05-normalisation.md](05-normalisation.md) | Keys, CHECK/FK, 3NF/BCNF |
| [sql/schema.sql](sql/schema.sql), [sql/integrity_tests.sql](sql/integrity_tests.sql) | DDL and illegal rows that must fail |
| [scripts/build_database.py](scripts/build_database.py) | Create `usirms`, seed, run integrity tests |

## Recreate

```text
python portfolio-1-database-design/scripts/build_database.py --scale full
```

## Evidence (assessor)

| File | What it shows |
| --- | --- |
| [evidence/constraint_violations.txt](evidence/constraint_violations.txt) | 8/8 illegal operations rejected |
| [evidence/schema_created.txt](evidence/schema_created.txt), [evidence/seed_counts.txt](evidence/seed_counts.txt) | Objects and row counts |
| [evidence/ada_okonkwo_transcript.txt](evidence/ada_okonkwo_transcript.txt) | Worked transcript example |
| [evidence/erd.png](evidence/erd.png) | ERD screenshot (optional; Mermaid in `02-erd.md`) |

Known limits (design notes): declared cache column on `enrolment`; campus modelled for Portfolio 5 fragmentation — see `05-normalisation.md`.
