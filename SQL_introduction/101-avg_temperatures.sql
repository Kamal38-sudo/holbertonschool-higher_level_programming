-- Display the average temperature by city ordered descending
SELECT city, ROUND(AVG(temp), 4) AS avg_temp
FROM city_temperature_table
GROUP BY city
ORDER BY avg_temp DESC;
