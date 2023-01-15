#from UI import UI
from Tokenizer import Tokenizer
from FormulaFactory import FormulaFactory
from FormulaProcessor import FormulaProcessor
from Spreadsheet import Spreadsheet
from Cell import Cell
from Coordinate import Coordinate
from utils import column_number_to_letter, column_letter_to_number

class SpreadsheetController:
    def __init__(self):
        self.spreadSheet = None
        #self.ui = ui
        self.tokenizer = Tokenizer()
        #NOt sure about the Factories yet
        #self.numericalFact = NumericalFactory()
        #self.textFactory = TextFactory()
        #self.formulaFactory = FormulaFactory()
        #self.factory = None 
        self.formula_factory = FormulaFactory()
        self.formula_processor = self.formula_factory.get_formula_processor()

    def create_spreadsheet(self, nrows, ncols):
        self.spreadSheet = Spreadsheet(nrows, ncols)
        print('creating spreadsheet')

    def get_spreadsheet(self):
        return self.spreadSheet

    def initialize_spreadsheet(self):
        pass

    def edit_cell(self, cell:Cell, content:str):
        cell.set_content(content)
        #faltaria fer un compute value, mirar dependencies ...

    def load_spreadsheet_from_file(self, path:str):
        #self.files_manager.load_spreadsheet(path)
        with open(path, 'r') as file:
            lines = file.readlines()
            nrows = len(lines)
            ncols = []
            for line in lines:
                row_no_n = line.split('\n')[0]
                #print(col_no_n)
                ncols.append(len(row_no_n.split(';')))
            ncols = min(ncols)
            #print(f'cols ={ncols} rows = {nrows}')
            spreadsheet = Spreadsheet(nrows, ncols)
            for idline, line in enumerate(lines): #iterates through rows
                content = line.split(';')
                #print(f'len content : {len(content)}')
                #for idcol, cell in enumerate(content): # iterates through cols
                for idcol in range(1, ncols+1):
                    cell_content = content[idcol-1]
                    #print(f'idline = {idline+1} and idcol = {column_number_to_letter(idcol+1)}')
                    coordinate = Coordinate(f'{column_number_to_letter(idcol)}{idline+1}')
                    specific_cell = spreadsheet.get_cell(coordinate)
                    self.edit_cell(specific_cell, cell_content)
                    #spreadsheet.get_cells().at[idline+1, column_number_to_letter(idcol+1)] = cell
            #print(spreadsheet.get_cells())
            #print('loading from file')
            self.spreadSheet = spreadsheet
        #return spreadsheet.get_cells()
        
    def save_spreadsheet_to_file(self, path:str):
        #self.files_manager.save_spreadsheet(path, self.spreadSheet)
                #crec q sobra un ; del final de linia
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
                elif (column_letter_to_number(j) == cols):
                    txt = f'{txt}{content_of_cell}'
                else:
                    txt = f'{txt}{content_of_cell};'
            if i != rows:
                txt = f'{txt}\n'
        
        f= open(path,"w+")
        f.write(txt)
        f.close()
        print('saving to file')
        

    def read_command_from_file(self):
        print('reading command from file')
        