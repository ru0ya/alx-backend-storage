-- sql script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    INSERT INTO average_weighted_scores (user_id, score)
    SELECT c.user_id, IFNULL(SUM(c.score * p.weight) / SUM(p.weight), 0)
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    GROUP BY c.user_id
    ON DUPLICATE KEY UPDATE score = VALUES(score);
END //

DELIMITER ;
