'''Class Coordinate'''
import re

class Coordinate():

    def __init__(self, coordinates):
        self.row = int(re.findall(r'\d+', coordinates)[0])
        self.column = re.findall(r'[a-zA-Z]+', coordinates)[0]
        
        
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

