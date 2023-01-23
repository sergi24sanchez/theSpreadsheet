#from UI import UI
from typing import Coroutine
from Function import Function
from Tokenizer import Tokenizer
from FormulaFactory import FormulaFactory
from FormulaProcessor import FormulaProcessor
from Spreadsheet import Spreadsheet
from Cell import Cell
from Content import Content, Formula, Numerical, Text, ContentEnum
from Coordinate import Coordinate
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.circular_dependency_exception import CircularDependencyException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.content_exception import ContentException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.bad_coordinate_exception import BadCoordinateException
import utils as utils
from Exceptions import *
from SpreadsheetPrinter import SpreadsheetPrinter

from typing import List

class SpreadsheetController:
    def __init__(self):
        self.spreadSheet = Spreadsheet(num_rows = 25,num_cols=25)
        self.printer = SpreadsheetPrinter()
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

    def create_content_by_type(self, type:str, content:str):
        if type == ContentEnum.FORMULA:
            return self.formula_processor.create_formula(
                input_string=content,
                spreadsheet=self.spreadSheet,
            )
        elif type == ContentEnum.TEXT:
            return Text(content)
        elif type == ContentEnum.NUMERICAL:
            return Numerical(content)
        else:
            raise ContentException("Incorrect content for a cell")

    def check_coordinate(self, coord:str):
        coordinate = Coordinate(coord)
        if (coordinate.get_row() > self.spreadSheet.get_nrows()) and (utils.column_letter_to_number(coordinate.get_column()) > self.spreadSheet.get_ncols()):
            raise BadCoordinateException("The coordinate introduced is not valid")
        return coordinate

    # def get_all_dependent_cells(self, cell:Cell)->List[Cell]:
    #     dependsonme = cell.get_dependsonme()
    #     dependencies=[]
    #     for dependant_cell in dependsonme:
    #         if dependant_cell not in dependencies:
    #             if dependant_cell == cell:
    #                 raise CircularDependencyException(f'Cell {cell.coordinate.get_as_string} generates a circular dependency')
    #             dependencies.append(dependant_cell)
            
    #             # inner_dependsonme = self.get_all_dependent_cells(cell=dependant_cell)
    #             # for depend in inner_dependsonme:
    #             #     if depend not in dependencies:
    #             #         if depend == dependant_cell or depend == cell:
    #             #             raise CircularDependencyException(f'Cell {dependant_cell.coordinate.get_as_string} generates a circular dependency')
    #             #         dependencies.append(depend)

    #     return dependencies
            
    def search_cirucular_dependencies(self, cell:Cell):
        #when searching for circular dependencies, raise an exception if circular dependencies == true
        for item in cell.get_dependsonme():
            if item in cell.get_idependon():
                raise CircularDependencyException('Circular depencendies!')
    
    def recalculate_dependent_cells(self, dependencies):
        for cell in dependencies:
            formula = cell.get_content()
            formula_components = formula.get_components()
            for component in formula_components:
                if isinstance(component,Function):
                    self.formula_processor.calculate_value_of_function_of_formula(
                        function=component,
                    )
            formula.compute_value(self.formula_processor)

    def edit_cell(self, cell_coordinate:str, content:str):
        try:
            coord = self.check_coordinate(cell_coordinate)
        except BadCoordinateException as e:
            print(e)
            return
        cell_obj = self.spreadSheet.get_cell(coordinate=coord)

        input_type = utils.check_string(content)

        new_content = self.create_content_by_type(input_type,content)
        cell_obj.set_content(content_=new_content)

        self.formula_processor.refresh_depending_cells(
            changed_cell=cell_obj,
        )
        # ACTUALLY REFRESH THE VALUES
        self.search_cirucular_dependencies(cell_obj)
        #depend_on_this_cell = self.get_all_dependent_cells(cell=cell_obj)
        # calculate actual cell
        if isinstance(cell_obj.get_content(),Formula):
            cell_obj.get_content().compute_value(self.formula_processor)
        else:
            cell_obj.get_content().compute_value()
        #calculate dependsonme new value
        self.recalculate_dependent_cells(cell_obj.get_dependsonme())

    def load_cell(self, cell_coordinate:str,content:str):
        try:
            coord = self.check_coordinate(cell_coordinate)
        except BadCoordinateException as e:
            print(e)
            return
        cell_obj = self.spreadSheet.get_cell(coordinate=coord)

        input_type = utils.check_string(content)

        new_content = self.create_content_by_type(input_type,content)
        cell_obj.set_content(content_=new_content)

        self.formula_processor.refresh_depending_cells(
            changed_cell=cell_obj,
        )
        # # ACTUALLY REFRESH THE VALUES
        # self.search_cirucular_dependencies(cell_obj)
        # depend_on_this_cell = self.get_all_dependent_cells(cell=cell_obj)
        # # calculate actual cell
        # if isinstance(cell_obj.get_content(),Formula):
        #     cell_obj.get_content().compute_value(self.formula_processor)
        # else:
        #     cell_obj.get_content().compute_value()
        # #calculate dependsonme new value
        # self.recalculate_dependent_cells(depend_on_this_cell)
    
    def compute_value_of_loaded_cells(self,spreadsheet:Spreadsheet):
        df = spreadsheet.get_cells()

        for i, row in df.iterrows():
            for j, cell in row.items():
                content_of_cell = cell.get_content()
                if isinstance(content_of_cell,Formula):
                    content_of_cell.compute_value(
                        formula_processor=self.formula_processor
                    )

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
                if ((content_of_cell == '')
                or (str(content_of_cell) == 'nan')
                or (content_of_cell is None)):
                    txt = f'{txt};'
                elif (utils.column_letter_to_number(j) == cols):
                    txt = f'{txt}{content_of_cell.get_as_string()}'
                else:
                    txt = f'{txt}{content_of_cell.get_as_string()};'
            if i != rows:
                txt = f'{txt}\n'
        
        f= open(path,"w+")
        f.write(txt)
        f.close()
        print('saving to file')

    def load_spreadsheet_from_file(self, path:str):
        #self.files_manager.load_spreadsheet(path)
        with open(path, 'r') as file:
            lines = file.readlines()
            nrows = len(lines)
            ncols = []
            for line in lines:
                row_no_n = line.split('\n')[0]
                ncols.append(len(row_no_n.split(';')))
            ncols = max(ncols)
            spreadsheet = Spreadsheet(num_rows = nrows, num_cols = ncols)
            for idline, line in enumerate(lines): #iterates through rows
                row_no_n = line.split('\n')[0]
                all_contents_row = row_no_n.split(';')
                for idcol in range(1, ncols+1):
                    cell_content = all_contents_row[idcol-1]
                    coordinate = Coordinate(
                        f'{utils.column_number_to_letter(idcol)}{idline+1}'
                    )
                    specific_cell = spreadsheet.get_cell(coordinate)
                    self.load_cell(
                        cell_coordinate=specific_cell.get_coordinate(),
                        content=cell_content,
                    )
                self.compute_value_of_loaded_cells(
                    spreadsheet=self.spreadSheet,
                )
            self.spreadSheet = spreadsheet

    def read_command_from_file(self):
        print('reading command from file')