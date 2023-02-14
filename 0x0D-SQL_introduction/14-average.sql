-- computes the score average of all records in second_table
-- query to get average of score and save to column `average`
ALTER TABLE second_table ADD COLUMN average FLOAT;
UPDATE second_table SET average = (SELECT AVG(score) FROM second_table);
