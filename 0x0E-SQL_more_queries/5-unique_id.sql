-- script creates a table
-- query to create table `unique_id` with id and name fields
-- id to have a default value of 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id (
id INT NOT NULL DEFAULT 1 UNIQUE,
name VARCHAR(256));
