from database import Database


"""
Only run it for 1 time, running it more than one time will create redundant data
"""


conn = Database.get_connection()

cursor = conn.cursor()

# Create the Category table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Category (
        CategoryID INTEGER PRIMARY KEY,
        CategoryName TEXT NOT NULL
    )
"""
)

# Create the Supplier table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Supplier (
        SupplierID INTEGER PRIMARY KEY,
        SupplierName TEXT NOT NULL,
        ContactPerson TEXT,
        ContactNumber TEXT,
        Email TEXT
    )
"""
)

# Create the Product table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Product (
        ProductID INTEGER PRIMARY KEY,
        ProductName TEXT NOT NULL,
        Description TEXT,
        UnitPrice DECIMAL(10, 2) NOT NULL,
        QuantityInStock INTEGER NOT NULL,
        CategoryID INTEGER,
        SupplierID INTEGER,
        FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
        FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
    )
"""
)

# Create the TransactionRecord table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TransactionRecord (
        TransactionID INTEGER PRIMARY KEY,
        ProductID INTEGER,
        TransactionType TEXT NOT NULL,
        TransactionDate DATE NOT NULL,
        Quantity INTEGER NOT NULL,
        TotalAmount DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
    )
"""
)
# Create the Admin table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Admin (
        AdminID INTEGER PRIMARY KEY,
        Username TEXT NOT NULL,
        Password TEXT NOT NULL,
        Email TEXT,
        FullName TEXT
    )
"""
)
insert_statements = [
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Sauce Tomato Pouch', 'Shrimp - 21/25, Peel And Deviened', 670.75, 22, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Mushroom - Enoki, Dry', 'Green Scrubbie Pad H.duty', 47.82, 16, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Nut - Pecan, Pieces', 'Cups 10oz Trans', 487.61, 31, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Chicken - Base', 'Squash - Guords', 77.67, 36, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Jolt Cola - Electric Blue', 'Energy Drink Bawls', 256.06, 24, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Muffin - Blueberry Individual', 'Pastry - Carrot Muffin - Mini', 67.99, 91, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Taro Leaves', 'Coffee - Colombian, Portioned', 185.13, 41, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Lamb - Rack', 'Sauce - Salsa', 845.49, 41, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Cabbage - Nappa', 'Beer - Labatt Blue', 257.9, 50, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Lobster - Tail 6 Oz', 'Tomatoes Tear Drop', 580.52, 39, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Fruit Mix - Light', 'Wine - Jackson Triggs Okonagan', 524.27, 91, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Milk - Chocolate 500ml', 'Syrup - Kahlua Chocolate', 785.67, 33, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Chips Potato Swt Chilli Sour', 'Temperature Recording Station', 517.96, 58, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Ham - Procutinni', 'Table Cloth 62x114 Colour', 312.26, 19, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Apple - Granny Smith', 'Vodka - Hot, Lnferno', 947.39, 33, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Veal - Slab Bacon', 'Tomatillo', 453.34, 51, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Cream - 10%', 'Sherbet - Raspberry', 605.35, 84, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Beef - Short Loin', 'Orange - Blood', 975.61, 85, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Flower - Dish Garden', 'Spice - Onion Powder Granulated', 468.55, 20, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Jam - Apricot', 'Flower - Carnations', 825.66, 90, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Yogurt - Raspberry, 175 Gr', 'Lentils - Green Le Puy', 675.69, 32, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Pasta - Canelloni', 'Water - Aquafina Vitamin', 223.39, 78, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Okra', 'Muffin Batt - Ban Dream Zero', 444.51, 33, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Uniform Linen Charge', 'Longos - Penne With Pesto', 488.41, 48, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Dc - Sakura Fu', 'The Pop Shoppe - Lime Rickey', 439.57, 82, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Potatoes - Fingerling 4 Oz', 'Peach - Halves', 541.0, 55, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Wine - Cahors Ac 2000, Clos', 'Beer - Steamwhistle', 325.76, 58, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Lobster - Base', 'Tea - Vanilla Chai', 696.73, 98, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Nantuket Peach Orange', 'Beer - Sleemans Cream Ale', 991.92, 53, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Oil - Peanut', 'Corn - On The Cob', 783.46, 93, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Chicken - Whole Fryers', 'Pork - Tenderloin, Fresh', 581.64, 97, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Lemonade - Natural, 591 Ml', 'Chilli Paste, Hot Sambal Oelek', 850.86, 91, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Bread - Flat Bread', 'Steampan - Lid For Half Size', 161.72, 95, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Juice - Clamato, 341 Ml', 'Red Pepper Paste', 558.33, 43, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Cake - Pancake', 'Blackberries', 223.4, 54, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Steel Wool', 'Gooseberry', 661.9, 54, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Soup - Cream Of Broccoli', 'Stock - Veal, White', 60.24, 3, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Juice - Prune', 'Carrots - Mini Red Organic', 342.38, 36, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Cheese - Cambozola', 'Soup - Campbellschix Stew', 849.69, 7, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Ecolab - Hand Soap Form Antibac', 'Mushroom - Crimini', 607.58, 8, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Water - San Pellegrino', 'Kaffir Lime Leaves', 249.99, 25, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Flour - Bread', 'Pomello', 827.3, 20, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Nut - Hazelnut, Whole', 'Turkey - Breast, Boneless Sk On', 214.88, 31, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Wine - Red, Pinot Noir, Chateau', 'Wine - Fontanafredda Barolo', 920.51, 47, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Silicone Paper 16.5x24', 'Wine - Zinfandel Rosenblum', 19.45, 48, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Extract - Lemon', 'Sprouts - Onion', 685.15, 14, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Chicken - Whole Roasting', 'Wine - Chateau Bonnet', 469.62, 28, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Beans - Soya Bean', 'Wine - Rioja Campo Viejo', 957.37, 44, 3);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Wine - Bourgogne 2002, La', 'Eggplant - Baby', 673.46, 52, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Ham - Virginia', 'Pasta - Fusili Tri - Coloured', 586.74, 84, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Olive Oil - Extra Virgin', 'Cheese - Mix', 531.76, 19, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Sunflower Seed Raw', 'Sugar - Sweet N Low, Individual', 237.91, 80, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Wine - White, French Cross', 'Lemonade - Natural, 591 Ml', 161.7, 32, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Bacardi Breezer - Strawberry', 'Napkin White - Starched', 591.69, 9, 1);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Lamb - Shoulder, Boneless', 'Beets - Mini Golden', 946.34, 75, 2);",
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID) VALUES ('Brandy - Bar', 'Cheese - Roquefort Pappillon', 654.91, 78, 2);",
]


# Create the User table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS User (
        UserID INTEGER PRIMARY KEY,
        Username TEXT NOT NULL,
        Password TEXT NOT NULL,
        Email TEXT,
        FullName TEXT,
        UserType TEXT
    )
"""
)
cursor.execute("INSERT INTO Category (CategoryName) VALUES ('Electronics')")
cursor.execute("INSERT INTO Category (CategoryName) VALUES ('Clothing')")
cursor.execute("INSERT INTO Category (CategoryName) VALUES ('Furniture')")
for i in insert_statements[:]:
    cursor.execute(i)
cursor.execute(
    "INSERT INTO Supplier (SupplierName, ContactPerson, ContactNumber, Email) VALUES ('SupplierA', 'John Doe', '123-456-7890', 'supplierA@example.com')"
)
cursor.execute(
    "INSERT INTO Supplier (SupplierName, ContactPerson, ContactNumber, Email) VALUES ('SupplierB', 'Jane Smith', '987-654-3210', 'supplierB@example.com')"
)
cursor.execute(
    "INSERT INTO Supplier (SupplierName, ContactPerson, ContactNumber, Email) VALUES ('SupplierC', 'Bob Johnson', '111-222-3333', 'supplierC@example.com')"
)

cursor.execute(
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID, SupplierID) VALUES ('Laptop', 'High-performance laptop', 1200.00, 50, 1, 1)"
)
cursor.execute(
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID, SupplierID) VALUES ('T-Shirt', 'Cotton T-Shirt', 15.99, 100, 2, 2)"
)
cursor.execute(
    "INSERT INTO Product (ProductName, Description, UnitPrice, QuantityInStock, CategoryID, SupplierID) VALUES ('Sofa', 'Comfortable sofa', 499.99, 20, 3, 3)"
)

cursor.execute(
    "INSERT INTO TransactionRecord (ProductID, TransactionType, TransactionDate, Quantity, TotalAmount) VALUES (1, 'Purchase', '2023-01-15', 10, 12000.00)"
)
cursor.execute(
    "INSERT INTO TransactionRecord (ProductID, TransactionType, TransactionDate, Quantity, TotalAmount) VALUES (2, 'Sale', '2023-02-20', 5, 79.95)"
)
cursor.execute(
    "INSERT INTO TransactionRecord (ProductID, TransactionType, TransactionDate, Quantity, TotalAmount) VALUES (3, 'Purchase', '2023-03-10', 2, 999.98)"
)
cursor.execute(
    "INSERT INTO Admin (Username, Password, Email, FullName) VALUES ('admin1', 'adminpassword', 'admin@example.com', 'Admin User')"
)

cursor.execute(
    "INSERT INTO User (Username, Password, Email, FullName, UserType) VALUES ('user1', 'userpassword', 'user1@example.com', 'Regular User', 'Regular')"
)
cursor.execute(
    "INSERT INTO User (Username, Password, Email, FullName, UserType) VALUES ('manager1', 'managerpassword', 'manager@example.com', 'Manager User', 'Manager')"
)


# Commit changes and close the connection
conn.commit()
