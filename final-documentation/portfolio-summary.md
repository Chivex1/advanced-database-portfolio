# MIT 8103 Advanced Database Systems — Portfolio summary

**Student:** Nwafor Chigor Nichodemus  
**Matriculation number:** 2026/A/MIT/0587  
**Course:** MIT 8103 Advanced Database Systems  
**Assessment:** Individual Practical Database Portfolio (40 marks)  
**GitHub repository:** `https://github.com/Chivex1/advanced-database-portfolio`  
*(Grant the assessor access before LMS submission.)*

## Selected organisation

**Riverside University** operates the **University Student Information and Results Management System (USIRMS)**.

- **Nature of the system:** OLTP student-records and results platform for a two-campus tertiary institution (MAIN / Lagos, NORTH / Kaduna).
- **Users:** students, lecturers, academic advisors, heads of department, registrar staff, and administrators.
- **Major data:** students, departments, programmes, modules, lecturers, enrolments, assessments, grades, timetables, attendance, fees, transcripts.
- **Key operations:** registration, grade entry, GPA/CGPA, transcript issue, timetable tracking, record updates, and reporting.

The same organisation is used in every portfolio folder.

## Portfolio activities

### Portfolio 1 — Database design and modelling (7)

Conceptual ERD, relational schema, keys/constraints, and normalisation to 3NF/BCNF with a declared cache of approved module results. SQLite DDL in `portfolio-1-database-design/sql/schema.sql` was executed; eight illegal statements were rejected (duplicate matric number, orphan grade, negative score, double enrolment, self-prerequisite, incomplete issued transcript, academic staff without a department, duplicate payment reference). Evidence: `portfolio-1-database-design/evidence/`.

### Portfolio 2 — Query processing and optimisation (7)

Eight registrar/HoD/advisor/bursary queries (transcript, CGPA rank, failure rates, outstanding fees, lecturer load, attendance, census, nested vs rewritten “failed CSC module”). `EXPLAIN QUERY PLAN` was captured before and after secondary indexes. Measured means (15 runs) show Q5 falling from 8.820 ms to 0.525 ms and Q8b from 4.894 ms to 0.178 ms. Q8a and Q8b returned the same six students. Some queries did not improve; that is reported rather than invented. Evidence: `portfolio-2-query-optimisation/evidence/`.

### Portfolio 3 — Transactions and concurrency (7)

Five live demonstrations on two WAL connections: atomic finalisation of Ada Okonkwo’s CSC102 (74 A) on COMMIT; fee batch ROLLBACK (`demo_payment_rows=0`); no dirty read (connection B still saw 26 while A held an uncommitted 3); lost update (naive 21 vs intended 22) corrected by `BEGIN IMMEDIATE` and `score = score + 1` (result 22); SAVEPOINT keeping a legal transcript request and discarding an illegal issued row. Evidence: `portfolio-3-transactions-concurrency/evidence/transaction_output.txt`.

### Portfolio 4 — NoSQL and advanced data models (7)

Primary alternative: **document** student aggregates. Also implemented: **key-value** timetable/fee cache and a **prerequisite graph**. Ada’s document yields CGPA 4.64 from nested enrolments without SQL. Graph BFS finds `CSC101 → CSC202 → MIT8103`. Column-family is discussed and rejected as the primary store. Relational ACID remains the write path; documents are an eventually consistent read model (BASE/DBASE). Evidence: `portfolio-4-nosql/evidence/`.

### Portfolio 5 — Distributed and cloud exercise (6)

Horizontal fragments by campus reconstruct the global 1,200 students (600 + 600, overlap 0). A file replica is stale (0 matching rows) until apply (1 row). Writes are treated as CP; campus reads as AP. `config/docker-compose.yml` is the cloud-style primary/replica description (Amazon RDS / Cloud SQL class). Docker was **not** claimed as a live run. Evidence: `portfolio-5-distributed-cloud/evidence/distributed_run.txt`.

## Evidence index (LMS)

Screenshots are not a substitute for the runnable scripts. Attach or point the assessor to:

1. `portfolio-1-database-design/evidence/constraint_violations.txt`
2. `portfolio-2-query-optimisation/evidence/timings.txt` and `plans_after/Q5_lecturer_load.txt`
3. `portfolio-3-transactions-concurrency/evidence/transaction_output.txt`
4. `portfolio-4-nosql/evidence/document_ada.json` and `nosql_queries.txt`
5. `portfolio-5-distributed-cloud/evidence/distributed_run.txt`

Recreate everything from the repository root with Python 3.10+ by running each folder’s `scripts/` entry point (see each README).

## Individual technical reflection

I treated USIRMS as an integrity-first OLTP system and only then added read models. The design choice that mattered most was separating the **module catalogue** from the **module offering**. Historical grades stay attached to the semester in which they were earned; that decision simplified transcripts, concurrency demos, and campus fragments.

Normalisation was not an abstract exercise. The unnormalised results sheet from the notes produces update anomalies; after 3NF those anomalies become constraint violations that SQLite actually rejected. I then *reintroduced* a small, declared denormalisation (`enrolment.final_mark`) so an issued transcript cannot drift when someone later edits a draft CA. Portfolio 3 is the procedure that is allowed to write that cache.

Query optimisation taught a different lesson from “add indexes and everything gets faster.” On a RAM-resident SQLite file, Q2’s global CGPA view stayed a full enrolment scan even after indexes; Q2b’s plan became a clean `SEARCH` from `department_code` but was not cheaper in milliseconds. Q5 *was* cheaper because persistent covering indexes replaced per-query automatic indexes. I kept the mixed timings. Inventing a uniform speed-up would have contradicted the evidence.

Concurrency work showed that “SERIALIZABLE-ish file locks” still allow a lost update if two lecturers do read–modify–write in application code. The fix was not a lecture on isolation levels; it was `BEGIN IMMEDIATE` plus an atomic `UPDATE score = score + 1`. Isolation Demo 3 (no dirty read) and Demo 4 (lost update) are easy to confuse; running both on two connections made the difference concrete.

The NoSQL and distributed pieces were tempting places to over-claim. I implemented documents, key-value, and a graph because those match transcript reads, portal gets, and prerequisite paths. I did not stand up MongoDB Atlas or a live RDS replica. Docker compose is labelled as configuration. The live distributed evidence is reconstruction correctness and a visible replica lag. That matches the module (fragmentation, replication, CAP, DBASE) without inventing a cloud bill.

Challenges: the first seeder inserted duplicate enrolments; Portfolio 4’s timetable query omitted the `module` join; Ada’s timetable key is empty after Portfolio 3 completed CSC102. Each failure was fixed and re-run. The remaining limit is scale — 1,200 students show plan shape, not warehouse-scale I/O.

Lessons: (1) write the integrity rule in the schema, then prove it fails; (2) measure plans and times, and keep the times that do not flatter the story; (3) use NoSQL and replicas as *complements* to ACID, not as replacements for the registrar’s system of record.

## References

MIVA Open University. (2025). *MIT 8103 Advanced Database Systems* (study sessions 1–6: relational design and normalisation; distributed databases; CAP, ACID and DBASE; big data and cloud databases; query optimisation and file organisation; graph and emerging models).

Elmasri, R., & Navathe, S. B. (2016). *Fundamentals of database systems* (7th ed.). Pearson. (Normal forms, ER mapping, transaction properties.)

Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). *Database system concepts* (7th ed.). McGraw-Hill. (Query processing, indexing, concurrency control.)

SQLite Consortium. (n.d.). *EXPLAIN QUERY PLAN* and *Isolation in SQLite*. https://www.sqlite.org/eqp.html and https://www.sqlite.org/isolation.html

Brewer, E. (2012). CAP twelve years later: How the “rules” have changed. *IEEE Computer, 45*(2), 23–29. (CAP trade-offs used in Portfolio 5.)

## AI use declaration

1. **Tool used:** Cursor (agent assistant, Grok 4.6) as a development and drafting aid.
2. **Purpose:** Draft folder structure, SQL DDL, seed/query/transaction/NoSQL/distribution scripts, and explanatory write-ups aligned to the CA brief and module notes.
3. **How the output was reviewed, corrected, tested, or verified:**
   - Every executable artefact was run locally on Python 3.12 / SQLite 3.49.1.
   - The seeder was corrected when `UNIQUE (student_id, offering_id)` failed.
   - Portfolio 2 timings and plans are engine output (`time.perf_counter`, `EXPLAIN QUERY PLAN`), not invented figures.
   - Portfolio 3 two-connection demos were re-run after wording clean-up; pass conditions (rollback row count 0, dirty-read blocked, lost update 21 then 22) were checked in the evidence file.
   - Portfolio 4 was corrected after a missing `module` join; Ada’s document and the CSC101–MIT8103 path were inspected.
   - Portfolio 5 reconstruction (600+600=1200, overlap 0) and replica apply (0 then 1) were checked in `distributed_run.txt`.
   - Technical claims were limited to what the scripts actually produced. Docker compose is documented as config, not as a live deployment.

Use of the tool does not replace responsibility for the accuracy and understanding of this submission. I can explain any script, plan, or constraint if selected for verification.
