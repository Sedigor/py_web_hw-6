SELECT
    t.teacher_name,
    s.subject_name
FROM teachers t
JOIN subjects s ON t.id = s.id;
