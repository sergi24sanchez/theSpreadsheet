'''
class Function
class Suma
class Min
class Max
class Promedio
'''

from abc import ABC, abstractclassmethod
from Component import Operand
from Argument import Argument

class Function(Argument,Operand,ABC):

    def __init__(self, arguments_list) -> None:
        '''
        arguments_list = every item of this list is of type Argument (a subclass)
        '''
        Argument.__init__(self)
        Operand.__init__(self)
        self.arguments = arguments_list
        self.result = None
   
    def calculate_arguments_value(self):
        #REVIEW THIS IS NOT CORRECT
        for arg in self.arguments:
            self.argument_val.append(arg.get_argument_value(arg))

    @abstractclassmethod
    def compute_result(self):
        pass
    
    def set_result(self):
        self.result = self.compute_result()

    def get_result(self):
        return self.result

class Suma(Function):

    def __init__(self) -> None:
        super().__init__()
            
    def compute_result(self):
        res = sum(self.argument_val)
        return res


class Min(Function):

    def __init__(self) -> None:
        super().__init__()

    def compute_result(self):
        res = min(self.argument_val)
        return res

class Max(Function):

    def __init__(self) -> None:
        super().__init__()

    def compute_result(self):
        res = max(self.argument_val)
        return res  

class Promedio(Function):

    def __init__(self) -> None:
        super().__init__()

    def compute_result(self):
        res = (sum(self.argument_val))/(len(self.argument_val))
        return res  