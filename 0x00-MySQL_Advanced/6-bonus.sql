-- script that creates a stored procedure
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN projects_name VARCHAR, IN score INT)
BEGIN
	UPDATE users
	SET OLD.score = NEW.score
	WHERE users = users.id

