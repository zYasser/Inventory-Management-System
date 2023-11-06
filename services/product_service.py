from sqlite3 import Connection

from models.product import Product


class ProductService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def get_all_products(self):
        # self.db_connection.row_factory = sqlite3.Row
        cursor = self.db_connection.cursor()

        results = cursor.execute(
            "SELECT p.* , c.CategoryName, s.SupplierName from Product p LEFT join Category c  on c.CategoryID=p.CategoryID JOIN Supplier s "
        ).fetchall()
        list_product = []
        print(results)
        for result in results:
            list_product.append(Product(*result))
