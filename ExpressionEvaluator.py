from ExpressionGenerator import ExpressionGenerator
from abc import ABC, abstractclassmethod

class ExpressionEvaluator(ABC):

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def evaluate_expression(self):
        pass

class PostfixEvaluator(ExpressionGenerator):

    def __init__(self):
        pass

    def evaluate_expression(self):
        pass

    def pop_element(self):
        pass

    def compute_result(self):
        pass

    def push_element(self):
        pass
