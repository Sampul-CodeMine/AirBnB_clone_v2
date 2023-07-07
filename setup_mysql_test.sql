-- CREATES A DATABASE AND USER FOR TEST PURPOSES

-- Creates a Schema/database hbnb_test_db if does not exist
CREATE SCHEMA IF NOT EXISTS `hbnb_test_db`;

-- Drop user hbnb_test if already existing and create a new user
DROP USER IF EXISTS 'hbnb_test'@'localhost';
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the newly created user hbnb_test
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
