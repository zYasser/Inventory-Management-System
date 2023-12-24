from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
from services.transaction_service import TransactionService

from utils.center import center_screen_geometry
from utils.database import Database


class TransactionWin(ctk.CTkToplevel):
    def __init__(self, lan, transaction, parent, type):
        super().__init__(parent)
        self.transaction = transaction
        self.title(transaction)
        self.type = type
        ctk.CTkLabel(self, text=self.transaction).pack(pady="50", padx="500")
        self.lan = lan
        self.lang_dict = {
            "en": {
                "Transaction ID": "Transaction ID",
                "Product Name": "Product Name",
                "Transaction Type": "Transaction Type",
                "Transaction Date": "Transaction Date",
                "Quantity": "Quantity",
                "Total Amount": "Total Amount",
                "Customer": "Customer",
            },
            "ar": {
                "Transaction ID": "رقم العملية",
                "Product Name": "أسم المنتج",
                "Transaction Type": "نوع العملية",
                "Transaction Date": "تاريخ العملية",
                "Quantity": "الكمية",
                "Total Amount": "المبلغ الإجمالي",
                "Customer": "العميل",
                
            },
        }
        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=1250,
                window_height=500,
            )
        )

        self.create_treeview()
        self.fetch()

    def create_treeview(self):
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=50, pady=30)
        self.tree = ttk.Treeview(
            frame,
            columns=(
                "Product Name",
                "ID",
                "Customer",
                "Type",
                "Date",
                "Quantity",
                "Amount",
            ),
            show="headings",
        )

        # Define column headings
        self.tree.heading("Product Name", text=self.lang_dict[self.lan]["Product Name"])
        self.tree.heading("ID", text=self.lang_dict[self.lan]["Transaction ID"])
        self.tree.heading("Customer", text=self.lang_dict[self.lan]["Customer"])
        self.tree.heading("Type", text=self.lang_dict[self.lan]["Transaction Type"])
        self.tree.heading("Date", text=self.lang_dict[self.lan]["Transaction Date"])
        self.tree.heading("Quantity", text=self.lang_dict[self.lan]["Quantity"])
        self.tree.heading("Amount", text=self.lang_dict[self.lan]["Total Amount"])
        # Add vertical scrollbar
        yscrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        yscrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=yscrollbar.set)

        # Add horizontal scrollbar
        xscrollbar = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        xscrollbar.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=xscrollbar.set)

        self.tree.pack(
            expand=True,
            fill="both",
        )

    def fetch(self):
        print(self.type)
        result = TransactionService(
            Database().get_connection()
        ).get_transaction_by_type(self.type)
        for i in result:
            self.tree.insert(parent="", index="end", values=i)
