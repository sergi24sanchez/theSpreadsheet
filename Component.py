'''
class Component
class Operand
class Operator
'''

class Component():

    def __init__(self) -> None:
        pass


class Operand(Component):
    '''component de la formula'''
    def __init__(self, operand) -> None:
        super().__init__()



class Operator(Component):
    '''+,-'''
    def __init__(self, operator) -> None:
        super().__init__()
        self.type_of_operator = operator