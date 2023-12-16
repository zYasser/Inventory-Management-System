from sqlite3 import Connection

from models.product import BaseProduct, Product


class ProductService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def get_all_products(self):
        cursor = self.db_connection.cursor()

        results = cursor.execute(
            """

SELECT 
    p.Product_ID AS id, 
    p.Product_Name AS name, 
    p.Description, 
    p.Category_Name AS Category, 
    p.Unit_Price AS Price, 
    p.Quantity_In_Stock AS quantity, 
    s.Supplier_Name AS Supplier
FROM Product p 
LEFT JOIN Supplier s ON p.Supplier_ID = s.Supplier_ID;

"""
        ).fetchall()
        return results

    def get_product_by_id(self, product_id: str):
        cursor = self.db_connection.cursor()

        result = cursor.execute(
            "SELECT p.*,s.Supplier_Name FROM Product p LEFT JOIN Supplier s ON s.Supplier_ID = p.Supplier_ID WHERE Product_ID=?;",
            (product_id,),
        ).fetchone()
        if result is None:
            return None
        return result

    def insert_product(self, product: BaseProduct):
        cursor = self.db_connection.cursor()
        result = cursor.execute(
            "INSERT INTO Product(ProductName, Description, UnitPrice, QuantityInStock, CategoryName, SupplierID) VALUES (?, ?, ?, ?, ?, ?) RETURNING ProductID",
            (
                product.product_name,
                product.description,
                product.unit_price,
                product.quantity_in_stock,
                product.category_name,
                product.supplier_id,
            ),
        ).fetchone()
        self.db_connection.commit()

        cursor.close()
        return result

    def update_product(self, product: Product):
        query = """
            UPDATE Product
            SET ProductName = ?, 
                Description = ?, 
                UnitPrice = ?, 
                QuantityInStock = ?, 
                CategoryName = ?, 
                SupplierID = ?
            WHERE ProductID = ?
            RETURNING * 
        """

        cursor = self.db_connection.cursor()
        result = cursor.execute(
            query,
            (
                product.product_name,
                product.description,
                product.unit_price,
                product.quantity_in_stock,
                product.category_name,
                product.supplier_id,
                product.product_id,
            ),
        ).fetchone()

        self.db_connection.commit()
        cursor.close()
        return result

    def delete_product(self, product_id) -> bool:
        query = "DELETE FROM Product WHERE ProductID=?"
        cursor = self.db_connection.cursor()
        result = cursor.execute(query, (product_id,))

        self.db_connection.commit()
        cursor.close()
        return True
