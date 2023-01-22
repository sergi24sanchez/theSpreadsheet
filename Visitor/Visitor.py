from abc import ABC,abstractclassmethod

from ExpressionGenerator import PostFixGenerator
from ExpressionEvaluator import PostfixEvaluator
from Element import Generator,Evaluator

class Visitor(ABC):

    @abstractclassmethod
    def visit_generator(generator:Generator):
        pass

    def visit_evaluator(evaluator:Evaluator):
        pass


class VisitorPostfix(Visitor):

    def visit_generator()