-- script that creates a trigger that resets the attribute
-- valid_email only when email has changed
DROP TRIGGER IF EXISTS reset_email;

DELIMITER //
CREATE TRIGGER reset_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = NEW.valid_email;
	END IF;
END
//
DELIMITER ;
