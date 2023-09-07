SELECT student_name, subject_name
FROM grades g
JOIN students st ON g.student_id = st.id
JOIN subjects sb ON g.subject_id = sb.id
WHERE g.id = 28;
