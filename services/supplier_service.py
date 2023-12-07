from sqlite3 import Connection
from models.supplier import Supplier


class SupplierService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def add_supplier(self, supplier):
        cursor = self.db_connection.cursor()

        cursor.execute(
            """
            INSERT INTO Supplier ( SupplierName, ContactPerson, ContactNumber, Email)
            VALUES (?, ?, ?, ?)
        """,
            (
                supplier.supplier_name,
                supplier.contact_person,
                supplier.contact_number,
                supplier.email,
            ),
        )
        self.db_connection.commit()
        return True

    def get_supplier_by_id(self, supplier_id):
        cursor = self.db_connection.cursor()

        cursor.execute("SELECT * FROM Supplier WHERE SupplierID = ?", (supplier_id,))
        result = cursor.fetchone()
        if result:
            print("ggg")
            return Supplier(*result)
        else:
            return None

    def get_all_suppliers(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM Supplier")
        results = cursor.fetchall()
        suppliers = [Supplier(*result) for result in results]
        return suppliers

    def update_supplier(self, supplier):
        cursor = self.db_connection.cursor()

        cursor.execute(
            """
            UPDATE Supplier
            SET SupplierName=?, ContactPerson=?, ContactNumber=?, Email=?
            WHERE SupplierID=?
        """,
            (
                supplier.supplier_name,
                supplier.contact_person,
                supplier.contact_number,
                supplier.email,
                supplier.supplier_id,
            ),
        )
        self.db_connection.commit()

    def delete_supplier(self, id):
        cursor = self.db_connection.cursor()

        cursor.execute(
            """
            DELETE FROM Supplier
            WHERE SupplierID=?
        """,
            (id),
        )
        self.db_connection.commit()
