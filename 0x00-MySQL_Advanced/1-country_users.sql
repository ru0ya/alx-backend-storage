-- creates a table users
-- attribute country has multiple
-- enumerations and a default US
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country SET('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
	);

