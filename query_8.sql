SELECT teacher_name, (ROUND(AVG(g.grade))) AS avg_grade
FROM teachers t
JOIN subjects sb ON t.id = sb.teacher_id
JOIN grades g ON sb.id = g.subject_id
GROUP BY t.teacher_name;
