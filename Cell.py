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
        self.idependon = None
    
    def get_coordinate(self):
        return self.coordinate
    
    def get_content(self):
        return self.content

    def get_idependon(self):
        return self.idependon

    def get_dependsonme(self):
        return self.dependsonme

    def get_for_print(self):
        pass

    def set_content(self, content:Content):
        self.content = content

    def set_coordinate(self,coordinate:Coordinate):
        self.coordinate = coordinate

    def set_idependon(self, cells):
        #cells: list of cells or a Cell that will be given
        self.idependon = cells

    def add_dependsonme(self, coordinate:Coordinate):
        self.dependsonme.append(coordinate)

    def set_argument_value(self):
        pass

    def get_argument_value(self):
        pass
    
    def get_operand_value(self):
        return self.content