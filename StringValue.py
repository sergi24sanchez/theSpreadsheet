from Value import Value
from src.edu.upc.etsetb.arqsoft.spreadsheet.entities.no_number_exception import NoNumberException

class StringValue(Value):

    def __init__(self, string_value):
        self.value = string_value
    
    def get_value(self):
        return self.get_as_string()

    def get_as_string(self):
        return self.value
    
    def get_as_float(self):
        try:
            return float(self.value)
        except:
            raise NoNumberException("Unable to convert the value to a string")
        
    def set_value(self, value):
        self.value = value