---lists the number of records with the same score
SELECT 'score', COUNT(*) AS 'number'
FROM 'second_table'
WHERE 'score' IS SAME
ORDER BY DESC
