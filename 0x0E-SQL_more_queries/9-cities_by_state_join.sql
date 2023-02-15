-- lists all cities stored in database
-- query to list city by id, name and state name
SELECT id, name, states.name
FROM cities
NATURAL JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
