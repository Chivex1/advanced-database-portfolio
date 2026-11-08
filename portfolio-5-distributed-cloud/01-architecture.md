# Distributed and cloud architecture for USIRMS

Riverside University has two campuses (`MAIN` in Lagos, `NORTH` in Kaduna). The module’s distributed-database toolkit is applied to that fact: fragmentation, replication, allocation, transparency, CAP, and cloud DBaaS.

## Architecture chosen

**Homogeneous distributed database** (same schema at each site) with:

1. **Horizontal fragmentation** of `student` (and, in production, `enrolment` / `attendance`) by `campus_code`.
2. **Primary-copy replication** of the registrar database to a reporting replica.
3. **Cloud target**: managed relational primary (Amazon RDS / Cloud SQL class of service from the module) plus a same-region read replica. Config sketch: `config/docker-compose.yml`.

This is still one case study. It is not a federated mash-up of unrelated vendor systems. A federated design would only appear if Riverside later queried an external JAMB or NYSC database without copying it — that is discussed, not built.

## Fragmentation

| Type | Applied to USIRMS | Predicate / projection |
| --- | --- | --- |
| Horizontal | `student` | `campus_code = 'MAIN'` vs `'NORTH'` |
| Vertical (design only) | `student` | Public (`matric_no`, name, programme) vs restricted (`date_of_birth`, email) for NDPR/GDPR-style least privilege |
| Hybrid | Enrolments | Horizontal by campus, vertical if a site should not store fee columns |

Correctness conditions checked live in `scripts/run_distributed.py`:

- Completeness: `|MAIN| + |NORTH| = |student|`
- Disjointness: overlap = 0
- Reconstruction: `UNION` of fragments = global count

Allocation: a student’s home campus stores their fragment (locality). Cross-campus MIT students stay on MAIN because Computing is allocated there.

## Replication and consistency models

| Copy | Role | Consistency |
| --- | --- | --- |
| Primary schema `usirms` / future managed RDS | All grade and fee writes | Strong / ACID |
| Schema `usirms_replica` | Advisor and portal reads | Stale until apply (eventual / DBASE) |
| Document export (Portfolio 4) | Portal cache | Eventual by design |

The live script inserts a transcript request on `usirms`, shows `usirms_replica` **missing** the row, then applies it into the replica schema. That gap is the module’s **soft state** and **eventual consistency** window.

During a network partition the university’s policy is:

- **Writes (grades, fees):** fail closed. Better to refuse an exam upload than to fork two primaries (CP).
- **Reads (timetable, handbook):** fail open on the local replica (AP).

That is the CAP theorem applied, not a claim that one system guarantees C, A, and P.

## Transparency (what users should not see)

| Transparency | How far this portfolio goes |
| --- | --- |
| Location | `route_query(matric)` hides the campus file name from the caller |
| Replication | After apply, the replica matches the primary; the student does not choose a copy |
| Fragmentation | Reconstruction query is the global view |
| Transaction | Full 2PC across campuses is **not** implemented. Cross-campus registration would need it; the scripts stay honest about that limit |

## Cloud deployment (practical vs claimed)

| Artefact | Status |
| --- | --- |
| `config/docker-compose.yml` | Written. Primary + replica service definitions (PostgreSQL `wal_level=replica` sketch) |
| Live `docker compose up` | **Not claimed.** Docker was not used as a running control plane in this environment |
| Live fragmentation + replica apply | **Claimed.** `evidence/distributed_run.txt` |

A production cloud mapping consistent with Session 3:

- Amazon RDS PostgreSQL Multi-AZ for the registrar primary (availability + automated backup)
- One read replica for HoD dashboards (Q2, Q3, Q5, Q7)
- Object store / document layer (Portfolio 4) on a regional bucket for portal JSON
- IAM + TLS for the CIA triad (confidentiality of results)

Pay-as-you-go and elastic storage matter at registration peaks (module: cloud DBaaS). They do not change the CP write rule.

## Scalability

- Vertical: larger primary for peak grade-upload week.
- Horizontal: more campus fragments; more read replicas.
- NewSQL (Spanner / CockroachDB in the notes) would keep SQL + ACID while sharding. It is a possible future, not a live deploy here.

## What is not invented

No fake multi-region latency figures. No claim that Docker was running. Network cost is discussed as a cost factor (Portfolio 2 / Session 4) and appears here as “apply lag”, not as a millisecond table.
