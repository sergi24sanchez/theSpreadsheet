from abc import ABC, abstractclassmethod

class Argument(ABC):

    @abstractclassmethod
    def __init__(self) -> None:
        pass
    
    @abstractclassmethod
    def set_argument_value(self):
        pass

    @abstractclassmethod
    def get_argument_value(self):
        pass
