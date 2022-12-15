class Argument():

    def __init__(self) -> None:
        pass


class Range(Argument):

    def __init__(self) -> None:
        super().__init__()
        self.initial_cell = None
        self.final_cell = None
    
    def get_initial_cell(self):
        return self.initial_cell
    
    def get_final_cell(self):
        return self.final_cell

    def get_all_range_of_cells(self) -> list:
        # THIS METHOD STILL HAS TO BE IMPLEMENTED
        pass


class Number(Argument):

    def __init__(self, input_number) -> None:
        super().__init__()
        self.number_value = int(input_number)

    def get_number_value(self):
        return self.number_value