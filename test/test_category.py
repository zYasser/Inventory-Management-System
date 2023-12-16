import pytest
import sqlite3
import os
from services.category_service import CategoryService


@pytest.fixture
def category_service():
    connection = sqlite3.connect("inventory.db")
    service = CategoryService(connection)
    yield service


@pytest.mark.skip()
def test_insert_and_get_all_categories(category_service):
    categories = category_service.get_all_categories()

    assert len(categories) == 2
    assert (1, "Electronics") in categories
    assert (2, "Clothing") in categories


@pytest.mark.skip()
def test_update_category(category_service):
    category_service.update_category(category_id=1, new_category_name="Gadgets")

    updated_category = category_service.get_category_by_id(category_id=1)

    assert updated_category == (1, "Gadgets")


def test_delete_category(category_service):
    category_service.delete_category(category_id=1)

    deleted_category = category_service.get_category_by_id(category_id=1)

    assert deleted_category is None


def test_get_category_by_id(category_service):
    category = category_service.get_category_by_id(category_id=1)

    assert category == (1, "Electronics")


@pytest.mark.skip()
def test_get_category_by_nonexistent_id(category_service):
    category = category_service.get_category_by_id(category_id=999)

    assert category is None
