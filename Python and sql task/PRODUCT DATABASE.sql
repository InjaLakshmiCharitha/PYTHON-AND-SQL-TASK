CREATE DATABASE product_db; 

USE product_db;

CREATE TABLE products (
 product_id INT PRIMARY KEY AUTO_INCREMENT,
 product_name VARCHAR(100) NOT NULL,
 price DECIMAL(10,2) NOT NULL, quantity INT NOT NULL,
 category VARCHAR(50) );

SELECT * FROM products;
