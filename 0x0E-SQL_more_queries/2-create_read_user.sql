-- script that creates a database and adds a user
-- query to create db `hbtn_0d_2` and add user `user_0d_2`
-- user `user_0d_2` should have only SELECT privileges in the db
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT on hbtn_0d_2.* TO 'user_0d_2'@'localhost';
