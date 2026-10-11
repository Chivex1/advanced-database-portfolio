-- USIRMS reporting queries used by scripts/run_optimisation.py
-- Each query is a real registrar / HoD / advisor operation from the case study.

-- Q1. Official transcript lines for Ada Okonkwo (student self-service / registrar)
-- Relational algebra sketch:
--   π session, semester, code, title, cu, mark, grade
--   (σ matric_no = 'RU/CSC/2024/001' (student ⋈ enrolment ⋈ offering ⋈ module ⋈ semester ⋈ session))
SELECT
    t.session_label,
    t.semester_no,
    t.module_code,
    t.module_title,
    t.credit_units,
    t.final_mark,
    t.letter_grade,
    t.grade_point,
    t.enrolment_status
FROM v_transcript_line t
WHERE t.matric_no = 'RU/CSC/2024/001'
ORDER BY t.session_label, t.semester_no, t.module_code;

-- Q2. Advisor / HoD: active students with CGPA, ranked in Computer Science
SELECT
    s.matric_no,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    s.current_level,
    c.cgpa,
    c.credit_units_completed
FROM student s
JOIN programme p ON p.programme_id = s.programme_id
JOIN department d ON d.department_id = p.department_id
JOIN v_student_cgpa c ON c.student_id = s.student_id
WHERE d.department_code = 'CSC'
  AND s.status = 'Active'
ORDER BY c.cgpa DESC, s.matric_no
LIMIT 15;

-- Q2b. Same ranking with selection pushed down (do not pre-aggregate every student)
SELECT
    s.matric_no,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    s.current_level,
    ROUND(SUM(e.grade_point * m.credit_units) * 1.0 / SUM(m.credit_units), 2) AS cgpa,
    SUM(m.credit_units) AS credit_units_completed
FROM student s
JOIN programme p ON p.programme_id = s.programme_id
JOIN department d ON d.department_id = p.department_id
JOIN enrolment e ON e.student_id = s.student_id
JOIN module_offering o ON o.offering_id = e.offering_id
JOIN module m ON m.module_id = o.module_id
WHERE d.department_code = 'CSC'
  AND s.status = 'Active'
  AND e.status = 'Completed'
  AND e.grade_point IS NOT NULL
GROUP BY s.student_id, s.matric_no, s.first_name, s.last_name, s.current_level
ORDER BY cgpa DESC, s.matric_no
LIMIT 15;

-- Q3. Registrar: modules with a high failure rate (letter F) in closed enrolments
SELECT
    m.module_code,
    m.module_title,
    COUNT(*) AS completed_enrolments,
    SUM(CASE WHEN e.letter_grade = 'F' THEN 1 ELSE 0 END) AS fails,
    ROUND(100.0 * SUM(CASE WHEN e.letter_grade = 'F' THEN 1 ELSE 0 END) / COUNT(*), 1) AS fail_rate_pct
FROM enrolment e
JOIN module_offering o ON o.offering_id = e.offering_id
JOIN module m ON m.module_id = o.module_id
WHERE e.status = 'Completed'
GROUP BY m.module_id, m.module_code, m.module_title
HAVING COUNT(*) >= 5
ORDER BY fail_rate_pct DESC, completed_enrolments DESC;

-- Q4. Bursary: outstanding fee balances for the current session
SELECT
    s.matric_no,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    sess.session_label,
    b.amount_due,
    b.amount_paid,
    b.balance,
    b.status
FROM v_invoice_balance b
JOIN student s ON s.student_id = b.student_id
JOIN academic_session sess ON sess.session_id = b.session_id
WHERE sess.is_current = 1
  AND b.balance > 0
ORDER BY b.balance DESC, s.matric_no
LIMIT 20;

-- Q5. HoD: lecturer teaching load in the open semester
SELECT
    st.staff_number,
    CONCAT(st.first_name, ' ', st.last_name) AS lecturer,
    d.department_name,
    COUNT(o.offering_id) AS offerings,
    COUNT(e.enrolment_id) AS enrolled_students
FROM staff st
JOIN department d ON d.department_id = st.department_id
JOIN module_offering o ON o.lecturer_staff_id = st.staff_id
JOIN semester sem ON sem.semester_id = o.semester_id
LEFT JOIN enrolment e ON e.offering_id = o.offering_id AND e.status <> 'Dropped'
WHERE sem.status = 'Open'
  AND st.role IN ('Lecturer', 'Advisor', 'HoD')
GROUP BY st.staff_id, st.staff_number, st.first_name, st.last_name, d.department_name
ORDER BY offerings DESC, enrolled_students DESC;

-- Q6. Advisor: current-semester attendance rate below 75%
SELECT
    s.matric_no,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    m.module_code,
    COUNT(*) AS meetings,
    SUM(CASE WHEN a.status IN ('Present', 'Late') THEN 1 ELSE 0 END) AS attended,
    ROUND(
        100.0 * SUM(CASE WHEN a.status IN ('Present', 'Late') THEN 1 ELSE 0 END) / COUNT(*),
        1
    ) AS attendance_pct
FROM attendance a
JOIN timetable_slot ts ON ts.slot_id = a.slot_id
JOIN module_offering o ON o.offering_id = ts.offering_id
JOIN module m ON m.module_id = o.module_id
JOIN student s ON s.student_id = a.student_id
GROUP BY s.student_id, s.matric_no, s.first_name, s.last_name, m.module_id, m.module_code
HAVING attendance_pct < 75
ORDER BY attendance_pct, s.matric_no;

-- Q7. Registrar census: enrolment by programme and semester
SELECT
    p.programme_code,
    sess.session_label,
    sem.semester_no,
    COUNT(e.enrolment_id) AS enrolments,
    COUNT(DISTINCT e.student_id) AS distinct_students
FROM enrolment e
JOIN student s ON s.student_id = e.student_id
JOIN programme p ON p.programme_id = s.programme_id
JOIN module_offering o ON o.offering_id = e.offering_id
JOIN semester sem ON sem.semester_id = o.semester_id
JOIN academic_session sess ON sess.session_id = sem.session_id
WHERE e.status <> 'Dropped'
GROUP BY p.programme_id, p.programme_code, sess.session_label, sem.semester_no
ORDER BY sess.session_label, sem.semester_no, p.programme_code;

-- Q8a. Correlated subquery form (same result as Q8b; typically worse plan)
-- Module example: employees in NY departments rewritten from nested IN to join.
SELECT s.matric_no, s.first_name, s.last_name
FROM student s
WHERE s.status = 'Active'
  AND s.student_id IN (
        SELECT e.student_id
        FROM enrolment e
        WHERE e.status = 'Completed'
          AND e.letter_grade = 'F'
          AND e.offering_id IN (
                SELECT o.offering_id
                FROM module_offering o
                JOIN module m ON m.module_id = o.module_id
                WHERE m.department_id = (
                    SELECT department_id FROM department WHERE department_code = 'CSC'
                )
          )
  )
ORDER BY s.matric_no
LIMIT 20;

-- Q8b. Rewritten as joins (selection/join rewrite from the module)
SELECT DISTINCT s.matric_no, s.first_name, s.last_name
FROM student s
JOIN enrolment e ON e.student_id = s.student_id
JOIN module_offering o ON o.offering_id = e.offering_id
JOIN module m ON m.module_id = o.module_id
JOIN department d ON d.department_id = m.department_id
WHERE s.status = 'Active'
  AND e.status = 'Completed'
  AND e.letter_grade = 'F'
  AND d.department_code = 'CSC'
ORDER BY s.matric_no
LIMIT 20;
