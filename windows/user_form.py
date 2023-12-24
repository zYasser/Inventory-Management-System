import tkinter as tk
import customtkinter as ctk
from exceptions.exception import DuplicateEmailError, DuplicateUsernameError
from models.user import User
from services.user_service import UserService
from utils.center import center_screen_geometry
from utils.database import Database
import CTkMessagebox as msg


class UserForm(ctk.CTkToplevel):
    def __init__(self, parent, lan, title):
        super().__init__(parent)

        self.title(title)
        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=300,
                window_height=350,
            )
        )
        self.msg = {}
        self.entries = {}
        self.role_var = ctk.StringVar(value="User")
        # Initialize the translation dictionary
        self.translation_dict = {
            "Error": "خطأ",
            "email": "البريد الإلكتروني موجود بالفعل",
            "username": "اسم المستخدم موجود بالفعل",
            "Done": "تم إنشاء الحساب بنجاح",
            "err": "تعذر انشاء الحساب",
        }

        # Initialize the msg dictionary with English messages
        self.msg = {
            "Error": "Error",
            "email": "Email Already Exist",
            "username": "Username Already Exist",
            "Done": "Account Has Been Created Successfully",
            "err": "Something Went Wrong",
        }

        print(lan)
        if lan == "English":
            self.lan = "en"
            self.create_widget_en()
        else:
            self.create_widget_ar()
            self.set_language("ar")

    def set_language(self, language):
        # Set the language and update the msg dictionary with translated values
        if language == "ar":
            self.msg = {key: self.translation_dict[key] for key in self.msg}

    def create_widget_en(self):
        # Label and Entry for "Username"
        ctk.CTkLabel(self, text="Username:").grid(
            row=0, column=0, sticky="w", pady=10, padx=20
        )
        entry_username = ctk.CTkEntry(self)
        entry_username.grid(row=0, column=1, sticky="e", padx=20, pady=10)
        self.entries["Username:"] = entry_username

        # Label and Entry for "Password"
        ctk.CTkLabel(self, text="Password:").grid(
            row=1, column=0, sticky="w", pady=10, padx=20
        )
        entry_password = ctk.CTkEntry(self)
        entry_password.grid(row=1, column=1, sticky="e", padx=20, pady=10)
        self.entries["Password:"] = entry_password

        # Label and Entry for "Email"
        ctk.CTkLabel(self, text="Email:").grid(
            row=2, column=0, sticky="w", pady=10, padx=20
        )
        entry_email = ctk.CTkEntry(self)
        entry_email.grid(row=2, column=1, sticky="e", padx=20, pady=10)
        self.entries["Email:"] = entry_email

        # Label and Entry for "Full Name"
        ctk.CTkLabel(self, text="Full Name:").grid(
            row=3, column=0, sticky="w", pady=10, padx=20
        )
        entry_full_name = ctk.CTkEntry(self)
        entry_full_name.grid(row=3, column=1, sticky="e", padx=20, pady=10)
        self.entries["Full Name:"] = entry_full_name

        # Create a submit button
        ctk.CTkButton(self, text="Submit", command=self.submit_form).grid(
            row=7, column=1, pady=10
        )
        # Create radio buttons for role
        ctk.CTkLabel(self, text="Role:").grid(
            row=4, column=0, sticky="w", pady=10, padx=20
        )

        ctk.CTkRadioButton(
            self, text="User", variable=self.role_var, value="User"
        ).grid(row=4, column=1, sticky="w", pady=10, padx=20)
        ctk.CTkRadioButton(
            self, text="Admin", variable=self.role_var, value="Admin"
        ).grid(row=5, column=1, sticky="w", pady=10, padx=20)
        self.msg["Error"] = "Error"
        self.msg["email"] = "Email Already Exist"
        self.msg["username"] = "Username Already Exist"
        self.msg["Done"] = "Account Has Been Created Successfully "

    def create_widget_ar(self):
        # Label and Entry for "اسم المستخدم"
        ctk.CTkLabel(self, text="اسم المستخدم:").grid(
            row=0, column=0, sticky="w", pady=10, padx=20
        )
        entry_username = ctk.CTkEntry(self)
        entry_username.grid(row=0, column=1, sticky="e", padx=20, pady=10)
        self.entries["Username:"] = entry_username

        # Label and Entry for "كلمة المرور"
        ctk.CTkLabel(self, text="كلمة المرور:").grid(
            row=1, column=0, sticky="w", pady=10, padx=20
        )
        entry_password = ctk.CTkEntry(self)
        entry_password.grid(row=1, column=1, sticky="e", padx=20, pady=10)
        self.entries["Password:"] = entry_password

        # Label and Entry for "البريد الإلكتروني"
        ctk.CTkLabel(self, text="البريد الإلكتروني:").grid(
            row=2, column=0, sticky="w", pady=10, padx=20
        )
        entry_email = ctk.CTkEntry(self)
        entry_email.grid(row=2, column=1, sticky="e", padx=20, pady=10)
        self.entries["Email:"] = entry_email

        # Label and Entry for "الاسم الكامل"
        ctk.CTkLabel(self, text="الاسم الكامل:").grid(
            row=3, column=0, sticky="w", pady=10, padx=20
        )
        entry_full_name = ctk.CTkEntry(self)
        entry_full_name.grid(row=3, column=1, sticky="e", padx=20, pady=10)
        self.entries["Full Name:"] = entry_full_name

        # Create a submit button
        ctk.CTkButton(self, text="تقديم", command=self.submit_form).grid(
            row=7, column=1, pady=10
        )
        ctk.CTkLabel(self, text="الرتبة").grid(
            row=4, column=0, sticky="w", pady=10, padx=20
        )

        ctk.CTkRadioButton(
            self, text="مستخدم", variable=self.role_var, value="User"
        ).grid(row=4, column=1, sticky="w", pady=10, padx=20)
        ctk.CTkRadioButton(
            self, text="مدير", variable=self.role_var, value="Admin"
        ).grid(row=5, column=1, sticky="w", pady=10, padx=20)

    def submit_form(self):
        # Retrieve values from the entry widgets and radio buttons
        values = {label: entry.get() for label, entry in self.entries.items()}
        values["role"] = self.role_var.get()
        # Create a User object with the retrieved values
        user = User(
            username=values["Username:"],
            password=values["Password:"],
            email=values["Email:"],
            full_name=values["Full Name:"],
            role=values["role"],
        )
        try:
            UserService(Database().get_connection()).create_user(user)
            msg.CTkMessagebox(icon="info", message=self.msg["Done"])
        except DuplicateUsernameError as e:
            msg.CTkMessagebox(
                icon="cancel", title=self.msg["Error"], message=self.msg["username"]
            )
        except DuplicateEmailError as e:
            msg.CTkMessagebox(
                icon="cancel", title=self.msg["Error"], message=self.msg["email"]
            )

        except Exception as e:
            msg.CTkMessagebox(
                icon="cancel", title=self.msg["Error"], message=self.msg["err"]
            )
