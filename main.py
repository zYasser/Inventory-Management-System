from database import Database
from services.admin_service import AdminService
from services.product_service import ProductService


con = Database().get_connection()

service = ProductService(db_connection=con)
service.get_all_products()
