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

        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=320,
                window_height=320,
            )
        )
        self.lang_dict = {
            "en": {
                "welcome": "Welcome to the login page",
                "username": "Username",
                "password": "Password",
                "login": "Login",
                "submit": "Submit",
                "user_exists": "User already exists!",
                "login_failed": "Please Make Sure You Entered Username and Password Correctly!",
                "error": "Error",
            },
            "ar": {
                "welcome": "مرحبًا بك في صفحة الدخول",
                "username": "المستخدم اسم",
                "password": "المرور كلمة",
                "login": "الدخول تسجيل",
                "submit": "إرسال",
                "user_exists": "المستخدم موجود بالفعل!",
                "login_failed": "!صحيح بشكل السر كلمة المستخدم اسم ادخلت انك التحقق الرجاء",
                "error": "Error",
            },
        }

        self.language_var = tk.StringVar()
        self.language_var.set("English")
        self.language_var.trace("w", self.switch_language)

        self.current_lang = "en"  # Default language
        self.title(self.lang_dict[self.current_lang]["login"])

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
            self,
            text=self.lang_dict[self.current_lang]["welcome"],
            font=("Calibri", 16),
        )
        self.lbl1.pack(pady=(20, 0))

        self.userName = ctk.CTkEntry(
            self, placeholder_text=self.lang_dict[self.current_lang]["username"]
        )
        self.userName.pack(pady=(20, 0))

        self.password = ctk.CTkEntry(
            self,
            show="*",
            placeholder_text=self.lang_dict[self.current_lang]["password"],
        )
        self.password.pack(pady=(20, 0))
        self.password.bind("<Return>", lambda event: self.login())

        self.btn1 = ctk.CTkButton(
            self,
            text=self.lang_dict[self.current_lang]["login"],
            command=self.login,
        )
        self.btn1.pack(pady=(20, 0))

        self.info_label = ctk.CTkLabel(self, text="")
        self.info_label.pack(pady=(10, 0))

        # ComboBox for lang switching
        self.language_combobox = ctk.CTkComboBox(
            self, values=["English", "العربية"], variable=self.language_var
        )
        self.language_combobox.pack(pady=(10, 0))

    def switch_language(self, *args):
        selected_language = self.language_var.get()
        self.current_lang = "ar" if selected_language == "العربية" else "en"
        self.update_language()

    def update_language(self):
        self.lbl1.configure(text=self.lang_dict[self.current_lang]["welcome"])
        self.userName.configure(
            placeholder_text=self.lang_dict[self.current_lang]["username"]
        )
        self.password.configure(
            placeholder_text=self.lang_dict[self.current_lang]["password"]
        )
        self.btn1.configure(text=self.lang_dict[self.current_lang]["login"])
        self.title(self.lang_dict[self.current_lang]["login"])

    def login(self):
        username = self.userName.get()
        password = self.password.get()
        u = UserService(db_connection=Database().get_connection())
        result = u.login(username=username, password=password)
        if result is None:
            msg.CTkMessagebox(
                title=self.lang_dict[self.current_lang]["error"],
                message=self.lang_dict[self.current_lang]["login_failed"],
                icon="cancel",
                width=530,
            )
            return

        self.user = result
        self.parent.deiconify()
        self.parent.fetch_user(self)
        self.destroy()

    def close_window(self):
        self.parent.destroy()
