import Spreadsheet
import pandas as pd
import utils

class SpreadsheetPrinter:

    def __init__(self):
        pass

    def show_all_spreadsheet(self,spreadsheet:Spreadsheet):
        cols = []
        for col in range(spreadsheet.get_ncols()):
            cols.append(utils.column_number_to_letter(col+1))
        dataframe_to_print = pd.DataFrame(index=pd.RangeIndex(1, (spreadsheet.get_nrows()+1)), columns=cols)
        
        dataframe = spreadsheet.get_cells()
        for i in range(1, spreadsheet.get_nrows()+1):
            for j in range(1, spreadsheet.get_ncols()+1):
                col = utils.column_number_to_letter(j)
                cell_content = dataframe.at[i,col].get_content()
                if cell_content is not None:
                    dataframe_to_print.at[i,col] = cell_content.get_for_print()
                else:
                    dataframe_to_print.at[i,col] = ''

        print(dataframe_to_print)