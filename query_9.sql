SELECT
    s.first_name,
    s.last_name,
    sb.subject_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sb ON g.subject_id = sb.subject_id
WHERE s.student_id = <student_id>;
