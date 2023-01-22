from typing import List

from abc import ABC, abstractclassmethod

from Component import Component,Operand,Operator,OperatorEnum

class ExpressionEvaluator(ABC):

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def evaluate_expression(self):
        pass

class PostfixEvaluator(ExpressionEvaluator):

    def __init__(self):
        pass

    def evaluate_expression(self,components:List[Component]):

        stack = []
        for comp in components:
            if isinstance(comp,Operand):
                stack.append(comp.get_operand_value())
            elif isinstance(comp,Operator):
                if stack:
                    value2 = stack.pop()
                    value1 = stack.pop()
                else:
                    raise Exception("Stack is empty")

                if comp.type == OperatorEnum.SUMA:
                    stack.append(value1 + value2)
                elif comp.type == OperatorEnum.RESTA:
                    stack.append(value1 - value2)
                elif comp.type == OperatorEnum.MULT:
                    stack.append(value1 * value2)
                elif comp.type == OperatorEnum.DIV:
                    stack.append(value1 / value2)
            
        return stack.pop()