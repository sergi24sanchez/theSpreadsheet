from Coordinate import Coordinate
from Cell import Cell
from utils import column_number_to_letter
import pandas as pd
from Exceptions import InputError

class Spreadsheet:

    def __init__(self, num_rows, num_cols):
        self.numcols = int(num_cols)
        self.numrows = int(num_rows)

        cols = []
        for col in range(self.numcols):
            cols.append(column_number_to_letter(col+1))
        self.cells = pd.DataFrame(index=pd.RangeIndex(1, (self.numrows+1)), columns=cols)
        for i in range(1, self.numrows+1):
            for j in range(1, self.numcols+1):
                self.cells.at[i, column_number_to_letter(j)] = Cell(f'{column_number_to_letter(j)}{i}')
        """cols = []
        for col in range(self.numcols):
            cols.append(column_number_to_letter(col+1))
        #empty dataframe
        self.cells = pd.DataFrame(index=range(1,(self.numrows+1)), columns=cols)
        for i, row in self.cells.iterrows():
            for j, cell in row.items():
                if (str(cell) == ('nan')):
                    cell = str('')
        #aqui fer el for i crear/ assignar les celes """
    
    def get_cells(self):
        return self.cells

    def get_ncols(self):
        return self.numcols
    
    def get_nrows(self):
        return self.numrows

    def get_cell(self, coordinate:Coordinate) -> Cell:
        return self.cells.at[coordinate.get_row(), coordinate.get_column()]
    
    #crec q sha de treure
    def set_cells(self, cells):
        self.cells = cells

    #crec q sha de treure
    def save_spreadsheet(self,file_name):
        # STILL TO BE IMPLEMENTED
        pass

#spread = Spreadsheet(3,4)
#print(spread.get_cells())