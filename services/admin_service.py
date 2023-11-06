from sqlite3 import Connection
import sqlite3

from models.admin import Admin


class AdminService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def getAdmin(self):
        # self.db_connection.row_factory = sqlite3.Row
        cursor = self.db_connection.cursor()

        result = cursor.execute("SELECT * FROM ADMIN WHERE Username=34343").fetchone()
        if result is None:
            print("NO DATA avaliable ")
            return
        print("There's Data ")
