create database class1;

use class1;
GO


IF OBJECT_ID('department') IS NULL
BEGIN
	CREATE TABLE department (
		ID INT NOT NULL, 
		Name NVARCHAR(255) NOT NULL,
		Description NVARCHAR(MAX) NULL
	);
END


DROP TABLE IF EXISTS department;

CREATE TABLE department (
	ID INT NOT NULL, 
	Name NVARCHAR(255) NOT NULL,
	Description NVARCHAR(MAX) NULL
);




/*
CREATE TABLE blogs (
	id INT,
	title NVARCHAR(255),
	blog_text NVARCHAR(MAX)
);
*/

SELECT * FROM department;

INSERT INTO department(ID, Name, Description)
VALUES
	(3, 'Marketing', 'This is marketing department'),
	(4, 'Demo', NULL);

INSERT INTO department(Name, ID, Description)
VALUES
	('Demo2', 4, NULL);

--Conversion failed when converting the varchar value 'Demo2' to data type int.

