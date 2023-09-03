SELECT student_name, AVG(grade) as avg_grade
FROM student_grades
WHERE subject_id = X
GROUP BY student_name
ORDER BY avg_grade DESC
LIMIT 1;
