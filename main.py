from tkinter import filedialog
from migration import create_database
from models.user import User
from utils.database import Database
from utils.center import center_screen_geometry
from windows.buy_win import BuyWin
from windows.login import LoginPage
from windows.product_add import addProductWindow
from windows.product_details import ProductDetailsPopup
from services.product_service import ProductService
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import CTkMessagebox as msg
from windows.sell_win import SellWin
from windows.transaction import TransactionWin
from windows.user_form import UserForm


class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        create_database()
        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=1250,
                window_height=800,
            )
        )
        self.resizable(False, False)
        self.current_lang = "en"
        self.language_var = tk.StringVar(value="English")
        self.language_var.trace("w", self.switch_language)

        # Language dictionaries
        self.lang_dict = {
            "en": {
                "Inventory Page": "Inventory Page",
                "inbound": "Inbound",
                "outbound": "Outbound",
                "add_product": "Add Product",
                "buy_product": "Buy Product",
                "sell_product": "Sell Product",
                "search": "Search",
                "product_id": "Product ID",
                "product_name": "Product Name",
                "description": "Description",
                "category": "Category",
                "price": "Price",
                "quantity_in_stock": "Quantity In Stock",
                "supplier": "Supplier",
                "delete": "Delete",
                "err_del": "You Should Select Item ",
                "del": "Are You Sure You Want To Delete This Product",
                "err": "Error",
                "Yes": "Yes",
                "No": "No",
                "create": "Create User",
                "per": "You Don't Permission To Do this Operation",
                "excel": "Create Excel File",
                "search_err": "Search bar is Empty!",
                "Ok": "Ok",
                "empty": "Could  Not Find The Product",
            },
            "ar": {
                "Inventory Page": "المخزن",
                "inbound": "الوارد",
                "outbound": "الصادر",
                "add_product": "منتج إضافة",
                "buy_product": "منتج شراء",
                "sell_product": "منتج بيع",
                "search": "بحث",
                "product_id": "معرّف المنتج",
                "product_name": "اسم المنتج",
                "description": "الوصف",
                "category": "الفئة",
                "price": "السعر",
                "quantity_in_stock": "الكمية في المخزون",
                "supplier": "المورد",
                "delete": "حذف",
                "err_del": "اختيار المنتج يرجى",
                "del": " المنتج هذا حذف تريد انك متاكد انت هل؟",
                "err": "خطأ",
                "Yes": "نعم",
                "No": "لا",
                "per": "الوصول صلايحة تملك لا أنت",
                "create": "مستخدم أنشاء",
                "excel": "Excel ملف أنشاء",
                "search_err": "فارغ! البحث شريط",
                "Ok": "حسناً",
                "empty": "الاسم بهذا المنتج يوجد لا",
            },
        }
        self.frame_side = None
        self.frame_dashboard = None
        self.treeview = None
        self.frame_control = None
        self.create_widget()
        self.product_service = ProductService(db_connection=Database().get_connection())
        self.prev = ""
        self.curr_idx = 0
        self.title(self.lang_dict[self.current_lang]["Inventory Page"])
        self.products = []
        self.user = User()
        self.open_login()
        self.fetch_product()
        self.mainloop()

    def open_login(self):
        self.withdraw()
        self.login = LoginPage(parent=self)
        self.login.grab_set()

    def fetch_user(self, login):
        self.user = login.user

    def export_to_excel(self, filename="products.xlsx"):
        # Get data from the database
        df = self.product_service.fetch_all_datafram()
        directory_path = filedialog.askdirectory(title="")
        if directory_path != "":
            df.to_excel(directory_path + "/products.xlsx", index=False)

        # # Export the DataFrame to Excel
        # df.to_excel(filename, index=False)
        # print(f"Data exported to {filename}")

    def open_transaction(self, type):
        if type == "inbound":
            TransactionWin(
                lan=self.current_lang,
                transaction=self.lang_dict[self.current_lang][type],
                parent=self,
                type="buy",
            ).grab_set()
        else:
            TransactionWin(
                lan=self.current_lang,
                transaction=self.lang_dict[self.current_lang][type],
                parent=self,
                type="sell",
            ).grab_set()

    def create_widget(self):
        # Create frames
        self.frame_side = ctk.CTkFrame(self)
        self.frame_dashboard = ctk.CTkFrame(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_rowconfigure(0, weight=1)

        # Grid layout
        self.frame_side.grid(row=0, column=0, sticky="nsew")
        self.frame_dashboard.grid(
            row=0, column=1, columnspan=2, sticky="nsew", padx=(15, 0)
        )
        self.frame_control = ctk.CTkFrame(self.frame_dashboard)

        # Create buttons in the sidebar
        self.button1 = ctk.CTkButton(
            self.frame_side,
            text=self.lang_dict[self.current_lang]["inbound"],
            command=lambda: self.open_transaction("inbound"),
        )
        self.button2 = ctk.CTkButton(
            self.frame_side,
            text=self.lang_dict[self.current_lang]["outbound"],
            command=lambda: self.open_transaction("outbound"),
        )
        self.button3 = ctk.CTkButton(
            self.frame_side,
            text=self.lang_dict[self.current_lang]["excel"],
            command=self.export_to_excel,
        )
        self.button4 = ctk.CTkButton(
            self.frame_side,
            text=self.lang_dict[self.current_lang]["create"],
            command=self.open_create_user,
        )

        self.button1.grid(row=0, column=0, pady=50)
        self.button2.grid(row=1, column=0, pady=50)
        self.button3.grid(row=2, column=0, pady=50)
        self.button4.grid(row=3, column=0, pady=50)
        self.frame_side.grid_columnconfigure(0, weight=1)
        self.frame_dashboard.grid_rowconfigure((0), weight=1)
        self.frame_dashboard.grid_rowconfigure((1), weight=10)

        self.frame_control.grid(row=0, column=0, sticky="nswe")

        self.create_tree_view()
        self.create_control_widget()

        # Here's the combobox
        self.language_combobox = ctk.CTkComboBox(
            self.frame_side, values=["English", "العربية"], variable=self.language_var
        )
        self.language_combobox.grid(row=4, column=0, pady=20, padx=10, sticky="ew")

    def open_create_user(self):
        if self.user.role != "admin":
            msg.CTkMessagebox(
                title=self.lang_dict[self.current_lang]["err"],
                message=self.lang_dict[self.current_lang]["per"],
                option_1=self.lang_dict[self.current_lang]["Ok"],
                icon="cancel",
            )
            return
        UserForm(
            parent=self,
            lan=self.language_var.get(),
            title=self.lang_dict[self.current_lang]["add_product"],
        ).grab_set()

    def switch_language(self, *args):
        selected_language = self.language_var.get()
        self.current_lang = "ar" if selected_language == "العربية" else "en"
        self.update_language()

    def update_language(self):
        self.button1.configure(text=self.lang_dict[self.current_lang]["inbound"])
        self.button2.configure(text=self.lang_dict[self.current_lang]["outbound"])
        self.button3.configure(text=self.lang_dict[self.current_lang]["excel"])
        self.button4.configure(text=self.lang_dict[self.current_lang]["create"])
        self.btn_add.configure(text=self.lang_dict[self.current_lang]["add_product"])
        self.btn_delete.configure(text=self.lang_dict[self.current_lang]["delete"])

        self.btn_buy.configure(text=self.lang_dict[self.current_lang]["buy_product"])
        self.btn_sell.configure(text=self.lang_dict[self.current_lang]["sell_product"])
        self.btn_search.configure(text=self.lang_dict[self.current_lang]["search"])
        self.treeview.heading(
            "id", text=self.lang_dict[self.current_lang]["product_id"]
        )
        self.treeview.heading(
            "name", text=self.lang_dict[self.current_lang]["product_name"]
        )
        self.treeview.heading(
            "Description", text=self.lang_dict[self.current_lang]["description"]
        )
        self.treeview.heading(
            "Category", text=self.lang_dict[self.current_lang]["category"]
        )
        self.treeview.heading("Price", text=self.lang_dict[self.current_lang]["price"])
        self.treeview.heading(
            "quantity", text=self.lang_dict[self.current_lang]["quantity_in_stock"]
        )
        self.treeview.heading(
            "Supplier", text=self.lang_dict[self.current_lang]["supplier"]
        )
        self.title(self.lang_dict[self.current_lang]["Inventory Page"])

    def open_sell(self):
        try:
            item = self.treeview.selection()[0]
            SellWin(
                self, self.current_lang, self.treeview.item(item, "values")[0]
            ).grab_set()
        except IndexError as e:
            msg.CTkMessagebox(
                title=self.lang_dict[self.current_lang]["err"],
                message=self.lang_dict[self.current_lang]["err_del"],
                icon="cancel",
                option_1=self.lang_dict[self.current_lang]["Ok"],
            )

    def open_buy(self):
        try:
            item = self.treeview.selection()[0]
            BuyWin(
                self, self.current_lang, self.treeview.item(item, "values")[0]
            ).grab_set()
        except IndexError as e:
            msg.CTkMessagebox(
                title=self.lang_dict[self.current_lang]["err"],
                message=self.lang_dict[self.current_lang]["err_del"],
                icon="cancel",
                option_1=self.lang_dict[self.current_lang]["Ok"],
            )

    def create_control_widget(self):
        # Add buttons and text entry to the frame
        frame_btn = ctk.CTkFrame(self.frame_control, fg_color="#383434")
        self.btn_add = ctk.CTkButton(
            frame_btn,
            text=self.lang_dict[self.current_lang]["add_product"],
            command=self.open_add_product,
        )

        self.entry = ctk.CTkEntry(self.frame_control)
        self.entry.pack(fill="x", anchor="center", padx=80, pady=(10, 0), expand=True)
        frame_btn.pack(side="right", fill="x")
        self.btn_buy = ctk.CTkButton(
            frame_btn,
            text=self.lang_dict[self.current_lang]["buy_product"],
            command=self.open_buy,
        )
        self.btn_search = ctk.CTkButton(
            frame_btn,
            text=self.lang_dict[self.current_lang]["search"],
            command=lambda: self.serach_product(self.entry.get()),
        )

        self.btn_sell = ctk.CTkButton(
            frame_btn,
            text=self.lang_dict[self.current_lang]["sell_product"],
            command=self.open_sell,
        )
        self.btn_delete = ctk.CTkButton(
            frame_btn,
            text=self.lang_dict[self.current_lang]["delete"],
            command=self.delete_product,
        )
        self.btn_add.grid(row=0, column=0)
        self.btn_buy.grid(row=0, column=1, padx=5, pady=10)
        self.btn_sell.grid(row=0, column=2, padx=5, pady=10)
        self.btn_delete.grid(row=0, column=4, padx=5, pady=10)

        self.btn_search.grid(row=0, column=3, padx=5, pady=10)

    def delete_product(self):
        if self.user.role != "admin":
            msg.CTkMessagebox(
                title=self.lang_dict[self.current_lang]["err"],
                message=self.lang_dict[self.current_lang]["per"],
                icon="cancel",
                option_1=self.lang_dict[self.current_lang]["Ok"],
            )
            return

        try:
            item = self.treeview.selection()[0]
            id = self.treeview.item(item)["values"]
            # get yes/no answers
            ask = msg.CTkMessagebox(
                title=self.lang_dict[self.current_lang]["delete"],
                message=self.lang_dict[self.current_lang]["del"],
                icon="question",
                option_1=self.lang_dict[self.current_lang]["No"],
                option_2=self.lang_dict[self.current_lang]["Yes"],
            )
            response = ask.get()
            if response == "Yes" or response == "لا":
                self.product_service.delete_product(id[0])
                self.treeview.delete(item)

        except IndexError as e:
            msg.CTkMessagebox(
                title=self.lang_dict[self.current_lang]["err"],
                message=self.lang_dict[self.current_lang]["err_del"],
                icon="cancel",
                option_1=self.lang_dict[self.current_lang]["Ok"],
            )

    def fetch_product(self):
        result = self.product_service.get_all_products()
        for i in result:
            self.products.append(i[1])
            self.treeview.insert(parent="", index="end", values=i)

    def serach_product(self, prefix: str):
        if prefix == "":
            msg.CTkMessagebox(
                title=self.lang_dict[self.current_lang]["err"],
                message=self.lang_dict[self.current_lang]["search_err"],
                icon="cancel",
                option_1=self.lang_dict[self.current_lang]["Ok"],
            )
            return
        if self.prev != "" and self.prev != prefix:
            self.curr_idx = 0
        self.prev = prefix
        if len(prefix) == 0:
            pass

        for w in range(self.curr_idx, len(self.products)):
            if self.products[w].lower().startswith((prefix.lower())):
                self.curr_idx = w + 1
                result = self.treeview.get_children()[w]

                self.treeview.selection_set(result)
                self.treeview.see(result)

                return

        self.curr_idx = 0
        msg.CTkMessagebox(
            title=self.lang_dict[self.current_lang]["err"],
            message=self.lang_dict[self.current_lang]["empty"],
            icon="cancel",
            option_1=self.lang_dict[self.current_lang]["Ok"],
        )

        return None

    def open_add_product(self):
        self.add_product = addProductWindow(parent=self, lan=self.current_lang)
        self.add_product.grab_set()

    def update_treeview(self):
        self.products = []
        self.treeview.delete(*self.treeview.get_children())

        self.fetch_product()
        self.treeview.update()

    def on_treeview_click(self, event):
        item = self.treeview.selection()[0]
        product_details = {}
        for col, val in zip(
            self.treeview["columns"], self.treeview.item(item, "values")
        ):
            product_details[col] = val
        win2 = ProductDetailsPopup(self, product_details, self.current_lang)
        win2.grab_set()

    def create_tree_view(self):
        frame_tree = ctk.CTkFrame(self.frame_dashboard)
        frame_tree.grid(row=1, column=0, sticky="nsew", pady=20)

        # Create Treeview with scrolling
        self.treeview = ttk.Treeview(
            frame_tree,
            columns=(
                "id",
                "name",
                "Description",
                "Price",
                "quantity",
                "Category",
                "Supplier",
            ),
            show="headings",
            selectmode="browse",
        )
        self.treeview.grid(row=0, column=0, sticky="nsew")

        # Add columns to the Treeview
        self.treeview.heading("id", text="Product ID")
        self.treeview.heading("name", text="Product Name")
        self.treeview.heading("Description", text="Description")
        self.treeview.heading("quantity", text="Quantity In Stock")
        self.treeview.heading("Price", text="Price")
        self.treeview.heading("Category", text="Category")
        self.treeview.heading("Supplier", text="Supplier")
        self.treeview.column("id", width=80)
        self.treeview.column("Price", width=100)
        self.treeview.column("quantity", width=100)
        self.treeview.column("Category", width=150)

        # Add a vertical scrollbar
        yscrollbar = ttk.Scrollbar(
            frame_tree, orient="vertical", command=self.treeview.yview
        )
        yscrollbar.grid(row=0, column=1, sticky="ns")
        self.treeview.configure(yscrollcommand=yscrollbar.set)

        # Add a horizontal scrollbar
        xscrollbar = ttk.Scrollbar(
            frame_tree, orient="horizontal", command=self.treeview.xview
        )
        xscrollbar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.treeview.configure(xscrollcommand=xscrollbar.set)

        # Configure weights for resizing
        frame_tree.grid_columnconfigure(0, weight=1)
        frame_tree.grid_rowconfigure(0, weight=1)
        self.treeview.bind("<Double-Button-1>", self.on_treeview_click)


main()
