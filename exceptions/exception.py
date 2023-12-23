class DuplicateEmailError(Exception):
    def __init__(self, message="Email is not unique."):
        self.message = message
        super().__init__(self.message)

class DuplicateUsernameError(Exception):
    def __init__(self, message="Username is not unique."):
        self.message = message
        super().__init__(self.message)