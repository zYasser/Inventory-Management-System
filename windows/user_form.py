import customtkinter as ctk
from models.user import User
from utils.center import center_screen_geometry


class UserForm(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("User Form")
        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=300,
                window_height=350,
            )
        )
        # Create labels and entry widgets for each attribute
        labels = [
            "Username:",
            "Password:",
            "Email:",
            "Full Name:",
        ]
        self.entries = {}

        for row, label in enumerate(labels):
            ctk.CTkLabel(self, text=label).grid(
                row=row, column=0, sticky="w", pady=10, padx=20
            )
            entry = ctk.CTkEntry(self)
            entry.grid(row=row, column=1, sticky="e", padx=20, pady=10)
            self.entries[label] = entry

        # Create radio buttons for role
        ctk.CTkLabel(self, text="Role:").grid(
            row=len(labels), column=0, sticky="w", pady=10, padx=20
        )
        self.role_var = ctk.StringVar(value="User")
        ctk.CTkRadioButton(
            self, text="User", variable=self.role_var, value="User"
        ).grid(row=len(labels), column=1, sticky="w", pady=10, padx=20)
        ctk.CTkRadioButton(
            self, text="Admin", variable=self.role_var, value="Admin"
        ).grid(row=len(labels) + 1, column=1, sticky="w", pady=10, padx=20)

        # Create a submit button
        ctk.CTkButton(self, text="Submit", command=self.submit_form).grid(
            row=len(labels) + 2, column=1, pady=10
        )

    def submit_form(self):
        # Retrieve values from the entry widgets and radio buttons
        values = {label: entry.get() for label, entry in self.entries.items()}
        values["role"] = self.role_var.get()
        print(values)
        # Create a User object with the retrieved values
        user = User(
            username=values["Username:"],
            password=values["Password:"],
            email=values["Email:"],
            full_name=values["Full Name:"],
            role=values["role"],
        )

        # Print the User object for demonstration purposes (replace with your desired logic)
        print(user)
