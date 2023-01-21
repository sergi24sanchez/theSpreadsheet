from Argument import Argument
from Component import Operand

class Number(Argument,Operand):

    def __init__(self, number:float) -> None: 
        self.number_value = number

    def set_argument_value(self, number:float):
        self.number_value = number

    def get_argument_value(self):
        return self.number_value
    
    def get_operand_value(self):
        return self.number_value
    
    def set_operand_value(self,value):
        self.number_value = float(value)