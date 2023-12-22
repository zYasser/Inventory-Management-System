from cgi import print_directory
import customtkinter as ctk

from utils.center import center_screen_geometry


class ProductDetailsPopup(ctk.CTkToplevel):
    def __init__(self, parent, product_details):
        super().__init__(parent)
        self.title("Product Details")
        self.geometry(center_screen_geometry(screen_width=self.winfo_screenwidth(),
                                    screen_height=self.winfo_screenheight(),
                                    window_width=500,
                                    window_height=500))
        self.resizable(False ,False)
        print(product_details)
        labels = [
            "ID",
            "Name",
            "Description",
            "Category",
            "Price",
            "Quantity",
            "Supplier",
        ]
        print(type(product_details))
        i = 0
        for _, val in product_details.items():
            ctk.CTkLabel(self, text=labels[i] + ":").grid(row=i, column=0, sticky="e" , pady=20 , padx=50)
            ctk.CTkLabel(self, text=val).grid(
                row=i, column=1, sticky="w",
                pady=20 , padx=20
            )
            i=i+1

