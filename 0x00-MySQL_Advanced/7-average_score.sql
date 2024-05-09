-- computes and store the avg score of student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id_param INT)
BEGIN
    -- Calculate average score for the user and update the users table
    UPDATE users
    SET average_score = (
        SELECT AVG(score)
        FROM corrections
        WHERE user_id = user_id_param
    )
    WHERE id = user_id_param;
END//

DELIMITER ;

