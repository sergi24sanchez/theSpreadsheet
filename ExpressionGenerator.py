from Parser_ import Parser
from abc import ABC, abstractclassmethod

class ExpressionGenerator(ABC):

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def generate_expression(self):
        pass

class PostfixGenerator(ExpressionGenerator):

    def __init__(self):
        pass

    def generate_expression(self):
        pass