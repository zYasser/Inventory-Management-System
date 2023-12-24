import os
from utils.database import Database


def create_database():
    exist = True
    # Only run it for 1 time, running it more than one time will create redundant data
    if not os.path.exists("inventory.db"):
        exist = False
    conn = Database.get_connection()
    cursor = conn.cursor()

    # Create the product table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            description TEXT,
            unit_price DECIMAL(10, 2) NOT NULL,
            quantity_in_stock INTEGER NOT NULL,
            category_name TEXT,
            supplier_name text not null
        )
    """
    )

    # Create  ttheransaction_record table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transaction_record (
            transaction_id INTEGER PRIMARY KEY,
            customer TEXT NOT NULL,
            product_id INTEGER,
            transaction_type TEXT NOT NULL,
            transaction_date DATE NOT NULL,
            quantity INTEGER NOT NULL,
            total_amount DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE
            
        )
    """
    )
    # Create the user table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT UNIQUE,
            full_name TEXT,
            role_id INTEGER,  -- This column will be used to connect to the role table
            FOREIGN KEY (role_id) REFERENCES role(role_id)  -- Establishing a foreign key relationship
        )
    """
    )

    # Create the role table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS role (
            role_id INTEGER PRIMARY KEY,
            role_name TEXT NOT NULL
        )
    """
    )
    if not exist:
        create_data(cursor=cursor)
    # Commit changes and close the connection
    conn.commit()


def create_data(cursor):
    cursor.execute(
        "INSERT INTO product (product_name, description, unit_price, quantity_in_stock, category_name, supplier_name) VALUES ('Laptop', 'High-performance laptop', 1200.00, 50, 'Electronics', 'Se23')"
    )
    cursor.execute(
        "INSERT INTO product (product_name, description, unit_price, quantity_in_stock, category_name, supplier_name) VALUES ('T-Shirt', 'Cotton T-Shirt', 15.99, 100, 'Clothing', 'kdwd')"
    )
    cursor.execute(
        "INSERT INTO product (product_name, description, unit_price, quantity_in_stock, category_name, supplier_name) VALUES ('Sofa', 'Comfortable sofa', 499.99, 20, 'Furniture', 'qkcw')"
    )

    cursor.execute(
        "INSERT INTO transaction_record (product_id, customer, transaction_type, transaction_date, quantity, total_amount) VALUES (1, 'customer','sell', '2023-01-15', 10, 12000.00)"
    )
    cursor.execute(
        "INSERT INTO transaction_record (product_id,customer, transaction_type, transaction_date, quantity, total_amount) VALUES (2, 'customer','buy', '2023-02-20', 5, 79.95)"
    )
    cursor.execute(
        "INSERT INTO transaction_record (product_id,customer, transaction_type, transaction_date, quantity, total_amount) VALUES (3,'customer3', 'buy', '2023-03-10', 2, 999.98)"
    )
    cursor.execute(
        """
                INSERT INTO role (role_name) VALUES ('user')
            """
    )

    cursor.execute(
        """
                INSERT INTO role (role_name) VALUES ('admin')
            """
    )
    # Insert users into the user table
    cursor.execute(
        """
                INSERT INTO user (username, password, email, full_name,  role_id) 
                VALUES ('user1', 'password1', 'user1@example.com', 'User One',  1)
            """
    )

    cursor.execute(
        """
                INSERT INTO user (username, password, email, full_name,  role_id) 
                VALUES ('user2', 'password2', 'user2@example.com', 'User Two',  1)
            """
    )

    cursor.execute(
        """
                INSERT INTO user (username, password, email, full_name,  role_id) 
                VALUES ('admin1', 'adminpass1', 'admin1@example.com',  'admin', 2)
            """
    )
