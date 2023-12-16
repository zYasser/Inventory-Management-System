from sqlite3 import Connection
from unittest import result


class TransicationService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def add_transaction(
        self, product_id, transaction_type, transaction_date, quantity, total_amount
    ):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
                INSERT INTO TransactionRecord (ProductID, TransactionType, TransactionDate, Quantity, TotalAmount)
                VALUES (?, ?, ?, ?, ?)
            """,
            (product_id, transaction_type, transaction_date, quantity, total_amount),
        )
        self.db_connection.commit()

    def get_transaction_by_id(self, transaction_id):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "SELECT * FROM TransactionRecord WHERE TransactionID=?", (transaction_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_all_transactions(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM TransactionRecord")
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
                UPDATE TransactionRecord
                SET ProductID=?, TransactionType=?, TransactionDate=?, Quantity=?, TotalAmount=?
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
            "DELETE FROM TransactionRecord WHERE TransactionID=?", (transaction_id,)
        )
        self.db_connection.commit()
        cursor.close()
