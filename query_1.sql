SELECT student_name, AVG(grade) as avg_grade
FROM student_grades
GROUP BY student_name
ORDER BY avg_grade DESC
LIMIT 5;