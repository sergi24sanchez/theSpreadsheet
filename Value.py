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
