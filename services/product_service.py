from sqlite3 import Connection

from models.product import BaseProduct, Product


class ProductService:
    def __init__(self, db_connection: Connection) -> [Product]:
        self.db_connection = db_connection

    def get_all_products(self):
        # self.db_connection.row_factory = sqlite3.Row
        cursor = self.db_connection.cursor()

        results = cursor.execute(
            "SELECT p.* , c.CategoryName, s.SupplierName from Product p LEFT join Category c  on c.CategoryID=p.CategoryID LEFT JOIN Supplier s on s.SupplierID=p.SupplierID;"
        ).fetchall()
        list_product = []
        print(results)
        for result in results:
            list_product.append(Product(*result))
        return list_product

    def get_product_by_id(self, product_id: str):
        # self.db_connection.row_factory = sqlite3.Row
        cursor = self.db_connection.cursor()

        result = cursor.execute(
            "SELECT p.* , c.CategoryName, s.SupplierName from Product p LEFT join Category c  on c.CategoryID=p.CategoryID LEFT JOIN Supplier s on s.SupplierID=p.SupplierID WHERE ProductID=?;",
            (product_id,),
        ).fetchone()
        if result is None:
            return None
        return Product(*result)

    def insert_product(self, Product: BaseProduct):
        cursor = self.db_connection.cursor()
        result = cursor.execute(
            "INSERT INTO Product(ProductName, Description, UnitPrice, QuantityInStock, CategoryID , SupplierID) VALUES(? , ? , ? , ? ,? , ? ) RETURNING ProductID",
            (
                Product.product_name,
                Product.description,
                Product.unit_price,
                Product.quantity_in_stock,
                Product.category_id,
                Product.supplier_id,
            ),
        ).fetchone()
        self.db_connection.commit()

        cursor.close()
        return result

    def update_product(self, product: Product):
        """
        Update an existing product in the Product table based on ProductID.
        """
        query = """
            UPDATE Product
            SET ProductName = ?, 
                Description = ?, 
                UnitPrice = ?, 
                QuantityInStock = ?, 
                CategoryID = ?, 
                SupplierID = ?
            WHERE ProductID = ?
            Returning * 
        """

        cursor = self.db_connection.cursor()
        result = cursor.execute(
            query,
            (
                product.product_name,
                product.description,
                product.unit_price,
                product.quantity_in_stock,
                product.category_id,
                product.supplier_id,
                product.product_id,
            ),
        ).fetchone()

        # Commit the changes to the database
        self.db_connection.commit()

        # Close the cursor
        cursor.close()
        return result

    def delete_product(self, product_id) -> bool:
        """
        Update an existing product in the Product table based on ProductID.
        """
        query = (
            """
        DELETE FROM PRODUCT WHERE ProductID=?
        """,
        )

        cursor = self.db_connection.cursor()
        result = cursor.execute(
            query,
            (product_id,),
        )

        # Commit the changes to the database
        self.db_connection.commit()

        # Close the cursor
        cursor.close()
        return True

    d