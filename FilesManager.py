from Spreadsheet import Spreadsheet
from utils import column_number_to_letter
import pandas as pd
class FilesManager():

    def __init__(self):
        pass

    def load_spreadsheet(self, path):
        #crea sempre una fila i columna de mes
        with open('awa.txt', 'r') as file:
            lines = file.readlines()
            ncols = len(lines)
            nrows = []
            for line in lines:
                row_no_n = line.split('\n')[0]
                print(row_no_n)
                nrows.append(len(row_no_n.split(';')))
            nrows = min(nrows)
            print(f'awa cols ={ncols} rows = {nrows}')
            spreadsheet = Spreadsheet(nrows, ncols)
            for idline, line in enumerate(lines):
                content = line.split(';')
                for idcol, cell in enumerate(content):
                    print(cell)
                    spreadsheet.get_cells().at[idline+1, column_number_to_letter(idcol+1)] = cell
            print(spreadsheet.get_cells())
        return spreadsheet.get_cells()

            
            
            
            
        

    def save_spreadsheet(self, path:str, spreadsheet:Spreadsheet):
        #crec q sobra un ; del final de linia
        df = spreadsheet.get_cells()
        cols = spreadsheet.get_ncols()
        txt = ''
        for i, row in df.iterrows():
            for j, cell in row.items():
                if (cell == '') or (str(cell) == 'nan'):
                    txt = f'{txt};'
                elif (j == cols):
                    txt = f'{txt}{cell}'
                else:
                    txt = f'{txt}{cell};'
            #s'ha de treure el \n de la ultima linia
            txt = f'{txt}\n'
        
        f= open(path,"w+")
        f.write(txt)
        f.close()

    """ def save_spreadsheet(self, path:str, spreadsheet:Spreadsheet):
        #crec q sobra un ; del final de linia
        df = spreadsheet.get_cells()
        cols = spreadsheet.get_ncols()
        txt = ''
        for row in df.iterrows():
            for col in range(cols):
                if ((row[column_number_to_letter(col+1)]) == ''):
                    txt = f'{txt};'
                else:
                    txt = f'{txt}{row[col]};'
            txt = f'{txt}\n'
        
        f= open(path,"w+")
        f.write(txt)
        f.close()

 """