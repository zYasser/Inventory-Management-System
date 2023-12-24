import customtkinter as ctk
import tkinter as tk

from models.product import Product
from services.product_service import ProductService
from utils.database import Database

import CTkMessagebox as msg


class addProductWindow(ctk.CTkToplevel):
    def __init__(self, parent, lan):
        super().__init__(parent)
        self.parent = parent
        self.lan = lan
        self.geometry("300x400+700+300")
        self.resizable(0, 0)
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.lang_dict = {
            "en": {
                "Product Name": "Product Name",
                "Description": "Description",
                "Price": "Price",
                "Quantity In Stock": "Quantity In Stock",
                "Category": "Category",
                "Supplier": "Supplier",
                "err_price": "Price Should More Than 0",
                "stock": "Quantity Should More Than or equal 0",
                "err": "Error",
                "int": "Price And Quantitiy Should Be A Number",
                "successfully": "Product added succesfully",
                "add": "Add Product",
                "fill": "You Should Fill All Fields",
                "clear": "Clear",
            },
            "ar": {
                "Product Name": "المنتج اسم",
                "Description": "الوصف",
                "Price": "السعر",
                "Quantity In Stock": "المخزون في الكمية",
                "Category": "الفئة",
                "Supplier": "المورد",
                "err_price": "0 من اكثر يكون ان يجب السعر",
                "stock": "0  يساوي او من اكثر تكون ان الكمية يجب",
                "err": "خطا",
                "int": "رقم تكون ان السعر و الكمية ان يجب",
                "successfully": "بنجاح المنتج اضافة تمت",
                "add": "اضافة منتج",
                "fill": "المعلومات جميع اكمال يجب",
                "clear": "مسح",
            },
        }
        self.createWidgets()

        self.title(self.lang_dict[self.lan]["add"])

    def close_window(self):
        self.destroy()
        self.parent.update_treeview()

    def createWidgets(self):
        self.nameLabel = ctk.CTkLabel(
            self,
            text=self.lang_dict[self.lan]["Product Name"],
        )
        self.nameLabel.grid(row=0, column=0, padx=(5, 10), pady=10)
        self.descriptionLabel = ctk.CTkLabel(
            self,
            text=self.lang_dict[self.lan]["Description"],
        )
        self.descriptionLabel.grid(row=1, column=0, padx=(5, 10), pady=10)
        self.categoryLabel = ctk.CTkLabel(
            self,
            text=self.lang_dict[self.lan]["Category"],
        )
        self.categoryLabel.grid(row=2, column=0, padx=(5, 10), pady=10)
        self.priceLabel = ctk.CTkLabel(
            self,
            text=self.lang_dict[self.lan]["Quantity In Stock"],
        )
        self.priceLabel.grid(row=3, column=0, padx=(5, 10), pady=10)
        self.quantityLabel = ctk.CTkLabel(
            self,
            text=self.lang_dict[self.lan]["Price"],
        )
        self.quantityLabel.grid(row=4, column=0, padx=(5, 10), pady=10)
        self.supplierLabel = ctk.CTkLabel(
            self,
            text=self.lang_dict[self.lan]["Supplier"],
        )
        self.supplierLabel.grid(row=5, column=0, padx=(5, 10), pady=10)

        self.nameEntry = ctk.CTkEntry(
            self,
        )
        self.nameEntry.grid(row=0, column=1, padx=(0, 10), pady=10)
        self.descriptionEntry = ctk.CTkEntry(
            self,
        )
        self.descriptionEntry.grid(row=1, column=1, padx=(0, 10), pady=10)
        self.categoryEntry = ctk.CTkEntry(
            self,
        )
        self.categoryEntry.grid(row=2, column=1, padx=(0, 10), pady=10)
        self.priceEntry = ctk.CTkEntry(
            self,
        )
        self.priceEntry.grid(row=4, column=1, padx=(0, 10), pady=10)
        self.quantityEntry = ctk.CTkEntry(
            self,
        )
        self.quantityEntry.grid(row=3, column=1, padx=(0, 10), pady=10)
        self.supplier = ctk.CTkEntry(
            self,
        )
        self.supplier.grid(row=5, column=1, padx=(0, 10), pady=10)

        self.addButton = ctk.CTkButton(
            self, text=self.lang_dict[self.lan]["add"], command=self.addItem
        )
        self.addButton.grid(row=6, column=0, padx=(5, 10), pady=10)
        self.exitButton = ctk.CTkButton(
            self, text=self.lang_dict[self.lan]["clear"], command=self.clear
        )
        self.exitButton.grid(row=6, column=1, padx=(5, 10), pady=10)
        self.entry_widgets = []

        # Add entry widgets to the array
        self.entry_widgets.append(self.nameEntry)
        self.entry_widgets.append(self.descriptionEntry)
        self.entry_widgets.append(self.categoryEntry)
        self.entry_widgets.append(self.priceEntry)
        self.entry_widgets.append(self.quantityEntry)
        self.entry_widgets.append(self.supplier)

    def clear(self):
        for i in self.entry_widgets:
            i.delete(0, "end")

    def addItem(self):
        for i in self.entry_widgets:
            if i.get() == "" or None:
                msg.CTkMessagebox(
                    title=self.lang_dict[self.lan]["err"],
                    message=self.lang_dict[self.lan]["fill"],
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
        print(p)
        # Check if price is a valid number
        try:
            price = float(price)
        except ValueError:
            msg.CTkMessagebox(
                title=self.lang_dict[self.lan]["err"],
                message=self.lang_dict[self.lan]["int"],
                icon="cancel",
            )
            return

        # Check if quantity is a valid integer
        try:
            quantity = int(quantity)
        except ValueError:
            msg.CTkMessagebox(
                title=self.lang_dict[self.lan]["err"],
                message=self.lang_dict[self.lan]["int"],
                icon="cancel",
            )
            return
        if price <= 0:
            msg.CTkMessagebox(
                title=self.lang_dict[self.lan]["err"],
                message=self.lang_dict[self.lan]["err_price"],
                icon="cancel",
            )
            return
        if quantity < 0:
            msg.CTkMessagebox(
                title=self.lang_dict[self.lan]["err"],
                message=self.lang_dict[self.lan]["stock"],
                icon="cancel",
            )
            return
        self.clear()
        ProductService(db_connection=Database().get_connection()).insert_product(p)
        msg.CTkMessagebox(
            title="",
            message=self.lang_dict[self.lan]["successfully"],
            icon="check",
        )
