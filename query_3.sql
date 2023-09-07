SELECT group_id, subject_id, (ROUND(AVG(grade))) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 2
GROUP BY students.group_id, grades.subject_id;
