from SpreadsheetController import SpreadsheetController
from UI import UI
from FormulaFactory import FormulaFactory

def __main__():
    controller = SpreadsheetController()
    ui = UI()
    status = 0
    while(status==0):
        status = ui.start_session(controller)

if __name__ == "__main__":
    __main__()