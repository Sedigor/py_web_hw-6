SELECT
    s.student_name AS student_name,
    t.teacher_name AS teacher_name,
    sb.subject_name
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sb ON g.subject_id = sb.id
JOIN teachers t ON sb.teacher_id = t.id
WHERE s.id = 28 AND t.id = 1;
