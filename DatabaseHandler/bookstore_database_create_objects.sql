-- Create the database
CREATE DATABASE BookStores;
GO

-- Use the database
USE BookStores;
GO

-- create schemas
CREATE SCHEMA production;
GO

CREATE SCHEMA sales;
GO

-- Table: production.publishers
CREATE TABLE production.publishers (
    publisher_id SMALLINT IDENTITY(1,1) PRIMARY KEY,
    publisher_name VARCHAR(25) UNIQUE NOT NULL
);

-- Table: production.authors
CREATE TABLE production.authors (
    author_id SMALLINT IDENTITY(1,1) PRIMARY KEY,
    author_name VARCHAR(25) UNIQUE NOT NULL
);

-- Table: production.genres
CREATE TABLE production.genres (
    genre_id SMALLINT IDENTITY(1,1) PRIMARY KEY,
    genre_name VARCHAR(25) UNIQUE NOT NULL
);

-- Table: production.books
CREATE TABLE production.books (
    book_id INT IDENTITY(1,1) PRIMARY KEY,
    book_barcode NCHAR(12) UNIQUE NOT NULL,
    book_name VARCHAR(100) UNIQUE NOT NULL,
    book_page SMALLINT NOT NULL,
    book_price DECIMAL (10,2) NOT NULL,
    author_id SMALLINT NOT NULL,
    genre_id SMALLINT NOT NULL,
    publisher_id SMALLINT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES production.authors(author_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES production.genres(genre_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (publisher_id) REFERENCES production.publishers(publisher_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: sales.customers
CREATE TABLE sales.customers (
    customer_id INT IDENTITY (1, 1) PRIMARY KEY,
    first_name VARCHAR (255) NOT NULL,
    last_name VARCHAR (255) NOT NULL,
    phone VARCHAR (25) UNIQUE NOT NULL,
    email VARCHAR (255) UNIQUE NOT NULL,
    address VARCHAR (255)
);

-- Table: sales.stores
CREATE TABLE sales.stores (
    store_id INT IDENTITY (1, 1) PRIMARY KEY,
    store_name VARCHAR (255) NOT NULL,
    phone VARCHAR (25),
    email VARCHAR (255),
    address VARCHAR (255)
);

-- Table: sales.staff
CREATE TABLE sales.staff (
    staff_id INT IDENTITY (1, 1) PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (50) NOT NULL,
    email VARCHAR (255) NOT NULL UNIQUE,
    phone VARCHAR (25) NOT NULL UNIQUE,
    active TINYINT NOT NULL,
    store_id INT NOT NULL,
    manager_id INT,
    address VARCHAR (255),
    FOREIGN KEY (store_id) REFERENCES sales.stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (manager_id) REFERENCES sales.staff (staff_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Table: sales.orders
CREATE TABLE sales.orders (
    order_id INT IDENTITY (1, 1) PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    store_id INT NOT NULL,
    staff_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES sales.customers (customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (store_id) REFERENCES sales.stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES sales.staff (staff_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Table: sales.order_items
CREATE TABLE sales.order_items (
    order_id INT,
    item_id INT,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    list_price DECIMAL (10, 2) NOT NULL,
    discount DECIMAL (4, 2) NOT NULL DEFAULT 0,
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES sales.orders (order_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (book_id) REFERENCES production.books (book_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: production.stocks
CREATE TABLE production.stocks (
    store_id INT,
    book_id INT,
    quantity INT,
    PRIMARY KEY (store_id, book_id),
    FOREIGN KEY (store_id) REFERENCES sales.stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (book_id) REFERENCES production.books (book_id) ON DELETE CASCADE ON UPDATE CASCADE
);