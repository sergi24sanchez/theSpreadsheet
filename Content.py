'''
Class Content
Class Numerical
Class Text
Class Formula
'''

from abc import ABC, abstractmethod

class Content(ABC):

    def __init__(self):
        self.input_string = None
    
    def get_content(self):
        return self.input_string
    
    def set_content(self,input_string):
        self.input_string = input_string
    
    @abstractmethod
    def compute_value(self):
        pass


class Numerical(Content):

    def __init__(self):
        super().__init__()
        self.value = None
    
    def get_content(self):
        return super().get_content()
    
    def set_content(self, input_string):
        return super().set_content(input_string)
    
    def compute_value(self):
        self.number_value = int(self.input_string)  # Is it OK?
    

class Text(Content):

    def __init__(self):
        super().__init__()
        self.value = None
    
    def get_content(self):
        return super().get_content()

    def set_content(self, input_string):
        return super().set_content(input_string)
    
    def compute_value(self):
        self.string_value = self.input_string


class Formula(Content):

    def __init__(self):
        super().__init__()
        self.value = None
    
    def get_content(self):
        return super().get_content()
    
    def set_content(self, input_string):
        return super().set_content(input_string)
    
    def compute_value(self):
        # STILL NOT IMPLEMENTED
        pass