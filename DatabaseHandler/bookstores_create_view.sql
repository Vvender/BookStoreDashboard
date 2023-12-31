-- 1. Total Revenue (total revenue of my stores)
CREATE VIEW total_revenue_view AS
SELECT
    s.store_id,
    s.store_name,
    ISNULL(SUM(oi.quantity * oi.book_price * (1 - oi.discount)), 0) AS total_revenue
FROM
    sales.stores s
LEFT JOIN sales.orders o ON s.store_id = o.store_id
LEFT JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY
    s.store_id, s.store_name;

-- 2. Total Number of books sold (total number of books sold in my stores)
CREATE VIEW total_books_sold_view AS
SELECT
    s.store_id,
    s.store_name,
    ISNULL(SUM(oi.quantity), 0) AS total_books_sold
FROM
    sales.stores s
LEFT JOIN sales.orders o ON s.store_id = o.store_id
LEFT JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY
    s.store_id, s.store_name;

-- 3. Average book price (average book price of sold books in all stores)
CREATE VIEW average_book_price_view AS
SELECT
    ISNULL(AVG(oi.book_price), 0) AS average_book_price
FROM
    sales.stores s
LEFT JOIN sales.orders o ON s.store_id = o.store_id
LEFT JOIN sales.order_items oi ON o.order_id = oi.order_id;

-- 4. Best seller book (select the most sold book in total)
CREATE VIEW best_seller_book_view AS
SELECT TOP 1 WITH TIES
    b.book_id,
    b.book_name,
    ISNULL(SUM(oi.quantity), 0) AS total_quantity_sold
FROM
    production.books b
LEFT JOIN sales.order_items oi ON b.book_id = oi.book_id
GROUP BY
    b.book_id, b.book_name
ORDER BY
    total_quantity_sold DESC;

-- 5. Best seller genre (select the most sold genre in total)
CREATE VIEW best_seller_genre_view AS
SELECT TOP 1 WITH TIES
    g.genre_id,
    g.genre_name,
    ISNULL(SUM(oi.quantity), 0) AS total_quantity_sold
FROM
    production.genres g
LEFT JOIN production.books b ON g.genre_id = b.genre_id
LEFT JOIN sales.order_items oi ON b.book_id = oi.book_id
GROUP BY
    g.genre_id, g.genre_name
ORDER BY
    total_quantity_sold DESC;

-- 6. Best seller author (select the most sold author in total)
CREATE VIEW best_seller_author_view AS
SELECT TOP 1 WITH TIES
    a.author_id,
    a.author_name,
    ISNULL(SUM(oi.quantity), 0) AS total_quantity_sold
FROM
    production.authors a
LEFT JOIN production.books b ON a.author_id = b.author_id
LEFT JOIN sales.order_items oi ON b.book_id = oi.book_id
GROUP BY
    a.author_id, a.author_name
ORDER BY
    total_quantity_sold DESC;

-- 7. Number of customers (number of our customers in total)
CREATE VIEW number_of_customers_view AS
SELECT
    COUNT(DISTINCT c.customer_id) AS total_customers
FROM
    sales.customers c;

-- 8. Yearly sales growth (compare this year's revenue to the year before)
CREATE VIEW yearly_sales_growth_view AS
SELECT
    YEAR(o.order_date) AS sales_year,
    ISNULL(SUM(oi.quantity * oi.book_price * (1 - oi.discount)), 0) AS total_revenue
FROM
    sales.orders o
LEFT JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY
    YEAR(o.order_date);

-- 9. Books in stock (total books in our stocks)
CREATE VIEW books_in_stock_view AS
SELECT
    s.store_id,
    s.store_name,
    ISNULL(SUM(ps.quantity), 0) AS total_books_in_stock
FROM
    production.stocks ps
LEFT JOIN sales.stores s ON ps.store_id = s.store_id
GROUP BY
    s.store_id, s.store_name;

-- 10. Top-performing employee (staff that has the best revenue)
CREATE VIEW top_performing_employee_view AS
SELECT TOP 1 WITH TIES
    st.staff_id,
    st.first_name + ' ' + st.last_name AS employee_name,
    ISNULL(SUM(oi.quantity * oi.book_price * (1 - oi.discount)), 0) AS total_revenue
FROM
    sales.staff st
LEFT JOIN sales.orders o ON st.staff_id = o.staff_id
LEFT JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY
    st.staff_id, st.first_name, st.last_name
ORDER BY
    total_revenue DESC;

-- Drop the existing top_performing_manager_view if it exists
IF OBJECT_ID('top_performing_manager_view', 'V') IS NOT NULL
    DROP VIEW top_performing_manager_view;

-- Create the updated top_performing_manager_view
CREATE VIEW top_performing_manager_view AS
SELECT TOP 1 WITH TIES
    s.store_id,
    s.store_name,
    s.manager_id AS manager_id,
    CONCAT(st.first_name, ' ', st.last_name) AS manager_name,
    ISNULL(SUM(oi.quantity * oi.book_price * (1 - oi.discount)), 0) AS total_revenue
FROM
    sales.stores s
JOIN sales.staff st ON s.manager_id = st.staff_id
LEFT JOIN sales.orders o ON s.store_id = o.store_id
LEFT JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY
    s.store_id, s.store_name, s.manager_id, st.first_name, st.last_name
ORDER BY
    total_revenue DESC;


-- 12. Top-performing store (store that has the best revenue)
CREATE VIEW top_performing_store_view AS
SELECT TOP 1 WITH TIES
    s.store_id,
    s.store_name,
    ISNULL(SUM(oi.quantity * oi.book_price * (1 - oi.discount)), 0) AS total_revenue
FROM
    sales.stores s
LEFT JOIN sales.orders o ON s.store_id = o.store_id
LEFT JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY
    s.store_id, s.store_name
ORDER BY
    total_revenue DESC;
