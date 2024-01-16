USE BookStores;

-- Inserting data into production.publishers
INSERT INTO production.publishers (publisher_name) VALUES
('Penguin Random House'),
('HarperCollins'),
('Simon & Schuster'),
('Hachette Livre'),
('Macmillan Publishers'),
('Bloomsbury'),
('Scholastic Corporation'),
('Pearson'),
('Wiley'),
('Oxford University Press');

-- Inserting data into production.authors
INSERT INTO production.authors (author_name) VALUES
('J.K. Rowling'),
('Dan Brown'),
('Stephen King'),
('George R.R. Martin'),
('James Patterson'),
('John Grisham'),
('Suzanne Collins'),
('Malcolm Gladwell'),
('J.R.R. Tolkien'),
('Nora Roberts'),
('Salman Rushdie'),
('Ken Follett'),
('Neil Gaiman'),
('Danielle Steel'),
('David Baldacci'),
('Hilary Mantel'),
('Margaret Atwood'),
('Bill Bryson'),
('Michael Lewis'),
('Richard Dawkins');


-- Inserting data into production.genres
INSERT INTO production.genres (genre_name) VALUES
('Fantasy'),
('Young Adult'),
('Thriller'),
('Mystery'),
('Horror'),
('Supernatural'),
('Epic Fantasy'),
('Legal Thriller'),
('Crime Fiction'),
('Dystopian Fiction'),
('Science Fiction'),
('Non-Fiction'),
('Psychology'),
('High Fantasy'),
('Romance'),
('Contemporary Fiction'),
('Historical Fiction'),
('Dark Fantasy'),
('Drama'),
('Travel'),
('Finance'),
('Magical Realism'),
('Speculative Fiction'),
('Evolutionary Biology');


-- Inserting data into production.books
INSERT INTO production.books (book_barcode, book_name, book_page, book_price, author_id, genre_id, publisher_id) VALUES
('100000000001', 'The Wizarding World', 400, 29.99, 1, 1, 1),
('100000000002', 'The Da Vinci Code', 450, 24.99, 2, 3, 2),
('100000000003', 'The Shining', 350, 19.99, 3, 5, 3),
('100000000004', 'A Game of Thrones', 600, 39.99, 4, 7, 4),
('100000000005', 'Along Came a Spider', 320, 15.99, 5, 9, 5),
('100000000006', 'The Firm', 400, 22.99, 6, 8, 6),
('100000000007', 'The Hunger Games', 370, 18.99, 7, 10, 7),
('100000000008', 'Outliers', 300, 21.99, 8, 11, 8),
('100000000009', 'The Hobbit', 320, 26.99, 9, 6, 9),
('100000000010', 'Nora Roberts Collection', 500, 34.99, 10, 15, 10),
('100000000011', 'Midnights Children', 450, 29.99, 11, 16, 1),
('100000000012', 'American Gods', 480, 31.99, 12, 13, 2),
('100000000013', 'Steel Collection', 420, 27.99, 13, 14, 3),
('100000000014', 'Absolute Power', 380, 23.99, 14, 9, 4),
('100000000015', 'Wolf Hall', 500, 32.99, 15, 16, 5),
('100000000016', 'The Handmaid''s Tale', 350, 25.99, 16, 11, 6),
('100000000017', 'A Short History of Nearly Everything', 550, 38.99, 17, 12, 7),
('100000000018', 'The Testaments', 400, 29.99, 18, 16, 8),
('100000000019', 'A Walk in the Woods', 320, 21.99, 19, 19, 9),
('100000000020', 'Moneyball', 400, 24.99, 20, 20, 10),
('100000000021', 'The Casual Vacancy', 380, 26.99, 1, 16, 1),
('100000000022', 'Inferno', 420, 29.99, 2, 3, 2),
('100000000023', 'Doctor Sleep', 400, 28.99, 3, 5, 3),
('100000000024', 'A Clash of Kings', 550, 36.99, 4, 7, 4),
('100000000025', 'Kiss the Girls', 340, 18.99, 5, 9, 5),
('100000000026', 'The Pelican Brief', 370, 21.99, 6, 8, 6),
('100000000027', 'Catching Fire', 360, 19.99, 7, 10, 7),
('100000000028', 'Blink', 320, 23.99, 8, 11, 8),
('100000000029', 'The Silmarillion', 400, 27.99, 9, 6, 9),
('100000000030', 'The Inn BoonsBoro Trilogy', 480, 33.99, 10, 15, 10),
('100000000031', 'Haroun and the Sea of Stories', 300, 17.99, 11, 16, 1),
('100000000032', 'Neverwhere', 420, 28.99, 12, 13, 2),
('100000000033', 'Rogue Lawyer', 390, 25.99, 13, 14, 3),
('100000000034', 'The Summons', 340, 20.99, 14, 9, 4),
('100000000035', 'Bring Up the Bodies', 460, 31.99, 15, 16, 5),
('100000000036', 'The Testament of Mary', 330, 22.99, 16, 11, 6),
('100000000037', 'The Pearl That Broke Its Shell', 400, 26.99, 18, 16, 8),
('100000000038', 'The Blind Side', 320, 23.99, 20, 20, 10),
('100000000039', 'The Night Circus', 420, 28.99, 1, 1, 1),
('100000000040', 'Angels & Demons', 380, 25.99, 2, 3, 2),
('100000000041', 'Doctor Zhivago', 500, 34.99, 3, 5, 3),
('100000000042', 'A Storm of Swords', 600, 42.99, 4, 7, 4),
('100000000043', 'Cross', 360, 19.99, 5, 9, 5),
('100000000044', 'The Client', 340, 21.99, 6, 8, 6),
('100000000045', 'Mockingjay', 400, 27.99, 7, 10, 7),
('100000000046', 'David and Goliath', 320, 23.99, 8, 11, 8),
('100000000047', 'The Children of Húrin', 380, 26.99, 9, 6, 9),
('100000000048', 'The Liar', 420, 29.99, 10, 15, 10),
('100000000049', 'Luka and the Fire of Life', 350, 22.99, 11, 16, 1),
('100000000050', 'Good Omens', 400, 28.99, 12, 13, 2),
('100000000051', 'The Testament', 370, 25.99, 13, 14, 3),
('100000000052', 'The Whistler', 340, 20.99, 14, 9, 4),
('100000000053', 'The Escape', 400, 29.99, 18, 16, 8),
('100000000054', 'The Innovators', 550, 38.99, 19, 12, 7),
('100000000055', 'The Sun Also Rises', 320, 24.99, 20, 20, 10);

-- Inserting data into sales.customers
INSERT INTO sales.customers (first_name, last_name, phone, email, address) VALUES
('John', 'Doe', '1234567890', 'john.doe@example.com', '123 Main St, City'),
('Jane', 'Smith', '9876543210', 'jane.smith@example.com', '456 Elm St, Town'),
('Michael', 'Johnson', '6758493021', 'michael.johnson@example.com', '789 Oak Ave, Village'),
('Emily', 'Brown', '1928374650', 'emily.brown@example.com', '567 Pine St, County'),
('William', 'Davis', '3847562910', 'william.davis@example.com', '890 Cedar Ave, Hamlet'),
('Olivia', 'Martinez', '5061728394', 'olivia.martinez@example.com', '234 Birch Ln, Borough');

-- Inserting data into sales.stores
INSERT INTO sales.stores (store_name, phone, email, address) VALUES
('Main Store', '9876543210', 'info@mainstore.com', '456 Center St, City'),
('Downtown Store', '9871234560', 'info@downtownstore.com', '789 Elm St, City'),
('West End Store', '9870011220', 'info@westendstore.com', '101 Oak St, City');



-- Inserting data into sales.staff
INSERT INTO sales.staff (first_name, last_name, email, phone, active, store_id, address) VALUES
('Alice', 'Smith', 'alice.smith@example.com', '5551234567', 0, 1, '123 Center St, City'),
('Bob', 'Johnson', 'bob.johnson@example.com', '5559876543', 0, 2, '456 Elm St, Town'),
('Eva', 'Williams', 'eva.williams@example.com', '5551928374', 0, 3, '789 Oak Ave, Village'),
('David', 'Miller', 'david.miller@example.com', '5553847562', 0, 1, '567 Pine St, County'),
('Sophia', 'Garcia', 'sophia.garcia@example.com', '5555061728', 0, 2, '890 Cedar Ave, Hamlet'),
('James', 'Rodriguez', 'james.rodriguez@example.com', '5556758493', 0, 1, '234 Birch Ln, Borough'),
('Ava', 'Lopez', 'ava.lopez@example.com', '5559302716', 0, 1, '345 Maple Rd, Village'),
('Daniel', 'Gonzalez', 'daniel.gonzalez@example.com', '5558192736', 0, 1, '456 Pineapple Ave, Town'),
('Mia', 'Hernandez', 'mia.hernandez@example.com', '5556273849', 0, 2, '678 Orange St, City'),
('Alex', 'Moore', 'alexander.moore@example.com', '5557384950', 0, 3, '789 Lemon Ln, County'),
('Charlotte', 'Perez', 'charlotte.perez@example.com', '5558493052', 0, 1, '890 Cherry Dr, Hamlet');

-- Updating manager_id for each store
UPDATE sales.stores SET manager_id = (SELECT staff_id FROM sales.staff WHERE first_name = 'Alice') WHERE store_id = 1;
UPDATE sales.stores SET manager_id = (SELECT staff_id FROM sales.staff WHERE first_name = 'Bob') WHERE store_id = 2;
UPDATE sales.stores SET manager_id = (SELECT staff_id FROM sales.staff WHERE first_name = 'Eva') WHERE store_id = 3;


-- Inserting data into sales.orders
INSERT INTO sales.orders (customer_id, order_date, store_id, staff_id) VALUES
(1, '2023-12-05', 1, 4),
(2, '2023-12-06', 2, 5),
(3, '2023-12-07', 3, 10),
(4, '2023-12-10', 1, 4),
(5, '2023-12-11', 2, 9),
(1, '2024-01-08', 3, 10),
(2, '2024-01-08', 1, 4),
(3, '2024-01-09', 2, 5),
(4, '2024-01-09', 3, 10),
(5, '2024-01-10', 1, 6),
(1, '2024-01-11', 2, 9),
(2, '2024-01-11', 3, 10),
(3, '2024-01-12', 1, 6),
(4, '2024-01-12', 2, 9),
(5, '2024-01-13', 3, 10),
(1, '2024-01-14', 1, 7),
(2, '2024-01-14', 2, 5),
(3, '2024-01-15', 3, 10),
(4, '2024-01-15', 1, 8),
(5, '2024-01-16', 2, 9);

-- Inserting data into sales.order_items
INSERT INTO sales.order_items (order_id, item_id, book_id, quantity, book_price, discount) VALUES
(1, 1, 1, 2, 29.99, 0.05),
(1, 2, 3, 1, 24.99, 0.1),
(1, 3, 5, 3, 19.99, 0.08),
(2, 1, 7, 1, 39.99, 0.12),
(3, 1, 10, 2, 15.99, 0.07),
(3, 2, 15, 1, 22.99, 0.1),
(4, 1, 20, 4, 18.99, 0.06),
(4, 2, 25, 1, 21.99, 0.08),
(5, 1, 30, 2, 26.99, 0.1),
(5, 2, 35, 1, 34.99, 0.15),
(6, 1, 40, 3, 32.99, 0.12),
(6, 2, 45, 1, 28.99, 0.1),
(7, 1, 50, 2, 25.99, 0.07),
(7, 2, 55, 1, 38.99, 0.1),
(8, 1, 10, 4, 23.99, 0.09),
(9, 1, 15, 1, 27.99, 0.12),
(9, 2, 20, 2, 29.99, 0.1),
(9, 3, 25, 1, 36.99, 0.15),
(9, 4, 30, 3, 21.99, 0.08),
(10, 1, 35, 1, 24.99, 0.1),
(11, 1, 40, 2, 26.99, 0.1),
(11, 2, 45, 1, 32.99, 0.12),
(12, 1, 50, 3, 27.99, 0.1),
(12, 2, 55, 1, 29.99, 0.15),
(13, 1, 10, 2, 36.99, 0.08),
(13, 2, 15, 1, 38.99, 0.1),
(14, 1, 20, 4, 23.99, 0.09),
(15, 1, 25, 1, 27.99, 0.12),
(15, 2, 30, 2, 29.99, 0.1),
(15, 3, 35, 1, 36.99, 0.15),
(16, 1, 40, 3, 21.99, 0.08),
(16, 2, 45, 1, 24.99, 0.1),
(17, 1, 50, 2, 26.99, 0.1),
(17, 2, 55, 1, 32.99, 0.12),
(18, 1, 10, 3, 27.99, 0.1),
(18, 2, 15, 1, 29.99, 0.15),
(19, 1, 20, 2, 36.99, 0.08),
(19, 2, 25, 1, 38.99, 0.1),
(20, 1, 30, 4, 23.99, 0.09),
(20, 2, 35, 1, 27.99, 0.12);

-- Inserting data into production.stocks
INSERT INTO production.stocks (store_id, book_id, quantity) VALUES
(1,1,54),
(1,2,31),
(1,3,48),
(1,4,18),
(1,5,39),
(1,6,23),
(1,7,29),
(1,8,57),
(1,9,40),
(1,10,26),
(1,11,17),
(1,12,37),
(1,13,45),
(1,14,27),
(1,15,36),
(1,16,59),
(1,17,19),
(1,18,52),
(1,19,55),
(1,20,34),
(1,21,20),
(1,22,41),
(1,23,24),
(1,24,16),
(1,25,56),
(1,26,58),
(1,27,30),
(1,28,49),
(1,29,35),
(1,30,47),
(1,31,42),
(1,32,32),
(1,33,21),
(1,34,28),
(1,35,25),
(1,36,38),
(1,37,50),
(1,38,46),
(1,39,53),
(1,40,22),
(1,41,44),
(1,42,33),
(1,43,60),
(1,44,51),
(1,45,15),
(1,46,43),
(1,47,52),
(1,48,19),
(1,49,30),
(1,50,44),
(1,51,34),
(1,52,25),
(1,53,29),
(1,54,50),
(1,55,46),
(2,1,63),
(2,2,39),
(2,3,46),
(2,4,60),
(2,5,20),
(2,6,64),
(2,7,30),
(2,8,28),
(2,9,42),
(2,10,61),
(2,11,53),
(2,12,16),
(2,13,50),
(2,14,59),
(2,15,31),
(2,16,23),
(2,17,36),
(2,18,26),
(2,19,57),
(2,20,41),
(2,21,33),
(2,22,22),
(2,23,38),
(2,24,56),
(2,25,19),
(2,26,65),
(2,27,47),
(2,28,32),
(2,29,54),
(2,30,18),
(2,31,25),
(2,32,58),
(2,33,35),
(2,34,62),
(2,35,49),
(2,36,24),
(2,37,17),
(2,38,44),
(2,39,15),
(2,40,21),
(2,41,29),
(2,42,48),
(2,43,37),
(2,44,27),
(2,45,52),
(2,46,43),
(2,47,45),
(2,48,55),
(2,49,34),
(2,50,51),
(2,51,40),
(2,52,63),
(2,53,22),
(2,54,19),
(2,55,62),
(3,1,42),
(3,2,15),
(3,3,28),
(3,4,40),
(3,5,23),
(3,6,38),
(3,7,50),
(3,8,16),
(3,9,34),
(3,10,46),
(3,11,19),
(3,12,27),
(3,13,49),
(3,14,13),
(3,15,55),
(3,16,30),
(3,17,14),
(3,18,32),
(3,19,41),
(3,20,26),
(3,21,11),
(3,22,52),
(3,23,25),
(3,24,53),
(3,25,47),
(3,26,31),
(3,27,35),
(3,28,48),
(3,29,44),
(3,30,20),
(3,31,12),
(3,32,36),
(3,33,29),
(3,34,51),
(3,35,45),
(3,36,22),
(3,37,33),
(3,38,24),
(3,39,37),
(3,40,17),
(3,41,39),
(3,42,10),
(3,43,18),
(3,44,43),
(3,45,54),
(3,46,21),
(3,47,50),
(3,48,14),
(3,49,31),
(3,50,26),
(3,51,11),
(3,52,45),
(3,53,38),
(3,54,53),
(3,55,40);

