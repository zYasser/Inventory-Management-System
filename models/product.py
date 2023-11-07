class BaseProduct:
    def __init__(
        self,
        product_name,
        description,
        unit_price,
        quantity_in_stock,
        category_id=None,
        category_name=None,
        supplier_id=None,
        supplier_name=None,
    ):
        self.product_name = product_name
        self.description = description
        self.unit_price = unit_price
        self.quantity_in_stock = quantity_in_stock
        self.category_id = category_id
        self.category_name = category_name
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name

    def __repr__(self):
        return f"ProductName='{self.product_name}', Description='{self.description}', UnitPrice={self.unit_price}, QuantityInStock={self.quantity_in_stock}, CategoryID={self.category_id}', SupplierID={self.supplier_id},')"


class Product(BaseProduct):
    def __init__(
        self,
        product_id,
        product_name,
        description,
        unit_price,
        quantity_in_stock,
        category_id=None,
        category_name=None,
        supplier_id=None,
        supplier_name=None,
    ):
        super().__init__(
            product_name=product_name,
            description=description,
            unit_price=unit_price,
            quantity_in_stock=quantity_in_stock,
            category_id=category_id,
            supplier_id=supplier_id,
        )
        self.product_id = product_id

        self.category_name = category_name
        self.supplier_name = supplier_name

    def __repr__(self):
        return f"Product(ProductID={self.product_id}, ProductName='{self.product_name}', Description='{self.description}', UnitPrice={self.unit_price}, QuantityInStock={self.quantity_in_stock}, CategoryID={self.category_id}, CategoryName='{self.category_name}', SupplierID={self.supplier_id}, SupplierName='{self.supplier_name}')"
