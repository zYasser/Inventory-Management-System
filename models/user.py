class User:
    def __init__(
        self,
        user_id=None,
        username=None,
        password=None,
        email=None,
        full_name=None,
        role_id=None,
        role=None,
    ):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.full_name = full_name
        self.role_id = role_id  
        self.role = role

    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}, Password: {self.password}, Email: {self.email}, Full Name: {self.full_name}, Role ID: {self.role_id}, Role: {self.role}"
