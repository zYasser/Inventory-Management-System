import customtkinter as ctk
from services.product_service import ProductService
from services.transaction_service import TransactionService

from utils.center import center_screen_geometry
from utils.database import Database
import CTkMessagebox as msg


class BuyWin(ctk.CTkToplevel):
    def __init__(self, master, lan, id):
        super().__init__(master)
        self.master = master
        self.lan = lan
        self.id = id
        self.dict_lan = {
            "en": {
                "error": "Quantity Should Be Only Number",
                "buy": "Buy",
                "Price": "This Will Cost You:",
                "confirm": "Are You Sure Want To Buy It",
                "qua": "Enter quantity:",
                "Customer": "Customer",
                "Customer_err": "Please Enter a Customer",
                "err": "Error",
                "Submit": "Submit",
                "Yes": "Yes",
                "No": "No",
                "Done": "The Product has bought",
                "stock": "Quantity Should more than 0",
            },
            "ar": {
                "error": "رقم تكون ان يجب الكمية",
                "buy": "شراء",
                "Price": "يكلفك سوا هذا",
                "confirm": "الكمية هذه شراء تريد أنك متأكد انت هل",
                "qua": "كمية ادخل:",
                "Customer": "العميل",
                "Customer_err": "العميل ادخال الرجاء",
                "err": "خطا",
                "Submit": "تقديم",
                "Yes": "نعم",
                "No": "لا",
                "Done": "المنتج شراء تم",
                "stock": "0 من اكثر تكون ان الكيمة يجب",
            },
        }
        self.title(self.dict_lan[lan]["buy"])

        # Add widgets to the window
        self.label = ctk.CTkLabel(self, text=self.dict_lan[lan]["qua"])
        self.label.pack(pady=10)
        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=250,
                window_height=250,
            )
        )

        self.quantity_entry = ctk.CTkEntry(self)
        self.quantity_entry.pack(pady=10)

        self.ok_button = ctk.CTkButton(
            self, text=self.dict_lan[lan]["Submit"], command=self.handle_transication
        )
        self.ok_button.pack(pady=10)
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        self.destroy()
        self.master.update_treeview()

    def handle_transication(self):
        p = ProductService(db_connection=Database().get_connection())
        product = p.get_product_by_id(self.id)
        quantity = self.quantity_entry.get()
        try:
            quantity = int(quantity)
            if quantity <= 0:
                msg.CTkMessagebox(
                    title=self.dict_lan[self.lan]["err"],
                    message=self.dict_lan[self.lan]["stock"],
                    icon="cancel",
                )
                return

            price = round(float(product.unit_price * quantity), 3)
            # get yes/no answers
            response = msg.CTkMessagebox(
                title="",
                message=self.dict_lan[self.lan]["confirm"]
                + f"\n {self.dict_lan[self.lan]['Price']}{price}",
                icon="question",
                option_1=self.dict_lan[self.lan]["Yes"],
                option_2=self.dict_lan[self.lan]["No"],
            )
            if response.get() == "Yes" or response.get() == "نعم":
                p.change_stock(self.id, quantity)
                TransactionService(Database().get_connection()).add_transaction(
                    product_id=self.id,
                    transaction_type="buy",
                    quantity=quantity,
                    total_amount=price,
                    customer=product.supplier_name,
                )
                msg.CTkMessagebox(
                    title="", message=self.dict_lan[self.lan]["Done"], icon="check"
                )
            else:
                return
        except ValueError:
            msg.CTkMessagebox(
                title=self.dict_lan[self.lan]["err"],
                message=self.dict_lan[self.lan]["error"],
                icon="cancel",
            )
