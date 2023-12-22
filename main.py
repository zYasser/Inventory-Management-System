from uri_template import expand
from models.user import User
from utils.database import Database
from utils.center import center_screen_geometry
from windows.login import LoginPage
from windows.product_details import ProductDetailsPopup
from services.product_service import ProductService
import customtkinter as ctk
from tkinter import W, Widget, ttk
import CTkMessagebox as msg


class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1250x800")
        self.geometry(
            center_screen_geometry(
                screen_width=self.winfo_screenwidth(),
                screen_height=self.winfo_screenheight(),
                window_width=1250,
                window_height=800,
            )
        )
        self.resizable(False, False)

        self.frame_side = None
        self.frame_dashboard = None
        self.treeview = None
        self.frame_control = None
        self.create_widget()
        self.product_service = ProductService(db_connection=Database().get_connection())
        self.prev = ""
        self.curr_idx = 0
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
        print(self.user)

    def create_widget(self):
        # Create frames
        self.frame_side = ctk.CTkFrame(
            self,
        )
        self.frame_dashboard = ctk.CTkFrame(
            self,
        )
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
        button1 = ctk.CTkButton(self.frame_side, text="Button 1")
        button2 = ctk.CTkButton(self.frame_side, text="Button 2")
        button3 = ctk.CTkButton(self.frame_side, text="Button 3")
        button4 = ctk.CTkButton(self.frame_side, text="Button 4")

        button1.grid(row=0, column=0, pady=50)
        button2.grid(row=1, column=0, pady=50)
        button3.grid(row=2, column=0, pady=50)
        button4.grid(row=3, column=0, pady=50)
        self.frame_side.grid_columnconfigure(0, weight=1)
        self.frame_dashboard.grid_rowconfigure((0), weight=1)
        self.frame_dashboard.grid_rowconfigure((1), weight=10)

        self.frame_control.grid(row=0, column=0, sticky="nswe")

        self.create_tree_view()
        self.create_control_widget()

    def create_control_widget(self):
        # Add buttons and text entry to the frame
        frame_btn = ctk.CTkFrame(self.frame_control, fg_color="#383434")
        self.btn_add = ctk.CTkButton(
            frame_btn,
            text="Add Product",
        )

        self.entry = ctk.CTkEntry(self.frame_control)
        self.entry.pack(fill="x", anchor="center", padx=80, pady=(10, 0), expand=True)
        frame_btn.pack(side="right", fill="x")
        self.btn_buy = ctk.CTkButton(
            frame_btn,
            text="Buy Product",
        )
        self.btn_search = ctk.CTkButton(
            frame_btn,
            text="Search",
            command=lambda: self.serach_product(self.entry.get()),
        )

        self.btn_sell = ctk.CTkButton(
            frame_btn,
            text="Sell Product",
        )
        self.btn_add.grid(row=0, column=0)
        self.btn_buy.grid(row=0, column=1, padx=5, pady=10)
        self.btn_sell.grid(row=0, column=2, padx=5, pady=10)
        self.btn_search.grid(row=0, column=3, padx=5, pady=10)

    def fetch_product(self):
        result = self.product_service.get_all_products()
        for i in result:
            self.products.append(i[1])
            self.treeview.insert(parent="", index="end", values=i)

    def serach_product(self, prefix: str):
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
            title="Error", message="Coudld Not Find The Product", icon="cancel"
        )

        return None

    def on_treeview_click(self, event):
        item = self.treeview.selection()[0]
        product_details = {}
        for col, val in zip(
            self.treeview["columns"], self.treeview.item(item, "values")
        ):
            product_details[col] = val
        win2 = ProductDetailsPopup(self, product_details)
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
                "Category",
                "Price",
                "quantity",
                "Supplier",
            ),
            show="headings",
        )
        self.treeview.grid(row=0, column=0, sticky="nsew")

        # Add columns to the Treeview
        self.treeview.heading("id", text="Product ID")
        self.treeview.heading("name", text="Product Name")
        self.treeview.heading("Description", text="Description")
        self.treeview.heading("Category", text="Category")
        self.treeview.heading("Price", text="Price")
        self.treeview.heading("quantity", text="Quantity In Stock")
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
