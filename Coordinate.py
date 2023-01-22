'''Class Coordinate'''
import re
from Exceptions import BadCoordinateException


class Coordinate:

    def __init__(self, coordinates:str):
        try:
            self.row = int(re.findall(r'\d+', coordinates)[0])
        except IndexError:
            raise BadCoordinateException('A row number is missing!')
        try:
            column = re.findall(r'[a-zA-Z]+', coordinates)[0]
            self.column = column.upper()
        except IndexError:
            raise BadCoordinateException('A row number is missing!')
        
    def get_coordinate(self):
        return f'{self.column}{self.row}'
    
    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column
    
    #do we need this?
    def set_coordinate(self, row_number, column_letter):
        self.row = row_number
        self.column = column_letter

