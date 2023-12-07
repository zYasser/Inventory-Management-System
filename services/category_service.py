from sqlite3 import Connection


class CategoryService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection
