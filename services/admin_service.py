from sqlite3 import Connection
import sqlite3

from matplotlib.streamplot import streamplot

from models.admin import Admin


class AdminService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def get_admin(self, id: str):
        # self.db_connection.row_factory = sqlite3.Row
        cursor = self.db_connection.cursor()

        result = cursor.execute("SELECT * FROM ADMIN WHERE AdminId=?", (id)).fetchone()
        if result is None:
            print("NO DATA avaliable ")
            return None

        return Admin(*result)

    def create_admin(self, username, password, email, fullname):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "INSERT INTO ADMIN(username,password,email , fullname) VALUES(? , ? , ? , ?)",
            (username, password, email, fullname),
        )

        return True
