import pytest

from database import Database
from services.admin_service import AdminService


con = Database().get_connection()

service = AdminService(db_connection=con)


def test_add_admin():
    assert (
        service.create_admin("username", "pawwrod", email="hello", fullname="kasdksd")
        is True
    )


def test_get_user_exist():
    user = service.get_admin("1")
    print(user)
    assert user is not None


def test_get_user_unexist():
    user = service.get_admin("0")
    assert user is None
