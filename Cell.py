'''class Cell'''
from Argument import Argument
from Component import Operand
from Coordinate import Coordinate
from Content import Content

class Cell(Argument,Operand):

    def __init__(self, coordinate:Coordinate):

        self.coordinate = coordinate
        self.content = None
        self.dependsonme = []
        self.idependon = []
    
    def get_coordinate(self):
        return self.coordinate
    
    def get_content(self):
        return self.content

    def set_content(self, content:Content):
        self.content = content

    def set_coordinate(self,coordinate:Coordinate):
        self.coordinate = coordinate

    def add_dependsonme(self, coordinate:Coordinate):
        self.dependsonme.append(coordinate)

    def set_idependon(self, cells):
        #cells is a list of cells or a Cell that will be given
        self.idependon = cells
