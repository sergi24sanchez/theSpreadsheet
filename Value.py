'''
Class Value
Class FloatValue
Class StringValue
'''
from abc import ABC, abstractclassmethod

class Value(ABC):

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get_value():
        pass

    @abstractclassmethod
    def get_as_string():
        pass

    @abstractclassmethod
    def get_as_float():
        pass
    
    @abstractclassmethod
    def set_value():
        pass


class FloatValue(Value):

    def __init__(self, float_value):
        self.value = float_value
    
    def get_value(self):
        return self.value

    def get_as_float():
        pass
    
    def set_value(self, value):
        self.value = value


class StringValue(Value):

    def __init__(self, string_value):
        self.value = string_value
    
    def get_value(self):
        return self.value

    def get_as_string():
        pass

    def set_value(self, value):
        self.value = value