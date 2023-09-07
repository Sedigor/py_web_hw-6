SELECT student_name, grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = 2 AND grades.subject_id = 3;
