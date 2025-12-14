CREATE TABLE sql_store.customers (
    Customer_id INT PRIMARY KEY,
    First_name VARCHAR(50) NOT NULL,
    Last_name VARCHAR(50) NOT NULL,
    Date_of_birth DATE NOT NULL,
    Address VARCHAR(100)
);

CREATE TABLE sql_store.products (
    Order_id INT PRIMARY KEY,
    Product_id INT NOT NULL,
    Quantity_in_stock INT NOT NULL,
    Unit_price DECIMAL(10,2) NOT NULL
);

INSERT INTO sql_store.customers VALUES (12, 'Becky', 'Benson', '1980-01-01', 'Sunny Avenue');
INSERT INTO sql_store.customers VALUES (13, 'Liam', 'Humphrey', '1990-01-01', 'Berlin Trail');
INSERT INTO sql_store.customers VALUES (14, 'Tom', 'Huny', '2002-02-10', 'Third Avenue');
INSERT INTO sql_store.customers VALUES (15, 'Lilian', 'Banford', '1999-10-10', 'Riley Court');

INSERT INTO sql_store.products VALUES (2, 22, 200, 2);
INSERT INTO sql_store.products VALUES (3, 23, 300, 15);
INSERT INTO sql_store.products VALUES (4, 24, 200, 27);
INSERT INTO sql_store.products VALUES (5, 25, 100, 30);

-- Question 3

SELECT order_id, order_date, shipped_date, DATEDIFF(shipped_date, order_date) AS daysdiff
FROM sql_store.order_items;

-- Question 4

SELECT product_id, quantity_in_stock, unit_price
FROM sql_store.products
WHERE quantity_in_stock IN (200, 300);

-- Question 5
SELECT Customer_id, First_name, Last_name, Address
FROM sql_store.customers
WHERE Address LIKE '%Trail'
    OR Address LIKE '%Avenue';

-- Question 6
DELETE FROM sql_store.products
WHERE Order_id = 6 
  AND Product_id = 26 
  AND Quantity_in_stock = 70 
  AND Unit_price = 20;

SELECT p.Order_id, p.Product_id, p.Quantity_in_stock, p.Unit_price,
    oi.order_id, oi.product_id, oi.quantity, oi.unit_price AS order_item_price
FROM sql_store.products AS p
JOIN sql_store.order_items AS oi
    ON p.Order_id = oi.order_id;