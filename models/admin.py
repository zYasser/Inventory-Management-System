class Admin:
    def __init__(self, admin_id, username, password, email=None, full_name=None):
        self.admin_id = admin_id
        self.username = username
        self.password = password
        self.email = email
        self.full_name = full_name

    def __repr__(self):
        return f"Admin(AdminID={self.admin_id}, Username='{self.username}', Password='{self.password}', Email='{self.email}', FullName='{self.full_name}')"
