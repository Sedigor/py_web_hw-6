SELECT
    st.group_id,
    g.subject_id,
    AVG(g.grade) AS average_grade
FROM students st
JOIN grades g ON st.student_id = g.student_id
WHERE g.subject_id = <subject_id>
GROUP BY st.group_id, g.subject_id;