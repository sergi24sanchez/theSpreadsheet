from abc import ABC, abstractclassmethod

class Argument(ABC):

    @abstractclassmethod
    def __init__(self) -> None:
        pass
    
    @abstractclassmethod
    def get_argument_value(self):
        pass
