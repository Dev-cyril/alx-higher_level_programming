-- a script that displays scores with more than 1 occurence

SELECT score, count(*) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;