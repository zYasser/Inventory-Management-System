class Product:
    def __init__(
        self,
        product_id=None,
        product_name=None,
        description=None,
        unit_price=None,
        quantity_in_stock=None,
        category_name=None,
        supplier_name=None,
    ):
        self.product_id = None
        self.product_name = product_name
        self.description = description
        self.unit_price = unit_price
        self.quantity_in_stock = quantity_in_stock
        self.category_name = category_name
        self.supplier_name = supplier_name

    def __repr__(self):
        return (
            f"Product("
            f"product_id={self.product_id}, "
            f"product_name='{self.product_name}', "
            f"description='{self.description}', "
            f"unit_price={self.unit_price}, "
            f"quantity_in_stock={self.quantity_in_stock}, "
            f"category_name='{self.category_name}', "
            f"supplier_name='{self.supplier_name}')"
        )
