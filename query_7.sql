SELECT
    s.first_name,
    s.last_name,
    g.grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE s.group_id = <group_id> AND g.subject_id = <subject_id>;
