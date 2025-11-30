-- Display the average temperature by city ordered descending
SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
