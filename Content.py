'''
Class Content
Class Numerical
Class Text
Class Formula
'''
from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from NumberValue import NumberValue
from StringValue import StringValue
from Value import Value

from Component import Component

class ContentEnum(Enum):
    NO_TYPE = 0
    FORMULA = 1
    NUMERICAL = 2
    TEXT = 3

class Content(ABC):

    def __init__(self, input_string:str):
        self.input_string = input_string
        self.content_type = ContentEnum.NO_TYPE
    
    def get_input_string(self):
        return self.input_string
    
    def set_input_string(self,input_string:str):
        self.input_string = input_string
    
    @abstractmethod
    def compute_value(self):
        pass

    @abstractmethod
    def set_value(self, value_):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_for_print(self):
        pass


class Numerical(Content):

    def __init__(self, input_string:str):
        super().__init__(input_string)
        self.value = self.compute_value()
        self.content_type = ContentEnum.NUMERICAL
    
    def get_input_string(self):
        return super().get_input_string()
    
    def set_input_string(self, input_string:str):
        return super().set_input_string(input_string)
    
    def compute_value(self):
        try:
            val = int(self.input_string)
        except ValueError:
            val = float(self.input_string)
        return NumberValue(val)

    def set_value(self, value_:float|int):
        self.value = NumberValue(value_)

    def get_value(self):
        return self.value
    
    def get_for_print(self):
        return f'{self.value}'
    

class Text(Content):

    def __init__(self, input_string:str):
        super().__init__(input_string)
        self.value = self.compute_value()
        self.content_type = ContentEnum.TEXT
    
    def get_input_string(self):
        return super().get_input_string()

    def set_input_string(self, input_string:str):
        return super().set_input_string(input_string)
    
    def compute_value(self):
        self.value = StringValue(self.input_string)

    def set_value(self, value_:str):
        self.value = StringValue(value_)

    def get_value(self):
        return self.value
    
    def get_for_print(self):
        return f'{self.value.get_as_string()}'


class Formula(Content):

    def __init__(self, input_string:str):
        super().__init__(input_string)
        self.content_type = ContentEnum.FORMULA
        self.components = None
        self.value = None
    
    def get_input_string(self):
        return super().get_input_string()
    
    def set_input_string(self, input_string:str):
        return super().set_input_string(input_string)
    
    def get_components(self):
        return self.components
    
    def set_components(self,components_:List[Component]):
        self.components = components_

    def set_value(self, value_:int|float):
        self.value = NumberValue(value_)

    def get_value(self):
        return self.value

    def get_for_print(self):
        return f'{self.get_input_string()} = {self.value.get_as_string()}'