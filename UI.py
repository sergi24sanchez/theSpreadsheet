from SpreadsheetController import SpreadsheetController
from Exceptions import BadCoordinateException, ContentException, InputError

class UI():
    def __init__(self):
        self.controller = SpreadsheetController()

    def print_menu(self):
        print("Select one option: \n\t - Press 'RF' to read the rest of commands from a file \n\t - Press 'C' for creating a new Spreadsheet \n\t - Press 'E' to edit a Cell \n\t - Press 'L' to Load an existing Spreadsheet from a file \n\t - Press 'S' to save the Spreadsheet to file \n\t - Press 'F' to finish session")


    def get_SpreadsheetController(self) -> SpreadsheetController:
        return self.controller

    def start_session(self):
        print("Welcome, what action do you want to do?")
        end = False
        while not end:
            self.print_menu()
            action = input()
            command = action.lower()
            try:
                if command == 'f':
                    print('Ending the session...')
                    end = True
                    break
                elif command == "rf":
                    self.controller.read_command_from_file()
                elif command == "c":
                    self.controller.create_spreadsheet()
                elif command == "e":
                    self.controller.edit_cell()
                elif command == "l":
                    self.controller.load_spreadsheet_from_file('awa')
                elif command == "s":
                    self.controller.save_spreadsheet_to_file('awa')
                else:
                    raise InputError("Invalid input")
            except BadCoordinateException as e:
                print(e)
            except ContentException as e:
                print(e)
            except InputError as e:
                print(e)

ui = UI()
controller = ui.get_SpreadsheetController()
controller.create_spreadsheet(3,4)
#print(controller.spreadSheet)
spread = controller.load_spreadsheet_from_file('awa.txt')
print(spread)