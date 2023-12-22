from utils.database import Database

# Only run it for 1 time, running it more than one time will create redundant data

conn = Database.get_connection()
cursor = conn.cursor()

# Create the supplier table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS supplier (
        supplier_id INTEGER PRIMARY KEY,
        supplier_name TEXT NOT NULL,
        contact_person TEXT,
        contact_number TEXT,
        email TEXT
    )
"""
)

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
        supplier_id INTEGER,
        FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
    )
"""
)

# Create the transaction_record table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS transaction_record (
        transaction_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        transaction_type TEXT NOT NULL,
        transaction_date DATE NOT NULL,
        quantity INTEGER NOT NULL,
        total_amount DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (product_id) REFERENCES product(product_id)
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


cursor.execute(
    "INSERT INTO supplier (supplier_name, contact_person, contact_number, email) VALUES ('SupplierA', 'John Doe', '123-456-7890', 'supplierA@example.com')"
)
cursor.execute(
    "INSERT INTO supplier (supplier_name, contact_person, contact_number, email) VALUES ('SupplierB', 'Jane Smith', '987-654-3210', 'supplierB@example.com')"
)
cursor.execute(
    "INSERT INTO supplier (supplier_name, contact_person, contact_number, email) VALUES ('SupplierC', 'Bob Johnson', '111-222-3333', 'supplierC@example.com')"
)

cursor.execute(
    "INSERT INTO product (product_name, description, unit_price, quantity_in_stock, category_name, supplier_id) VALUES ('Laptop', 'High-performance laptop', 1200.00, 50, 'Electronics', 1)"
)
cursor.execute(
    "INSERT INTO product (product_name, description, unit_price, quantity_in_stock, category_name, supplier_id) VALUES ('T-Shirt', 'Cotton T-Shirt', 15.99, 100, 'Clothing', 2)"
)
cursor.execute(
    "INSERT INTO product (product_name, description, unit_price, quantity_in_stock, category_name, supplier_id) VALUES ('Sofa', 'Comfortable sofa', 499.99, 20, 'Furniture', 3)"
)

cursor.execute(
    "INSERT INTO transaction_record (product_id, transaction_type, transaction_date, quantity, total_amount) VALUES (1, 'Purchase', '2023-01-15', 10, 12000.00)"
)
cursor.execute(
    "INSERT INTO transaction_record (product_id, transaction_type, transaction_date, quantity, total_amount) VALUES (2, 'Sale', '2023-02-20', 5, 79.95)"
)
cursor.execute(
    "INSERT INTO transaction_record (product_id, transaction_type, transaction_date, quantity, total_amount) VALUES (3, 'Purchase', '2023-03-10', 2, 999.98)"
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


# Commit changes and close the connection
conn.commit()
