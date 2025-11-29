-- salam
SELECT * FROM cities where state_id (SELECT * FROM states where name="California") ORDER BY id ASC;
