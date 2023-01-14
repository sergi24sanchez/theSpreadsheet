from Coordinate import Coordinate
from utils import column_number_to_letter
import pandas as pd

class Spreadsheet():

    def __init__(self, num_rows:int, num_cols:int):
        self.numcols = num_cols
        self.numrows = num_rows
        cols = []
        for col in range(self.numcols):
            cols.append(column_number_to_letter(col+1))
        #empty dataframe
        self.cells = pd.DataFrame(index=range(1,(self.numrows+1)), columns=cols)
        for i, row in self.cells.iterrows():
            for j, cell in row.items():
                if (str(cell) == ('nan')):
                    cell = str('')
        #aqui fer el for i crear/ assignar les celes
    
    def get_cells(self):
        return self.cells

    def get_ncols(self):
        return self.numcols
    
    def get_nrows(self):
        return self.numrows
    
    #crec q sha de treure
    def set_cells(self, cells):
        self.cells = cells

    #crec q sha de treure
    def save_spreadsheet(self,file_name):
        # STILL TO BE IMPLEMENTED
        pass