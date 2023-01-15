from Argument import Argument
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

    def get_all_cells(self) -> list:
        
        all_cells = []
        initial_row = [*self.initial_cell][1]
        initial_col = utils.column_letter_to_number([*self.initial_cell][0])
        final_row = [*self.final_cell][1]
        final_col = utils.column_letter_to_number([*self.final_cell][0])
        for col in range(int(initial_col), int(final_col)+1):
            col_letter = utils.column_number_to_letter(col)
            for row in range(int(initial_row), int(final_row)+1):
                all_cells.append(f'{col_letter}{row}')        
        return all_cells

    def set_argument_value(self):
        self.range_val = self.get_all_cells()

    def get_argument_value(self):
        return self.range_val