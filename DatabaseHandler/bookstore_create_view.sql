-- View: TOTAL REVENUE

CREATE VIEW total_revenue_view AS
SELECT
  o.store_id,
  SUM(oi.quantity * oi.book_price * (1 - oi.discount)) AS total_revenue
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY o.store_id;

-- View: BOOKS SOLD

CREATE VIEW books_sold_view AS
SELECT
  o.store_id,
  COUNT(DISTINCT oi.book_id) AS books_sold
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY o.store_id;

-- View: AVERAGE BOOK PRICE

CREATE VIEW avg_book_price_view AS
SELECT
  o.store_id,
  AVG(oi.book_price) AS avg_book_price
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY o.store_id;

-- View: BEST SELLER BOOK

CREATE VIEW best_seller_book_view AS
SELECT
  o.store_id,
  oi.book_id,
  SUM(oi.quantity) AS total_quantity_sold
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY o.store_id, oi.book_id
ORDER BY total_quantity_sold DESC
LIMIT 1;

-- View: BEST SELLER GENRE

CREATE VIEW best_seller_genre_view AS
SELECT
  o.store_id,
  b.genre_id,
  SUM(oi.quantity) AS total_quantity_sold
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN production.books b ON oi.book_id = b.book_id
GROUP BY o.store_id, b.genre_id
ORDER BY total_quantity_sold DESC
LIMIT 1;

-- View: BEST SELLER AUTHOR

CREATE VIEW best_seller_author_view AS
SELECT
  o.store_id,
  b.author_id,
  SUM(oi.quantity) AS total_quantity_sold
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN production.books b ON oi.book_id = b.book_id
GROUP BY o.store_id, b.author_id
ORDER BY total_quantity_sold DESC
LIMIT 1;

-- View: TOTAL CUSTOMERS

CREATE VIEW total_customers_view AS
SELECT
  s.store_id,
  COUNT(DISTINCT o.customer_id) AS total_customers
FROM sales.stores s
LEFT JOIN sales.orders o ON s.store_id = o.store_id
GROUP BY s.store_id;

-- View: YEARLY SALES GROWTH

CREATE VIEW yearly_sales_growth_view AS
SELECT
  store_id,
  EXTRACT(YEAR FROM order_date) AS order_year,
  SUM(SUM(oi.quantity * oi.book_price * (1 - oi.discount))) OVER (PARTITION BY store_id ORDER BY EXTRACT(YEAR FROM order_date)) AS yearly_sales
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY store_id, EXTRACT(YEAR FROM order_date);

-- View: BOOKS IN STOCK

CREATE VIEW books_in_stock_view AS
SELECT
  s.store_id,
  COUNT(*) AS books_in_stock
FROM sales.stores s
JOIN production.stocks st ON s.store_id = st.store_id
GROUP BY s.store_id;

-- View: TOP PERFORMING EMPLOYEE

CREATE VIEW top_performing_employee_view AS
SELECT
  s.store_id,
  o.staff_id,
  SUM(oi.quantity * oi.book_price * (1 - oi.discount)) AS total_revenue
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN sales.stores s ON o.store_id = s.store_id
GROUP BY s.store_id, o.staff_id
ORDER BY total_revenue DESC
LIMIT 1;

-- View: TOP PERFORMING MANAGER

CREATE VIEW top_performing_manager_view AS
SELECT
  s.store_id,
  s.manager_id,
  SUM(oi.quantity * oi.book_price * (1 - oi.discount)) AS total_revenue
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN sales.stores s ON o.store_id = s.store_id
GROUP BY s.store_id, s.manager_id
ORDER BY total_revenue DESC
LIMIT 1;

-- View: TOP PERFORMING STORE

CREATE VIEW top_performing_store_view AS
SELECT
  s.store_id,
  SUM(oi.quantity * oi.book_price * (1 - oi.discount)) AS total_revenue
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN sales.stores s ON o.store_id = s.store_id
GROUP BY s.store_id
ORDER BY total_revenue DESC
LIMIT 1;
