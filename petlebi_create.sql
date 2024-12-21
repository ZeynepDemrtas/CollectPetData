CREATE SCHEMA IF NOT EXISTS `db_petlebi`;

CREATE TABLE IF NOT EXISTS db_petlebi.petlebi (product_URL VARCHAR(255), product_name VARCHAR(255), product_barcode VARCHAR(255),
product_price DOUBLE, product_stock VARCHAR(255), product_images VARCHAR(255), description LONGTEXT,
sku VARCHAR(255), category VARCHAR(255), product_id INTEGER, brand VARCHAR(255))
