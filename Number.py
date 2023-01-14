from Argument import Argument

class Number(Argument):

    def __init__(self, number:float) -> None: 
        self.number_value = number

    def set_argument_value(self, number:float):
        self.number_value = number

    def get_argument_value(self):
        return self.number_value