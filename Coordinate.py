'''Class Coordinate'''

from typing import Self

class Coordinate():

    def __init__(self):
        self.row = None
        self.column = None
    
    def get_coordinate(self):
        return self
    
    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column
    
    #do we need this?
    def set_coordinate(self, row_number, column_letter):
        self.row = row_number
        self.column = column_letter