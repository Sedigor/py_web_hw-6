SELECT group_name, AVG(grade) as avg_grade
FROM student_grades
JOIN students ON student_grades.student_id = students.student_id
WHERE subject_id = X
GROUP BY group_name;
