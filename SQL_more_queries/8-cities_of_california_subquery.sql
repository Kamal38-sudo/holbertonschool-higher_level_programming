-- salam
SELECT cities.id, cities.name, cities.state_id
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
