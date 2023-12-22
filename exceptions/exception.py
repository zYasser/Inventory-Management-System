class DuplicateEmailError(Exception):
    def __init__(self, message="Email is not unique."):
        self.message = message
        super().__init__(self.message)

class DuplicatePasswordError(Exception):
    def __init__(self, message="Password is not unique."):
        self.message = message
        super().__init__(self.message)

