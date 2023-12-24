from sqlite3 import Connection

from models.product import Product

import pandas as pd


class ProductService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def get_all_products(self):
        cursor = self.db_connection.cursor()

        results = cursor.execute(
            """

SELECT * FROM product;

"""
        ).fetchall()
        return results

    def change_stock(self, product_id, stock):
        cursor = self.db_connection.cursor()
        result = cursor.execute(
            "UPDATE Product Set quantity_in_stock=quantity_in_stock + ? Where product_id=?",
            (stock, product_id),
        )

    def get_product_by_id(self, product_id: str):
        cursor = self.db_connection.cursor()

        result = cursor.execute(
            "SELECT * FROM Product p  WHERE Product_ID=?;",
            (product_id,),
        ).fetchone()
        if result is None:
            return None
        return Product(*result)

    def get_product_stock(self, product_id: str):
        cursor = self.db_connection.cursor()

        result = cursor.execute(
            "SELECT p.quantity_in_stock FROM Product p  WHERE Product_ID=?;",
            (product_id,),
        ).fetchone()
        if result is None:
            return None
        return result

    def insert_product(self, product: Product):
        cursor = self.db_connection.cursor()
        result = cursor.execute(
            "INSERT INTO Product(product_name, description, unit_price, quantity_in_stock, category_name, supplier_name) VALUES (?, ?, ?, ?, ?, ?) RETURNING Product_ID",
            (
                product.product_name,
                product.description,
                product.unit_price,
                product.quantity_in_stock,
                product.category_name,
                product.supplier_name,
            ),
        ).fetchone()
        self.db_connection.commit()

        cursor.close()
        return result

    def update_product(self, product: Product):
        query = """
            UPDATE Product
            SET product_name = ?, 
                description = ?, 
                unit_price = ?, 
                quantity_in_stock = ?, 
                category_name = ?, 
                supplier_name = ?
            WHERE Product_ID = ?
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
                product.supplier_name,
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

    def fetch_all_datafram(self):
        return pd.read_sql_query("SELECT * FROM Product", self.db_connection)
