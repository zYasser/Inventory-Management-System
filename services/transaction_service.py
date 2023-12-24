import datetime
from sqlite3 import Connection
from unittest import result


class TransactionService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def add_transaction(
        self, product_id, transaction_type, quantity, total_amount, customer
    ):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
                INSERT INTO transaction_record (customer,Product_ID, Transaction_Type, Transaction_Date, Quantity, Total_Amount)
                VALUES (?, ?, ?, ?, ? , ?)
            """,
            (
                customer,
                product_id,
                transaction_type,
                datetime.datetime.now(),
                quantity,
                total_amount,
            ),
        )
        self.db_connection.commit()

    def get_transaction_by_id(self, transaction_id):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "SELECT * FROM transaction_record WHERE TransactionID=?", (transaction_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_all_transactions(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM transaction_record")
        result = cursor.fetchall()
        cursor.close()
        return result

    def update_transaction(
        transaction_id,
        product_id,
        transaction_type,
        transaction_date,
        quantity,
        total_amount,
        self,
    ):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
                UPDATE transaction_record
                SET ProductID=?, Transaction_Type=?, Transaction_Date=?, Quantity=?, Total_Amount=?
                WHERE TransactionID=?
            """,
            (
                product_id,
                transaction_type,
                transaction_date,
                quantity,
                total_amount,
                transaction_id,
            ),
        )
        self.db_connection.commit()
        cursor.close()

    def delete_transaction(self, transaction_id):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "DELETE FROM transaction_record WHERE Transaction_ID=?", (transaction_id,)
        )
        self.db_connection.commit()
        cursor.close()

    def get_transaction_by_type(self, type):
        cursor = self.db_connection.cursor()
        res = cursor.execute(
            """
    SELECT p.product_name, t.Transaction_ID, t.customer, t.Transaction_Type, t.Transaction_Date, t.Quantity, t.Total_Amount FROM transaction_record t Left JOIN Product p on t.product_id=p.product_id WHERE Transaction_Type=?; 
""",
            (type,),
        ).fetchall()
        cursor.close()
        return res
