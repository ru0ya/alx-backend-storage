-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores average weighted score for a student

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT IFNULL(SUM(corrections.score * projects.weight) / SUM(projects.weight), 0)
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id
    )
    WHERE id = user_id;
END //

DELIMITER ;
