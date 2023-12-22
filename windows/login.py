import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from models.user import User
from services.user_service import UserService

from utils.center import center_screen_geometry
from utils.database import Database
import CTkMessagebox as msg


class LoginPage(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Login Page")
        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=320,
                window_height=320,
            )
        )
        self.user = None
        self.parent = parent
        self.resizable(0, 0)

        self.lbl1 = None
        self.userName = None
        self.password = None
        self.btn1 = None
        self.info_label = None
        self.user = User()
        self.createWidgets()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def createWidgets(self):
        self.lbl1 = ctk.CTkLabel(
            self, text="Welcome to the login page", font=("Calibri", 16)
        )
        self.lbl1.pack(pady=(20, 0))

        self.userName = ctk.CTkEntry(self, placeholder_text="Username")
        self.userName.pack(pady=(20, 0))

        self.password = ctk.CTkEntry(self, show="*", placeholder_text="Password")
        self.password.pack(pady=(20, 0))
        self.password.bind(
            "<Return>", lambda event: self.login()
        )  # Bind Enter key for login

        self.btn1 = ctk.CTkButton(self, text="Login", command=self.login)
        self.btn1.pack(pady=(20, 0))

        self.info_label = ctk.CTkLabel(self, text="")
        self.info_label.pack(pady=(10, 0))

    def login(self):
        username = self.userName.get()
        password = self.password.get()
        u = UserService(db_connection=Database().get_connection())
        result = u.login(username=username, password=password)
        if result is None:
            msg.CTkMessagebox(
                title="Error",
                message="Please Check Your Username and Password",
                icon="cancel",
            )
            return

        self.user = result
        self.parent.deiconify()
        self.parent.fetch_user(self)
        self.destroy()

    def close_window(self):
        self.parent.destroy()
