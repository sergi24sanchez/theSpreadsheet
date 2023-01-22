#from src.edu.upc.etsetb.arqsoft.spreadsheet.usecases.marker.spreadsheet_controller_for_checker import ISpreadsheetControllerForChecker
from src.edu.upc.etsetb.arqsoft.spreadsheet.usecases.marker.spreadsheet_controller_for_checker import ISpreadsheetControllerForChecker
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.bad_coordinate_exception import BadCoordinateException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.circular_dependency_exception import CircularDependencyException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.content_exception import ContentException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.no_number_exception import NoNumberException
from src.edu.upc.etsetb.arqsoft.spreadsheet.usecases.marker.reading_spreadsheet_exception import ReadingSpreadsheetException
from src.edu.upc.etsetb.arqsoft.spreadsheet.usecases.marker.saving_spreadsheet_exception import SavingSpreadsheetException
from Exceptions import InputError
from Coordinate import Coordinate
from SpreadsheetController import SpreadsheetController

class SpreadsheetChecker(ISpreadsheetControllerForChecker):
    def __init__(self):
        self.controller = SpreadsheetController()

    def set_cell_content(self, coord, str_content):
        try:
            coordinate = self.controller.check_coordinate(coord)
            cell_to_modify = self.controller.get_spreadsheet().get_cell(coordinate)
            #TO DO: Create an object depending of the type of content and give it to the cell.setcontent()
            cell_to_modify.set_content(str_content)
        except BadCoordinateException as e:
            print(e)
        except ContentException as e:
            print(e)
        except CircularDependencyException as e:
            print(e)

    def get_cell_content_as_float(self, coord):
        try:
            coordinate = self.controller.check_coordinate(coord)
            cell = self.controller.spreadSheet.get_cell(coordinate)
            return cell.get_content().get_value().get_as_float()
        except BadCoordinateException as e:
            print(e)
        except NoNumberException as e:
            print(e)

    def get_cell_content_as_string(self, coord):
        try:
            coordinate = self.controller.check_coordinate(coord)
            cell = self.controller.spreadSheet.get_cell(coordinate)
            return cell.get_content().get_value().get_as_string()
        except BadCoordinateException as e:
            print(e)

    def get_cell_formula_expression(self, coord):
        try:
            coordinate = self.controller.check_coordinate(coord)
            cell = self.controller.spreadSheet.get_cell(coordinate)
            return cell.get_content().get_value().get_as_string()
        except BadCoordinateException as e:
            print(e)

    def save_spreadsheet_to_file(self, s_name_in_user_dir):
        try:
            self.controller.save_spreadsheet_to_file(s_name_in_user_dir)
        except SavingSpreadsheetException as e:
            print(e)

    def load_spreadsheet_from_file(self, s_name_in_user_dir):
        try:
            self.controller.load_spreadsheet_from_file(s_name_in_user_dir)
        except ReadingSpreadsheetException as e:
            print(e)
