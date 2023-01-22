#from UI import UI
from typing import Coroutine
from Tokenizer import Tokenizer
from FormulaFactory import FormulaFactory
from FormulaProcessor import FormulaProcessor
from Spreadsheet import Spreadsheet
from Cell import Cell
from Content import Content, Formula, Numerical, Text
from Coordinate import Coordinate
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.content_exception import ContentException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.bad_coordinate_exception import BadCoordinateException
import utils as utils
from Exceptions import *

class SpreadsheetController:
    def __init__(self):
        self.spreadSheet = Spreadsheet(num_rows = 25,num_cols=25)
        #self.ui = ui
        self.tokenizer = Tokenizer()
        #NOt sure about the Factories yet
        #self.numericalFact = NumericalFactory()
        #self.textFactory = TextFactory()
        #self.factory = None 
        self.formula_factory = FormulaFactory()
        self.formula_processor = self.formula_factory.get_formula_processor()

    def create_spreadsheet(self, nrows, ncols):
        self.spreadSheet = Spreadsheet(num_rows = nrows,num_cols=ncols)
        print('creating spreadsheet')

    def get_spreadsheet(self):
        return self.spreadSheet

    #crec q no cal
    def initialize_spreadsheet(self):
        pass

    def check_type_content(self, content:str):

        if content.startswith("="):
            return 'isFormula'
        try:
            int(content)
            return 'isNumerical'
        except:
            try:
                str(content)
                return 'isText'
            except:
                return 'noType'

        return 'noType' 

    def create_type_content(self, type:str, content:str):
        if type == 'isFormula':
            return Formula(content)
        elif type == 'isText':
            return Text(content)
        elif type == 'isNumerical':
            return Numerical(content)
        else:
            raise ContentException("Incorrect content for a cell")

    def check_coordinate(self, coord:str):
        coordinate = Coordinate(coord)
        if (coordinate.get_row() > self.spreadSheet.get_nrows()) and (utils.column_letter_to_number(coordinate.get_column()) > self.spreadSheet.get_ncols()):
            raise BadCoordinateException("The coordinate introduced is not valid")
        return coordinate

    def edit_cell(self, cell_coordinate:str, content:str):
        try:
            coord = self.check_coordinate(cell_coordinate)
        except BadCoordinateException as e:
            print(e)
            return

        #cell.set_content(content)
        #faltaria fer un compute value, mirar dependencies ...

    
        
    def save_spreadsheet_to_file(self, path:str):
        #self.files_manager.save_spreadsheet(path, self.spreadSheet)
        df = self.spreadSheet.get_cells()
        cols = self.spreadSheet.get_ncols()
        rows = self.spreadSheet.get_nrows()
        txt = ''
        for i, row in df.iterrows():
            for j, cell in row.items():
                content_of_cell = cell.get_content()
                #print(f'i = {i} and j = {j}')
                if (content_of_cell == '') or (str(content_of_cell) == 'nan'):
                    txt = f'{txt};'
                elif (utils.column_letter_to_number(j) == cols):
                    txt = f'{txt}{content_of_cell}'
                else:
                    txt = f'{txt}{content_of_cell};'
            if i != rows:
                txt = f'{txt}\n'
        
        f= open(path,"w+")
        f.write(txt)
        f.close()
        print('saving to file')

    def load_spreadsheet_from_file(self, path:str):
        #self.files_manager.load_spreadsheet(path)
        with open(path, 'r') as file:
            #print('awa1')
            lines = file.readlines()
            nrows = len(lines)
            ncols = []
            for line in lines:
                #print(f'awa2 {line}')
                row_no_n = line.split('\n')[0]
                #print(col_no_n)
                ncols.append(len(row_no_n.split(';')))
            ncols = max(ncols)
            #print('awa3')
            #print(f'cols ={ncols} rows = {nrows}')
            spreadsheet = Spreadsheet(num_rows = nrows, num_cols = ncols)
            for idline, line in enumerate(lines): #iterates through rows
                #print(f'awa4')
                row_no_n = line.split('\n')[0]
                content = row_no_n.split(';')
                #print(content)
                #print(f'len content : {len(content)}')
                #for idcol, cell in enumerate(content): # iterates through cols
                for idcol in range(1, ncols+1):
                    cell_content = content[idcol-1]
                    #print(f'idline = {idline+1} and idcol = {column_number_to_letter(idcol+1)}')
                    coordinate = Coordinate(
                        f'{utils.column_number_to_letter(idcol)}{idline+1}'
                    )
                    specific_cell = spreadsheet.get_cell(coordinate)
                    #TO DO: Modificar edit cell pq sea el de arriba
                    self.edit_cell(specific_cell, cell_content)
                    #print('awa5')
                    #spreadsheet.get_cells().at[idline+1, column_number_to_letter(idcol+1)] = cell
            #print(spreadsheet.get_cells())
            #print('loading from file')
            self.spreadSheet = spreadsheet
        #return spreadsheet.get_cells()
        

    def read_command_from_file(self):
        print('reading command from file')

def main():
    pass

if __name__ == "__main__":
    main()