from sqlite3 import Connection


class CategoryService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def insert_category(self, category_name):
        c = self.db_connection.cursor()

        c.execute(
            """
            INSERT INTO Category (CategoryName)
            VALUES (?)
        """,
            (category_name),
        )

        self.db_connection.commit()
        c.close()

    def update_category(self, category_id, new_category_name):
        c = self.db_connection.cursor()

        c.execute(
            """
            UPDATE Category
            SET CategoryName = ?
            WHERE CategoryID = ?
        """,
            (new_category_name, category_id),
        )

        self.db_connection.commit()
        c.close()

    def delete_category(self, category_id):
        c = self.db_connection.cursor()

        c.execute(
            """
            DELETE FROM Category
            WHERE CategoryID = ?
        """,
            (category_id,),
        )

        self.db_connection.commit()
        c.close()
        return True

    def get_category_by_id(self, category_id):
        c = self.db_connection.cursor()

        c.execute(
            """
            SELECT * FROM Category
            WHERE CategoryID = ?
        """,
            (category_id,),
        )

        category = c.fetchone()

        c.close()

        return category

    def get_all_categories(self):
        c = self.db_connection.cursor()

        c.execute(
            """
            SELECT * FROM Category
        """
        )

        categories = c.fetchall()

        c.close()

        return categories
