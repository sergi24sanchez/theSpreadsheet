from abc import ABC, abstractclassmethod
from Component import Operand
from Argument import Argument

class Function(Argument,Operand,ABC):

    @abstractclassmethod
    def __init__(self) -> None:
        Argument.__init__(self)
        Operand.__init__(self)
    @abstractclassmethod
    def get_result(Argument):
        # STILL TO BE IMPLEMENTED
        pass

class Suma(Function):

    def __init__(self) -> None:
        super().__init__()

    def get_result(Argument):

        pass

class Min(Function):

    def __init__(self) -> None:
        super().__init__()

    def get_result(Argument):

        pass

class Max(Function):

    def __init__(self) -> None:
        super().__init__()

    def get_result(Argument):

        pass    

class Promedio(Function):

    def __init__(self) -> None:
        super().__init__()

    def get_result(Argument):

        pass