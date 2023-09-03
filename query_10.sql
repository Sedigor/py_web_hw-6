SELECT
    s.first_name AS student_first_name,
    s.last_name AS student_last_name,
    t.first_name AS teacher_first_name,
    t.last_name AS teacher_last_name,
    sb.subject_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sb ON g.subject_id = sb.subject_id
JOIN teachers t ON sb.teacher_id = t.teacher_id
WHERE s.student_id = <student_id> AND t.teacher_id = <teacher_id>;
