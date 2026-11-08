# MIT 8103 Advanced Database Systems - Portfolio summary

**Student:** Nwafor Chigor Nichodemus  
**Matriculation number:** 2026/A/MIT/0587  
**Course:** MIT 8103 Advanced Database Systems  
**Assessment:** Individual Practical Database Portfolio (40 marks)  
**GitHub repository:** https://github.com/Chivex1/advanced-database-portfolio  

## Selected organisation

Riverside University operates the University Student Information and Results Management System (USIRMS).

- **Nature of the system:** OLTP student-records and results platform for a two-campus tertiary institution (MAIN / Lagos, NORTH / Kaduna).
- **Users:** students, lecturers, academic advisors, heads of department, registrar staff, and administrators.
- **Major data:** students, departments, programmes, modules, lecturers, enrolments, assessments, grades, timetables, attendance, fees, transcripts.
- **Key operations:** registration, grade entry, GPA/CGPA, transcript issue, timetable tracking, record updates, and reporting.

The same organisation is used in every portfolio folder.

## Portfolio activities

### Portfolio 1 - Database design and modelling (7)

Conceptual ERD, relational schema, keys/constraints, and normalisation to 3NF/BCNF with a declared cache of approved module results. MySQL/MariaDB DDL in portfolio-1-database-design/sql/schema.sql was executed; eight illegal statements were rejected (duplicate matric number, orphan grade, negative score, double enrolment, self-prerequisite, incomplete issued transcript, academic staff without a department, duplicate payment reference). Evidence: portfolio-1-database-design/evidence/.

### Portfolio 2 - Query processing and optimisation (7)

Eight registrar/HoD/advisor/bursary queries (transcript, CGPA rank, failure rates, outstanding fees, lecturer load, attendance, census, nested vs rewritten "failed CSC module"). EXPLAIN was captured before and after secondary indexes. Measured means (15 runs) are in evidence/timings.txt (for example Q8b improves sharply; Q2b and Q4 do not always win). Q8a and Q8b returned the same six students. Evidence: portfolio-2-query-optimisation/evidence/.

### Portfolio 3 - Transactions and concurrency (7)

Five live demonstrations on two InnoDB connections (default REPEATABLE READ): atomic finalisation of Ada Okonkwo's CSC102 (74 A) on COMMIT; fee batch ROLLBACK (demo_payment_rows=0); no dirty read (connection B still saw 26 while A held an uncommitted 3); lost update (naive 21 vs intended 22) corrected by row lock and UPDATE score = score + 1 (result 22); SAVEPOINT keeping a legal transcript request and discarding an illegal issued row. Evidence: portfolio-3-transactions-concurrency/evidence/transaction_output.txt.

### Portfolio 4 - NoSQL and advanced data models (7)

Primary alternative: document student aggregates. Also implemented: key-value timetable/fee cache and a prerequisite graph. Ada's document yields CGPA 4.64 from nested enrolments without SQL. Graph BFS finds CSC101 -> CSC202 -> MIT8103. Column-family is discussed and rejected as the primary store. Relational ACID remains the write path; documents are an eventually consistent read model (BASE/DBASE). Evidence: portfolio-4-nosql/evidence/.

### Portfolio 5 - Distributed and cloud exercise (6)

Horizontal fragments by campus reconstruct the global 1,200 students (600 + 600, overlap 0). A file replica is stale (0 matching rows) until apply (1 row). Writes are treated as CP; campus reads as AP. config/docker-compose.yml is the cloud-style primary/replica description (Amazon RDS / Cloud SQL class). Docker was not claimed as a live run. Evidence: portfolio-5-distributed-cloud/evidence/distributed_run.txt.

## Evidence index (LMS)

Screenshots are not a substitute for the runnable scripts. Attach or point the assessor to:

1. portfolio-1-database-design/evidence/constraint_violations.txt
2. portfolio-2-query-optimisation/evidence/timings.txt and plans_after/Q5_lecturer_load.txt
3. portfolio-3-transactions-concurrency/evidence/transaction_output.txt
4. portfolio-4-nosql/evidence/document_ada.json and nosql_queries.txt
5. portfolio-5-distributed-cloud/evidence/distributed_run.txt

Recreate everything from the repository root with Python 3.10+ by running each folder's scripts/ entry point (see each README).

## Repository layout

```text
advanced-database-portfolio/
├── README.md
├── requirements.txt
├── shared/mysql_db.py                 MySQL connection helper
├── portfolio-1-database-design/       ERD, schema, integrity evidence
├── portfolio-2-query-optimisation/    Queries, plans, timings
├── portfolio-3-transactions-concurrency/
├── portfolio-4-nosql/
├── portfolio-5-distributed-cloud/
└── final-documentation/               LMS summary (portfolio-summary.md)
```

## Individual technical reflection

I treated USIRMS as an integrity-first OLTP system and only then added read models. The design choice that mattered most was separating the module catalogue from the module offering. Historical grades stay attached to the semester in which they were earned; that decision simplified transcripts, concurrency demos, and campus fragments.

Normalisation was not an abstract exercise. The unnormalised results sheet from the notes produces update anomalies; after 3NF those anomalies become constraint violations that InnoDB actually rejected. I then reintroduced a small, declared denormalisation (enrolment.final_mark) so an issued transcript cannot drift when someone later edits a draft CA. Portfolio 3 is the procedure that is allowed to write that cache.

Query optimisation taught a different lesson from "add indexes and everything gets faster." On this MariaDB instance, Q2's view-based plan can still scan heavily; Q2b's selection pushdown changes the plan without always winning on time. Q5 and Q8b did benefit from persistent indexes. I kept the mixed timings in timings.txt rather than smoothing them.

Concurrency work showed that a naive read-modify-write in application code can still lose an increment under READ COMMITTED. The fix was row-level locking plus an atomic UPDATE score = score + 1. Isolation Demo 3 (no dirty read) and Demo 4 (lost update) are easy to confuse; running both on two connections made the difference concrete.

The NoSQL and distributed pieces were tempting places to over-claim. I implemented documents, key-value, and a graph because those match transcript reads, portal gets, and prerequisite paths. I did not stand up MongoDB Atlas or a live RDS replica. Docker compose is labelled as configuration. The live distributed evidence is reconstruction correctness and a visible replica lag. That matches the module (fragmentation, replication, CAP, DBASE) without inventing a cloud bill.

Challenges: the first seeder inserted duplicate enrolments; Portfolio 4's timetable query omitted the module join; Ada's timetable key is empty after Portfolio 3 completed CSC102. Each failure was fixed and re-run. The remaining limit is scale - 1,200 students show plan shape, not warehouse-scale I/O.

Lessons: (1) write the integrity rule in the schema, then prove it fails; (2) measure plans and times, and keep the times that do not flatter the story; (3) use NoSQL and replicas as complements to ACID, not as replacements for the registrar's system of record.

## References

MIVA Open University. (2025). MIT 8103 Advanced Database Systems (study sessions 1-6: relational design and normalisation; distributed databases; CAP, ACID and DBASE; big data and cloud databases; query optimisation and file organisation; graph and emerging models).

Elmasri, R., & Navathe, S. B. (2016). Fundamentals of database systems (7th ed.). Pearson. (Normal forms, ER mapping, transaction properties.)

Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). Database system concepts (7th ed.). McGraw-Hill. (Query processing, indexing, concurrency control.)

Oracle. (n.d.). MySQL 8.4 Reference Manual - EXPLAIN and InnoDB transaction isolation. https://dev.mysql.com/doc/refman/8.4/en/

MariaDB Foundation. (n.d.). MariaDB Knowledge Base - isolation levels and InnoDB. https://mariadb.com/kb/

Brewer, E. (2012). CAP twelve years later: How the "rules" have changed. IEEE Computer, 45(2), 23-29. (CAP trade-offs used in Portfolio 5.)
