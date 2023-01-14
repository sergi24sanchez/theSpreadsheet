'''
class Component
class Operand
class Operator
'''
from abc import ABC, abstractclassmethod
from enum import Enum
from Tokenizer import Token

class Component:

    def __init__(self) -> None:
        pass
    

class Operand(Component):
    '''component de la formula'''
    def __init__(self) -> None:
        pass
    
    @abstractclassmethod
    def get_operand_value(self):
        pass
    
    @abstractclassmethod
    def set_operand_value(self):
        pass


class OperatorEnum(Enum):
    SUMA = 1
    RESTA = 2
    MULT = 3
    DIV = 4


class Operator(Component):
    '''+,-'''
    def __init__(self, type_:OperatorEnum, token_:Token) -> None:
        self.type = type_
        self.sequence = token_.get_sequence()