
class InputError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ParserException(Exception):
    def __init__(self, msg:str):
        self.msg = msg
