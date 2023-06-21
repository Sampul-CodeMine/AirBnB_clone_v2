-- CREATES A DATABASE AND USER FOR DEVELOPMENT PURPOSES

-- Creates a Schema/database if not exist
CREATE SCHEMA IF NOT EXISTS `hbnb_dev_db`;

-- Drop user if already existing and create a new user
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant some privileges to the newly created user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
