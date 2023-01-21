from Visitor import Visitor
from abc import ABC,abstractclassmethod

class Element(ABC):

    @abstractclassmethod
    def accept_visitor():
        pass


class Generator(Element):

    def accept_visitor(self,visitor:Visitor):
        visitor.visit_generator(self)


class Evaluator(Element):

    def accept_visitor(self,visitor:Visitor):
        visitor.visit_evaluator(self)