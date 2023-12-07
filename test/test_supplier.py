import sqlite3
import pytest
from models.supplier import Supplier
from services.product_service import ProductService
from services.supplier_service import SupplierService

DB_NAME = "inventory.db"


@pytest.fixture
def test_db_connection():
    connection = sqlite3.connect(DB_NAME)
    yield connection
    connection.close()


def test_add_supplier(test_db_connection):
    service = SupplierService(test_db_connection)
    supplier = Supplier(
        supplier_id="999",
        supplier_name="TestSupplier",
        contact_person="John Doe",
        contact_number="123456789",
        email="test@example.com",
    )

    assert service.add_supplier(supplier) is True


def test_get_supplier_by_id(test_db_connection):
    service = SupplierService(test_db_connection)
    retrieved_supplier = service.get_supplier_by_id("1")
    assert retrieved_supplier is not None


def test_get_all_suppliers(test_db_connection):
    service = SupplierService(test_db_connection)

    # Check if all suppliers are retrieved
    all_suppliers = service.get_all_suppliers()
    assert all_suppliers is not None
    assert len(all_suppliers) != 0


def test_update_supplier(test_db_connection):
    service = SupplierService(test_db_connection)

    # Update the supplier information
    updated_supplier = Supplier(
        supplier_id="3",
        supplier_name="UpdatedSupplier",
        contact_person="Updated John",
        contact_number="987654321",
        email="updated@example.com",
    )
    service.update_supplier(updated_supplier)

    # Check if the supplier is updated successfully
    retrieved_supplier = service.get_supplier_by_id("3")
    assert retrieved_supplier is not None
    assert retrieved_supplier.supplier_name == "UpdatedSupplier"
    assert retrieved_supplier.contact_person == "Updated John"
    assert retrieved_supplier.contact_number == "987654321"
    assert retrieved_supplier.email == "updated@example.com"


def test_delete_supplier(test_db_connection):
    service = SupplierService(test_db_connection)
    service.delete_supplier("15")

    # Check if the supplier is deleted successfully
    retrieved_supplier = service.get_supplier_by_id("15")
    assert retrieved_supplier is None
