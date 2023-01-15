class NoNumberException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class BadCoordinateException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class ContentException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class InputError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message