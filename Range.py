from typing import List

from Argument import Argument
from Cell import Cell
from Coordinate import Coordinate
from Spreadsheet import Spreadsheet
import utils

class Range(Argument):
    '''Range(B2:D5)'''
    def __init__(self, range:str) -> None:
        self.initial_cell = range.split(':')[0]
        self.final_cell = range.split(':')[1]
        self.range_val = None

    def set_initial_cell(self, range:str):
        self.initial_cell = range.split(':')[0]

    def set_final_cell(self, range:str):
        self.initial_cell = range.split(':')[0]

    def get_initial_cell(self):
        return self.initial_cell
    
    def get_final_cell(self):
        return self.final_cell

    def get_all_cells(self,spreadsheet:Spreadsheet) -> List[Cell]:

        all_cells = []
        initial_coord = Coordinate(self.initial_cell)
        initial_row = int(initial_coord.get_row())
        initial_col = int(utils.column_letter_to_number(initial_coord.get_column()))
        final_coord = Coordinate(self.final_cell)
        final_row = int(final_coord.get_row())
        final_col = int(utils.column_letter_to_number(final_coord.get_column()))
        for col in range(initial_col, final_col+1):
            col_letter = utils.column_number_to_letter(col)
            for row in range(initial_row, final_row+1):
                coord = Coordinate(f'{col_letter}{row}')
                cell = spreadsheet.get_cell(coord)
                all_cells.append(cell)
                # all_cells.append(f'{col_letter}{row}')        
        return all_cells

    def set_argument_value(self,value):
        self.range_val = self.get_all_cells()

    def get_argument_value(self):
        return self.range_val