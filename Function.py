from Component import Operand
from Argument import Argument

class Function(Argument,Operand):

    def __init__(self) -> None:
        Argument.__init__(self)
        Operand.__init__(self)