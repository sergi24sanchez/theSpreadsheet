from Cell import Cell

class DependenciesManager():

    def __init__(self):
        pass

    def recalculate_dependent_cells(self):
        pass

    def search_cirucular_dependencies(self, cell:Cell):
        #when searching for circular dependencies, raise an exception if circular dependencies == true
        circular_dependencies = True
        for item in cell.get_dependsonme:
            if item not in cell.idependon:
                circular_dependencies = False
        return circular_dependencies

