SELECT student_name, (ROUND(AVG(grade))) as avg_grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE subject_id = 4
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 1;

