import pytest

from database import Database
from models.product import BaseProduct, Product
from services.product_service import ProductService


con = Database().get_connection()

service = ProductService(db_connection=con)


def test_get_product():
    result = service.get_all_products()
    assert result is not None
    assert len(result) != 0


def test_insert_a_product():
    product1 = BaseProduct(
        product_name="Sample Product",
        description="This is a sample product",
        unit_price=19.99,
        quantity_in_stock=100,
        category_id=1,
        category_name="Electronics",
        supplier_id=101,
        supplier_name="ABC Supplier",
    )
    result = service.insert_product(product1)

    print(result)
    assert result is not None


def test_update_a_product():
    product1 = Product(
        product_id=55,
        product_name="Sample Product",
        description="This is a sample product",
        unit_price=19.99,
        quantity_in_stock=100,
        category_id=1,
        category_name="Electronics",
        supplier_id=101,
        supplier_name="ABC Supplier",
    )
    result = service.update_product(product1)

    print(result)
    assert result is not None
