'''class Cell'''
from Argument import Argument
from Component import Operand
from Coordinate import Coordinate
from Content import Content

class Cell(Argument,Operand):

    def __init__(self, coordinate_:Coordinate):
        self.coordinate = coordinate_
        self.content = Content(input_string='')
        self.dependsonme = []
        self.idependon = []
    
    def get_coordinate(self):
        #si ho faig servir aixi es un str i no un objecte coordinate
        #return self.coordinate.get_coordinate()
        return self.coordinate
    
    def get_row(self):
        return self.coordinate.get_row()

    def get_col(self):
        return self.coordinate.get_column()

    def get_content(self):
        return self.content

    def get_idependon(self):
        return self.idependon

    def get_dependsonme(self):
        return self.dependsonme

    def get_for_print(self):
        self.content.get_for_print()

    def set_content(self, content_:Content):
        self.content = content_

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
        '''It gets the content's Value object's value'''
        return self.content.get_value().get_value()
    
    def get_operand_value(self):
        '''It gets the content's Value object's value'''
        return self.content.get_value().get_value()