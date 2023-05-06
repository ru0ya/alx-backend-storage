-- creates a stored procedure that computes
-- and stores average score for a student

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE average_score FLOAT;
	SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = user.id;
	UPDATE users SET average_score = average_score WHERE user_id = user.id;
END
//
DELIMITER ;
