from Element import Element

class Structure:

    def __init__(self) -> None:
        self.elements = []
    
    def add_element(self,element:Element):
        self.elements.append(element)