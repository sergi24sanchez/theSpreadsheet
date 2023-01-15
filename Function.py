'''
class Function
class Suma
class Min
class Max
class Promedio
'''

from abc import ABC, abstractclassmethod
from typing import List
from Component import Operand
from Argument import Argument

from enum import Enum

class FunctionEnum(Enum):
    SUMA = "SUMA"
    PROMEDIO = "PROMEDIO"
    MAX = "MAX"
    MIN = "MIN"


class Function(Argument,Operand,ABC):

    def __init__(self, arguments_list:List[Argument]) -> None:
        '''
        arguments_list = every item of this list is of type Argument (a subclass)
        '''
        self.arguments = arguments_list # vacia, y despues un metodo de añadir argumentos
        self.value = self.compute_value()
    
   # ARGUMENT CLASS METHODS 
    @abstractclassmethod
    def get_argument_value():
        # metodo polimorfico
        pass
    
    @abstractclassmethod
    def set_argument_value(self):
        pass
    
    @abstractclassmethod
    def compute_value(self):
        pass

    @abstractclassmethod
    def get_operand_value(self):
        pass
    
    @abstractclassmethod
    def set_operand_value(self):
        pass   


class Suma(Function): 

    def __init__(self,arguments_list) -> None:
        super().__init__(arguments_list)
             
    def compute_value(self):
        res = sum([argument.get_argument_value() for argument in self.arguments])
        return res
    
    def get_argument_value(self):
        return self.value
    
    def get_operand_value(self):
        return self.value
    
    def set_argument_value(self,value):
        self.value = value
    
    def set_operand_value(self,value):
        self.value = value


class Min(Function):

    def __init__(self,arguments_list) -> None:
        super().__init__(arguments_list)

    def compute_value(self):
        res = min([argument.get_argument_value() for argument in self.arguments])
        return res
    
    def get_argument_value(self):
        return self.value
    
    def get_operand_value(self):
        return self.value
    
    def set_argument_value(self,value):
        self.value = value
    
    def set_operand_value(self,value):
        self.value = value


class Max(Function):

    def __init__(self,arguments_list) -> None:
        super().__init__(arguments_list)

    def compute_value(self):
        res = max([argument.get_argument_value() for argument in self.arguments])
        return res
    
    def get_argument_value(self):
        return self.value
    
    def get_operand_value(self):
        return self.value
    
    def set_argument_value(self,value):
        self.value = value
    
    def set_operand_value(self,value):
        self.value = value


class Promedio(Function):

    def __init__(self,arguments_list) -> None:
        super().__init__(arguments_list)

    def compute_value(self):
        suma = sum([argument.get_argument_value() for argument in self.arguments])
        res = (suma)/(len(self.arguments))
        return res 
    
    def get_argument_value(self):
        return self.value
    
    def get_operand_value(self):
        return self.value
    
    def set_argument_value(self,value):
        self.value = value
    
    def set_operand_value(self,value):
        self.value = value