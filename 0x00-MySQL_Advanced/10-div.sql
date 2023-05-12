-- script that creates a function 'SafeDiv' that divides
-- and returns first number by second number: if second
-- number is equal to 0 returns 0
DROP FUNCTION IF EXISTS SafeDiv;


CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS INT
BEGIN
	DECLARE result INT;

	IF b = 0 THEN
		SET result = 0;
	ELSE
		SET result = a / b;
	END IF;

	RETURN result;
END
