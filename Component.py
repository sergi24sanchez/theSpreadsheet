class Component():

    def __init__(self) -> None:
        pass


class Operand(Component):

    def __init__(self) -> None:
        super().__init__()


class Operator(Component):

    def __init__(self, operator) -> None:
        super().__init__()
        self.type_of_operator = operator