'''
Class Content
Class Numerical
Class Text
Class Formula
'''

from abc import ABC, abstractmethod
from FloatValue import FloatValue
from StringValue import StringValue

class Content(ABC):

    def __init__(self, input_string):
        self.input_string = input_string
    
    def get_content(self):
        return self.input_string
    
    def set_content(self,input_string):
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
    
    def get_content(self):
        return super().get_content()
    
    def set_content(self, input_string):
        return super().set_content(input_string)
    
    def compute_value(self):
        self.number_value = int(self.input_string)  # Is it OK?

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def get_for_print(self):
        return f'{self.value}'
    

class Text(Content):

    def __init__(self, input_string):
        super().__init__(input_string)
        self.value = None
    
    def get_content(self):
        return super().get_content()

    def set_content(self, input_string):
        return super().set_content(input_string)
    
    def compute_value(self):
        self.string_value = self.input_string

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def get_for_print(self):
        return f'{self.value}'


class Formula(Content):

    def __init__(self, input_string):
        super().__init__(input_string)
        self.value = None
    
    def get_content(self):
        return super().get_content()
    
    def set_content(self, input_string):
        return super().set_content(input_string)
    
    def compute_value(self):
        # STILL NOT IMPLEMENTED
        pass

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_for_print(self):
        return f'{self.get_content()} = {self.value}'