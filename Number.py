from Argument import Argument

class Number(Argument):

    def __init__(self, number) -> None: 
        self.number_value = float(number)

    def set_argument_value(self, number):
        self.number_value = float(number)

    def get_argument_value(self):
        return self.number_value