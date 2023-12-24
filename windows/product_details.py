import customtkinter as ctk

from utils.center import center_screen_geometry


class ProductDetailsPopup(ctk.CTkToplevel):
    def __init__(self, parent, product_details, lan):
        super().__init__(parent)
        self.title("Product Details")
        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=500,
                window_height=500,
            )
        )
        self.lang_dict = {
            "en": [
                "Product ID",
                "Product Name",
                "Description",
                "Price",
                "Quantity In Stock",
                "Category",
                "Supplier",
            ],
            "ar": [
                "المنتج معرّف",
                "المنتج اسم",
                "الوصف",
                "السعر",
                "المخزون في الكمية",
                "الفئة",
                "المورد",
            ],
        }
        self.resizable(False, False)
        i = 0
        for _, val in product_details.items():
            ctk.CTkLabel(self, text=self.lang_dict[lan][i] + ":").grid(
                row=i, column=0, sticky="e", pady=20, padx=50
            )
            ctk.CTkLabel(self, text=val).grid(
                row=i, column=1, sticky="w", pady=20, padx=20
            )
            i = i + 1
