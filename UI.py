from SpreadsheetController import SpreadsheetController
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.bad_coordinate_exception import BadCoordinateException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.content_exception import ContentException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.circular_dependency_exception import CircularDependencyException
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.no_number_exception import NoNumberException

class UI():
    def __init__(self):
        pass

    def print_menu(self):
        print("Select one option: \n\t - Press 'RF' to read the rest of commands from a file \n\t - Press 'C' for creating a new Spreadsheet \n\t - Press 'E' to edit a Cell \n\t - Press 'L' to Load an existing Spreadsheet from a file \n\t - Press 'S' to save the Spreadsheet to file \n\t - Press 'F' to finish session")

    def start_session(self, controller:SpreadsheetController):
        print("Welcome, what action do you want to do?")
        end = 0
        while not end:
            self.print_menu()
            action = input()
            command = action.lower()
            try:
                if command == 'f':
                    print('Ending the session...')
                    end = 1
                    return end
                elif command == "rf":
                    controller.read_command_from_file()
                elif command == "c":
                    print('Write the number of rows you want the new spreadsheet to have:')
                    nrows = input()
                    print('Write the number of columns you want the new spreadsheet to have:')
                    ncols = input()
                    controller.create_spreadsheet(nrows, ncols)
                elif command == "e":
                    cell_cordinate = input('Write the cell you want to edit: ')
                    cell_content = input('Write the content for the cell: ')
                    controller.edit_cell(
                        cell_coordinate=cell_cordinate,
                        content=cell_content,
                    )
                elif command == "l":
                    print('Introduce the path of the file you want to load. Include the name and also the extension .txt')
                    path_load = input()
                    controller.load_spreadsheet_from_file(path_load)
                elif command == "s":
                    print('Introduce the output path of the file you want to save. Include the name and also the extension .txt')
                    path_save = input()
                    controller.save_spreadsheet_to_file(path_save)
                else:
                    raise ValueError("Invalid input")
                controller.printer.show_all_spreadsheet(controller.spreadSheet)
            except BadCoordinateException as e:
                print(e)
            except ContentException as e:
                print(e)
            except ValueError as e:
                print(e)
            except CircularDependencyException as e:
                print(e)

# ui = UI()
# controller = ui.get_SpreadsheetController()
# controller.create_spreadsheet(3,4)
# #print(controller.spreadSheet)
# controller.load_spreadsheet_from_file('awa.txt')
# controller.save_spreadsheet_to_file('awa2.txt')
# #print(spread)
# controller = SpreadsheetController()
# ui = UI()
# ui.start_session(controller)