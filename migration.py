from database import Database

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

# Create the admin table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        full_name TEXT
    )
"""
)

# Create the user table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS user (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        full_name TEXT,
        user_type TEXT
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
    "INSERT INTO admin (username, password, email, full_name) VALUES ('admin1', 'adminpassword', 'admin@example.com', 'Admin User')"
)

cursor.execute(
    "INSERT INTO user (username, password, email, full_name, user_type) VALUES ('user1', 'userpassword', 'user1@example.com', 'Regular User', 'Regular')"
)
cursor.execute(
    "INSERT INTO user (username, password, email, full_name, user_type) VALUES ('manager1', 'managerpassword', 'manager@example.com', 'Manager User', 'Manager')"
)

# Commit changes and close the connection
conn.commit()





