'''
Class Content
Class Numerical
Class Text
Class Formula
'''
from abc import ABC, abstractmethod
from typing import List

from FloatValue import FloatValue
from StringValue import StringValue
from Value import Value

from Component import Component

class Content(ABC):

    def __init__(self, input_string):
        self.input_string = input_string
    
    def get_input_string(self):
        return self.input_string
    
    def set_input_string(self,input_string):
        self.input_string = input_string
    
    @abstractmethod
    def compute_value(self):
        pass

    @abstractmethod
    def set_value(self, value):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_for_print(self):
        pass


class Numerical(Content):

    def __init__(self, input_string):
        super().__init__(input_string)
        self.value = None
    
    def get_input_string(self):
        return super().get_input_string()
    
    def set_input_string(self, input_string):
        return super().set_input_string(input_string)
    
    def compute_value(self):
        self.number_value = int(self.input_string)  # Is it OK?

    def set_value(self, value_):
        self.value = FloatValue(value_)

    def get_value(self):
        return self.value
    
    def get_for_print(self):
        return f'{self.value}'
    

from StringValue import StringValue

class Text(Content):

    def __init__(self, input_string):
        super().__init__(input_string)
        self.value = None
    
    def get_input_string(self):
        return super().get_input_string()

    def set_input_string(self, input_string):
        return super().set_input_string(input_string)
    
    def compute_value(self):
        self.string_value = self.input_string

    def set_value(self, value_:str):
        self.value = StringValue(value_)

    def get_value(self):
        return self.value
    
    def get_for_print(self):
        return f'{self.value}'


from FloatValue import FloatValue

class Formula(Content):

    def __init__(self, input_string):
        super().__init__(input_string)
        self.value = None
        self.components = None
    
    def get_input_string(self):
        return super().get_input_string()
    
    def set_input_string(self, input_string):
        return super().set_input_string(input_string)
    
    def get_components(self):
        return self.components
    
    def set_components(self,components_:List[Component]):
        self.components = components_

    def set_value(self, value_:float):
        self.value = FloatValue(value_)

    def get_value(self):
        return self.value

    def compute_value(self):
        # STILL NOT IMPLEMENTED
        pass

    def get_for_print(self):
        return f'{self.get_input_string()} = {self.value.get_as_string()}'