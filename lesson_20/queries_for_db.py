create_table_category = """
CREATE TABLE category(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);
"""

create_table_product = """
CREATE TABLE product(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(250) NOT NULL,
    decryption VARCHAR(500),
    price DECIMAL(6, 2) NOT NULL,
    category_id INTEGER REFERENCES category(id) ON DELETE SET NULL
);
"""

insert_into_category = """
INSERT INTO category (name)
VALUES 
('fruits'), 
('toiletries'), 
('clothes');
"""

insert_into_product = """
INSERT INTO product (name, manufacturer, decryption, price, category_id)
VALUES
('apple', 'FreshForAll', 'apple "golden"; Greece', 26.75, 1),
('soap', 'CleanUp', 'soap with lavender scent', 68.90, 2),
('socks', 'DressUp', 'socks black; 100% silk', 189.99, 3),
('toothpaste', 'CleanUp', 'toothpaste with mint flavor', 155.40, 2),
('banana', 'SweetFruits', 'banana "nendrum"; Nepal', 73.89, 1),
('peach', 'FreshForAll', 'peach; Turkey', 42.50, 1),
('shirt', 'ModernFashion', 'shirt white; 90% cotton, 10% padding polyester', 541.10, 3);
"""

select_join_product_and_category = """
SELECT p.name AS name, ct.name AS category, p.manufacturer AS manufacturer, 
p.decryption AS decryption, p.price AS price FROM product AS p
JOIN category AS ct ON p.category_id = ct.id;
"""
