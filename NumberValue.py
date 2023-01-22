from Value import Value

class NumberValue(Value):

    def __init__(self, float_value:int or float):
        self.value = float_value
    
    def get_value(self):
        return self.get_as_float()

    def get_as_string(self):
        return str(self.value)

    def get_as_float(self):
        return self.value
    
    def set_value(self, value):
        self.value = value