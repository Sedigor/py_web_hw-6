SELECT course_name
FROM courses
JOIN student_courses ON courses.course_id = student_courses.course_id
WHERE student_id = W
AND teacher_id = Y;
