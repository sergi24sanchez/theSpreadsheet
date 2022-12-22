from Argument import Argument
from Component import Operand
from Coordinate import Coordinate
from Content import Content

class Cell(Argument,Operand):

    def __init__(self, coordinate:Coordinate):

        self.coordinate = coordinate
        self.content = None
    
    def get_coordinate(self):
        return self.coordinate
    
    def get_content(self):
        return self.content

    def set_content(self, content:Content):
        self.content = content

    def set_coordinate(self,coordinate:Coordinate):
        self.coordinate = coordinate