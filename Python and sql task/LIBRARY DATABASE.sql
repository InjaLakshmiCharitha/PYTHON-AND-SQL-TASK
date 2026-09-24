-- Create database
Create database library_db; 
-- Select database 
USE library_db;

-- BOOKS TABLE
CREATE TABLE Books ( book_id INT PRIMARY KEY AUTO_INCREMENT,
 title VARCHAR(150) NOT NULL,
 author VARCHAR(100) NOT NULL,
 category VARCHAR(50),
 published_year INT,
 available BOOLEAN DEFAULT TRUE );
 
 -- MEMBERS TABLE
 CREATE TABLE Members ( member_id INT PRIMARY KEY AUTO_INCREMENT,
 member_name VARCHAR(100) NOT NULL,
 email VARCHAR(100) UNIQUE NOT NULL,
 phone VARCHAR(15) UNIQUE,
 join_date DATE NOT NULL );
 
 -- BORROW RECORDS TABLE
 CREATE TABLE Borrow_Records ( borrow_id INT PRIMARY KEY AUTO_INCREMENT,
 book_id INT NOT NULL, member_id INT NOT NULL,
 borrow_date DATE NOT NULL,
 return_date DATE,
 FOREIGN KEY (book_id) REFERENCES Books(book_id),
 FOREIGN KEY (member_id) REFERENCES Members(member_id) );
 
 -- CRUD OPERATIONS
 
 -- INSERT BOOKS
 INSERT INTO Books (title, author, category, published_year, available) VALUES 
 ('Python Programming', 'Mark Lutz', 'Programming', 2020, TRUE),
 ('SQL Fundamentals', 'John Smith', 'Database', 2021, TRUE), 
 ('Data Structures', 'Robert Lafore', 'Programming', 2019, TRUE),
 ('Web Development', 'David Miller', 'Web', 2022, TRUE),
 ('Computer Networks', 'Andrew Tanenbaum', 'Networking', 2018, TRUE);
 
 -- READ / SELECT
 SELECT * FROM Books;
 SELECT book_id, title, author, category FROM Books;
 
 -- UPDATE
 UPDATE Books SET category = 'Python Programming' WHERE book_id = 1;
 UPDATE Books SET available = FALSE WHERE book_id = 3;
 
 -- DELETE
 DELETE FROM Books WHERE book_id = 5;
 
 -- Check final records
 SELECT * FROM Books;
 
 -- INSERT MEMBERS
 INSERT INTO Members (member_name, email, phone, join_date) VALUES
 ('Charitha', 'charitha@gmail.com', '9876543210', '2026-01-20'),
 ('Rahul', 'rahul@gmail.com', '9876543211', '2026-02-12'),
 ('Sravani', 'sravani@gmail.com', '6300258652', '2026-03-15'),
 ('Vasavi', 'vasavi@gmail.com', '7993032596', '2026-04-17');
  SELECT * FROM Members;
  
  -- INSERT BORROW_RECORDS
INSERT INTO Borrow_Records (book_id, member_id, borrow_date, return_date) VALUES
(1, 1, '2026-09-01', '2026-09-10'),
(2, 2, '2026-09-05', NULL),
(3, 3, '2026-09-08', '2026-09-15'),
(4, 4, '2026-09-15', '2026-09-23');
SELECT * FROM Borrow_Records;

-- JOIN
SELECT b.title, b.author, m.member_name, br.borrow_date, br.return_date
FROM Borrow_Records br JOIN Books b ON br.book_id = b.book_id JOIN Members m ON br.member_id = m.member_id;

-- GROUP BY
SELECT category, COUNT(*) AS total_books FROM Books GROUP BY category;
SELECT member_id, COUNT(*) AS total_borrowed FROM Borrow_Records GROUP BY member_id;

-- ORDER BY
SELECT * FROM Books ORDER BY title ASC;
SELECT * FROM Books ORDER BY published_year DESC;

-- AGGREGATE FUNCTIONS
-- COUNT
SELECT COUNT(*) AS total_books FROM Books;
-- AVG
SELECT AVG(published_year) AS average_year FROM Books;
-- MIN
SELECT MIN(published_year) AS oldest_book_year FROM Books;
-- MAX
SELECT MAX(published_year) AS newest_book_year FROM Books;


-- VIEWS FOR BORROWED BOOKS 
-- BORROWED BOOK REPORT
CREATE VIEW Borrowed_Book_Report AS
SELECT br.borrow_id, b.book_id, b.title, b.author, m.member_id, m.member_name, m.email, br.borrow_date, br.return_date FROM 
Borrow_Records br
JOIN Books b ON br.book_id = b.book_id
JOIN Members m ON br.member_id = m.member_id;

SELECT * FROM Borrowed_Book_Report;

-- CURRENTLY BORROWED BOOKS
CREATE VIEW Currently_Borrowed_Books AS
SELECT b.title, b.author, m.member_name, br.borrow_date FROM
Borrow_Records br 
JOIN Books b ON br.book_id = b.book_id
JOIN Members m ON br.member_id = m.member_id
WHERE br.return_date IS NULL;

SELECT * FROM Currently_Borrowed_Books;

