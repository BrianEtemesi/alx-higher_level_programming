-- lists all tables of a database in my mysql server
-- the database will be passed as an argument of mysql command
-- query to list tables of a database
USE $1;
SHOW TABLES;
