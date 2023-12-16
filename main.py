import random
from database import Database
from services.admin_service import AdminService
from services.product_service import ProductService
import customtkinter as ctk
from tkinter import W, Widget, ttk


class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.frame_side = None
        self.frame_dashboard = None
        self.treeview = None
        self.frame_control = None
        self.create_widget()
        self.con = Database().get_connection()
        self.product_service = ProductService(db_connection=self.con)
        self.fetch_product()
        self.mainloop()

    def create_widget(self):
        # Create frames
        self.frame_side = ctk.CTkFrame(self, border_color="red", border_width=3)
        self.frame_dashboard = ctk.CTkFrame(
            self,
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_rowconfigure(0, weight=1)

        # Grid layout
        self.frame_side.grid(row=0, column=0, sticky="nsew")
        self.frame_dashboard.grid(row=0, column=1, columnspan=2, sticky="nsew")
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
        frame_btn = ctk.CTkFrame(self.frame_control)
        self.btn_add = ctk.CTkButton(
            frame_btn,
            text="Button 1",
        )
        self.entry = ctk.CTkEntry(self.frame_control)
        self.entry.pack(fill="x", anchor="center", padx=80, pady=10)
        

        self.btn_buy = ctk.CTkButton(
            frame_btn,
            text="Button 2",
        )

        self.btn_sell = ctk.CTkButton(
            frame_btn,
            text="Button 3",
        )
        self.btn_add.grid(row=0, column=0)
        self.btn_buy.grid(row=0, column=1, padx=5, pady=10)
        self.btn_sell.grid(row=0, column=2, padx=5, pady=10)




    def fetch_product(self):
        result = self.product_service.get_all_products()
        for i in result:
            self.treeview.insert(parent="", index="end", values=i)

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


main()
