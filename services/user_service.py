from sqlite3 import Connection, IntegrityError
import sqlite3
from utils.database import Database
from exceptions.exception import (
    DuplicateEmailError,
    DuplicateUsernameError,
)

from models.user import User


class UserService:
    def __init__(self, db_connection: Connection):
        self.db_connection = db_connection

    def create_user(self, user: User):
        c = self.db_connection.cursor()

        try:
            c.execute(
                """
                INSERT INTO user (username, password, email, full_name, role_id) 
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    user.username,
                    user.password,
                    user.email,
                    user.full_name,
                    user.role_id,
                ),
            )
            self.db_connection.commit()
            print("User created successfully!")
        except IntegrityError as e:
            error_message = str(e)
            if "UNIQUE constraint failed: user.username" in error_message:
                raise DuplicateUsernameError()
            elif "UNIQUE constraint failed: user.email" in error_message:
                raise DuplicateEmailError("Email is not unique.")
            else:
                print(f"Error creating user: {e}")
        finally:
            c.close()

    def get_user_by_id(self, user_id):
        cursor = self.db_connection.cursor()

        cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        return user

    def updat_user(self, user: User):
        cursor = self.db_connection.cursor()

        try:
            # Update user information in the 'user' table
            cursor.execute(
                """
                UPDATE user
                SET username=?, password=?, email=?, full_name=?, role_id=?
                WHERE user_id=?
            """,
                (
                    user.username,
                    user.password,
                    user.email,
                    user.full_name,
                    user.role_id,
                    user.user_id,
                ),
            )

            # Commit the changes
            self.db_connection.commit()

            print("User updated successfully!")
        except sqlite3.Error as e:
            print(f"Error updating user: {e}")
        finally:
            # Close the database connection
            self.db_connection.close()

    def get_user_by_id(self, id):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
SELECT u.* , r.role_name from User u left join Role r on u.role_id=r.role_id where u.user_id=?
""",
            (id,),
        )
        return User(*cursor.fetchone())

    def get_user_by_username(self, username):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
SELECT u.* , r.role_name from User u left join Role r on u.role_id=r.role_id where u.username=?
""",
            (username,),
        )
        return User(*cursor.fetchone())

    def delete_user(self, id):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
        DELETE FROM User u WHERE u.id=?
""",
            (id,),
        )
        return User(*cursor.fetchone())

    def login(self, username, password):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
SELECT u.* , r.role_name from User u left join Role r on u.role_id=r.role_id where u.username=? and u.password=?
""",
            (username,password),
        )
        result = cursor.fetchone()
        return User(*result) if result is not None else None
