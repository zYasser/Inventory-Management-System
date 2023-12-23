import customtkinter as ctk
import tkinter as tk
import sqlite3

from models.product import Product
from models.transaction import Transaction
from services.product_service import ProductService
from services.transaction_service import TransactionService
from utils.database import Database

import CTkMessagebox as msg


class addProductWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Inventory Page")
        self.geometry("300x400+700+300")
        self.resizable(0, 0)
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.createWidgets()

    def createWidgets(self):
        self.nameLabel = ctk.CTkLabel(self, text="Item Name:", text_color="black")
        self.nameLabel.grid(row=0, column=0, padx=(5, 10), pady=10)
        self.descriptionLabel = ctk.CTkLabel(
            self, text="Item Description:", text_color="black"
        )
        self.descriptionLabel.grid(row=1, column=0, padx=(5, 10), pady=10)
        self.categoryLabel = ctk.CTkLabel(
            self, text="Item Category:", text_color="black"
        )
        self.categoryLabel.grid(row=2, column=0, padx=(5, 10), pady=10)
        self.priceLabel = ctk.CTkLabel(self, text="Item Price:", text_color="black")
        self.priceLabel.grid(row=3, column=0, padx=(5, 10), pady=10)
        self.quantityLabel = ctk.CTkLabel(
            self, text="Item Quantity:", text_color="black"
        )
        self.quantityLabel.grid(row=4, column=0, padx=(5, 10), pady=10)
        self.supplierLabel = ctk.CTkLabel(self, text="Supplier:", text_color="black")
        self.supplierLabel.grid(row=5, column=0, padx=(5, 10), pady=10)

        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Name")
        self.nameEntry.grid(row=0, column=1, padx=(0, 10), pady=10)
        self.descriptionEntry = ctk.CTkEntry(self, placeholder_text="Description")
        self.descriptionEntry.grid(row=1, column=1, padx=(0, 10), pady=10)
        self.categoryEntry = ctk.CTkEntry(self, placeholder_text="Category")
        self.categoryEntry.grid(row=2, column=1, padx=(0, 10), pady=10)
        self.priceEntry = ctk.CTkEntry(self, placeholder_text="Price")
        self.priceEntry.grid(row=3, column=1, padx=(0, 10), pady=10)
        self.quantityEntry = ctk.CTkEntry(self, placeholder_text="Quantity")
        self.quantityEntry.grid(row=4, column=1, padx=(0, 10), pady=10)
        self.supplier = ctk.CTkEntry(self, placeholder_text="Suppler")
        self.supplier.grid(row=5, column=1, padx=(0, 10), pady=10)

        self.addButton = ctk.CTkButton(self, text="Add Item", command=self.addItem)
        self.addButton.grid(row=6, column=0, padx=(5, 10), pady=10)
        self.exitButton = ctk.CTkButton(self, text="Exit", command=self.destroy)
        self.exitButton.grid(row=6, column=1, padx=(5, 10), pady=10)
        self.entry_widgets = []

        # Add entry widgets to the array
        self.entry_widgets.append(self.nameEntry)
        self.entry_widgets.append(self.descriptionEntry)
        self.entry_widgets.append(self.categoryEntry)
        self.entry_widgets.append(self.priceEntry)
        self.entry_widgets.append(self.quantityEntry)
        self.entry_widgets.append(self.supplier)

    def validateInteger(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def validateString(self, value):
        return isinstance(value, str)

    def validateFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def addItem(self):
        for i in self.entry_widgets:
            if i.get() == "" or None:
                msg.CTkMessagebox(
                    title="Error",
                    message="All fields must be filled in.",
                    icon="cancel",
                )
                return

        name = self.nameEntry.get()
        description = self.descriptionEntry.get()
        category = self.categoryEntry.get()
        price = self.priceEntry.get()
        quantity = self.quantityEntry.get()
        supplier_name = self.supplier.get()
        p = Product(
            product_name=name,
            description=description,
            category_name=category,
            unit_price=price,
            quantity_in_stock=quantity,
            supplier_name=supplier_name,
        )
        # Check if price is a valid number
        try:
            price = float(price)
        except ValueError:
            msg.CTkMessagebox(
                title="Error", message="Price must be a valid number.", icon="cancel"
            )
            return

        # Check if quantity is a valid integer
        try:
            quantity = int(quantity)
        except ValueError:
            msg.CTkMessagebox(
                title="Error",
                message="Quantity must be a valid integer.",
                icon="cancel",
            )
            return

        id = ProductService(db_connection=Database().get_connection()).insert_product(p)
        if quantity > 0:
            TransactionService(
                db_connection=Database().get_connection()
            ).add_transaction(
                str(id),
                "buy",
                quantity=quantity,
                total_amount=round(float(price * quantity), 4),
            )
        for i in self.entry_widgets:
            i.delete(0, "end")
        msg.CTkMessagebox(
            message="Product added succesfully ",
            icon="check",
        )
