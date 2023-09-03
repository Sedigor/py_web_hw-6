SELECT student_name, grade
FROM student_grades
JOIN students ON student_grades.student_id = students.student_id
WHERE subject_id = X AND group_id = Z;
