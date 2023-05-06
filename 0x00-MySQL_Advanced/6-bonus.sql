-- script that creates a stored procedure
DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN projects_name VARCHAR(255), IN score INT)
BEGIN
	UPDATE users
	SET score = score
	WHERE users_id = users.id AND project_name = projects.name;
END
//
DELIMITER ;

