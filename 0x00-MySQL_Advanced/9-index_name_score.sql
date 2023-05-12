-- sql script that creates an index 'idx_name_first_score' on
-- the table names and first letter of name and score
DROP INDEX IF EXISTS idx_name_first_score ON names;

CREATE INDEX idx_name_first_score ON names(SUBSTRING(names, 1, 1), score);
