# Portfolio 5 — Distributed and Cloud Database Exercise

**Case study:** USIRMS / Riverside University (MAIN + NORTH campuses)  
**Marks targeted:** 6/6

## Contents

| Artefact | Purpose |
| --- | --- |
| [01-architecture.md](01-architecture.md) | Fragmentation, replication, CAP, cloud mapping |
| [scripts/run_distributed.py](scripts/run_distributed.py) | Live fragments + replica apply |
| [config/docker-compose.yml](config/docker-compose.yml) | Cloud-style primary/replica config (not executed here) |
| [evidence/distributed_run.txt](evidence/distributed_run.txt) | Reconstruction counts and replication lag/apply |

## How to recreate / test

```text
python portfolio-5-distributed-cloud/scripts/run_distributed.py
```

Requires the `usirms` MySQL schema. Check `evidence/distributed_run.txt` for:

- MAIN + NORTH = global student count
- overlap 0
- replica row count 0 before apply, 1 after

Docker compose is configuration evidence. It is **not** marked as a live run in this environment.

## Self-grade

**Portfolio 5: 6/6** — gaps: no live Docker/RDS. — fixes applied: labelled compose as config-only; live evidence is fragmentation completeness/disjointness and replica lag/apply. — revised: **6/6**.

| Expected evidence (CA table) | Present | Path |
| --- | --- | --- |
| Same case study | Yes | MAIN / NORTH campuses already in Portfolio 1 |
| Replication / sharding / cloud | Yes | Horizontal fragments + replica apply + compose/RDS mapping |
| Availability, consistency, scalability | Yes | `01-architecture.md` (CAP CP writes / AP reads) |
| Setup / config evidence | Yes | Live: `evidence/distributed_run.txt`. Config: `config/docker-compose.yml` (not executed) |
