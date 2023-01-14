#from UI import UI
from FilesManager import FilesManager
from Tokenizer import Tokenizer
from ExpressionGenerator import PostfixGenerator
from Spreadsheet import Spreadsheet

class SpreadsheetController:
    def __init__(self):
        self.spreadSheet = None
        self.files_manager = FilesManager()
        #self.ui = ui
        self.tokenizer = Tokenizer()
        #NOt sure about the Factories yet
        #self.numericalFact = NumericalFactory()
        #self.textFactory = TextFactory()
        #self.formulaFactory = FormulaFactory()
        #self.factory = None 
        self.generator = PostfixGenerator()

    def create_spreadsheet(self, nrows, ncols):
        self.spreadSheet = Spreadsheet(nrows, ncols)
        print('creating spreadsheet')

    def get_spreadsheet(self):
        return self.spreadSheet

    def initialize_spreadsheet(self):
        pass

    def edit_cell(self):
        pass

    def load_spreadsheet_from_file(self, path:str):
        self.files_manager.load_spreadsheet(path)
        print('loading from file')
        

    def save_spreadsheet_to_file(self, path:str):
        self.files_manager.save_spreadsheet(path, self.spreadSheet)
        print('saving to file')
        

    def read_command_from_file(self):
        print('reading command from file')
        

    
