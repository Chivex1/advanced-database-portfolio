# Portfolio 5 — Distributed and Cloud Database Exercise

**Case study:** USIRMS — MAIN + NORTH campuses

## Write-ups and scripts

| Path | Content |
| --- | --- |
| [01-architecture.md](01-architecture.md) | Fragmentation, replication, CAP, cloud mapping |
| [scripts/run_distributed.py](scripts/run_distributed.py) | Live fragments + replica apply on MySQL/MariaDB |
| [config/docker-compose.yml](config/docker-compose.yml) | Cloud-style primary/replica **config** (not executed in this repo) |

## Recreate

```text
python portfolio-5-distributed-cloud/scripts/run_distributed.py
```

## Evidence (assessor)

| File | What it shows |
| --- | --- |
| [evidence/distributed_run.txt](evidence/distributed_run.txt) | MAIN 600 + NORTH 600 = 1200, overlap 0; replica 0 rows then 1 after apply |
| [config/docker-compose.yml](config/docker-compose.yml) | Intended RDS / read-replica topology (PostgreSQL sketch) |

Live Docker/RDS is not claimed. Limits are stated in `01-architecture.md`.
