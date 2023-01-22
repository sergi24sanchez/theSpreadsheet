from typing import List
from Spreadsheet import Spreadsheet
from Coordinate import Coordinate

from Tokenizer import Tokenizer, ParserException, Token, TokenEnum
from Parser_ import Parser
from ExpressionGenerator import ExpressionGenerator, PostFixGenerator
from ExpressionEvaluator import ExpressionEvaluator, PostfixEvaluator

from Content import Formula

# TYPES OF FORMULA COMPONENT
from Component import Component, Operator, OperatorEnum
from Cell import Cell
from Range import Range
from Number import Number
from Function import Function, Max, Min, Promedio, Suma

from NumberValue import NumberValue

class FormulaProcessor:

    def __init__(self, tokenizer:Tokenizer,
        parser:Parser,
        generator:ExpressionGenerator,
        evaluator:ExpressionEvaluator,
    ) -> None:
        self.tokenizer = tokenizer
        self.parser = parser
        self.generator = generator
        self.evaluator = evaluator

    def create_formula(self, input_string:str, spreadsheet:Spreadsheet)-> Formula:
        # Generate token sequence from input string
        without_equal_char = input_string.split("=")[1]
        token_sequence = self.tokenizer.tokenize(without_equal_char)
        # Check formula syntax
        self.parser.parse(token_sequence)
        # Generate Postfix expression as tokens
        postfix_expression_as_tokens = self.generator.generate_expression(token_sequence)
        # Convert List[Token] into List[Component]
        postfix_expression_as_components = self.convert_tokens_into_components(
            postfix_tokens=postfix_expression_as_tokens,
            spreadsheet=spreadsheet,
        )

        formula = Formula(input_string=input_string)
        formula.set_components(postfix_expression_as_components)

        return formula
    
    def compute_value_of_formula(self,formula:Formula):
        calculated_value = self.evaluator.evaluate_expression(formula.get_components())
        return calculated_value
    
    def convert_tokens_into_components(self,postfix_tokens:List[Token],spreadsheet:Spreadsheet)->List[Component]:
        list_of_components = []
        count = 0
        while count < len(postfix_tokens):
            token = postfix_tokens[count]
            if token.type == TokenEnum.NUMBER:
                number = Number(number=float(token.get_sequence()))
                list_of_components.append(number)

            elif token.type == TokenEnum.CELL:
                cell = spreadsheet.get_cell(
                    Coordinate(token.get_sequence())
                )
                list_of_components.append(cell)

            elif token.type == TokenEnum.OPERATOR:
                if token.get_sequence() == '+':
                    suma_operator = Operator(type_=OperatorEnum.SUMA,token_=token)
                    list_of_components.append(suma_operator)
                elif token.get_sequence() == '-':
                    resta_operator = Operator(type_=OperatorEnum.RESTA,token_=token)
                    list_of_components.append(resta_operator)
                elif token.get_sequence() == '*':
                    mult_operator = Operator(type_=OperatorEnum.MULT,token_=token)
                    list_of_components.append(mult_operator)
                elif token.get_sequence() == '/':
                    div_operator = Operator(type_=OperatorEnum.DIV,token_=token)
                    list_of_components.append(div_operator)

            elif token.type == TokenEnum.FUNCTION:
                
                n_functions = 0
                if token.get_sequence() in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                    n_functions +=1
                # SALTAR AL PRIMER ARGUMENT DE LA FUNCIO
                inner_count = count +2
                while n_functions > 0:
                    s = postfix_tokens[inner_count].get_sequence()
                    if s in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                        n_functions +=1
                    elif s == ')':
                        n_functions -=1
                    inner_count +=1
                # GO BACK TO THE L_BRACKET OF THE FUNCTION
                inner_count -=1
                function_component = self.generate_function(
                    token_list=postfix_tokens,
                    init=count,
                    final=inner_count,
                    spreadsheet=spreadsheet,
                )
                list_of_components.append(function_component)
                # JUMP FINS AL L_BRACKET DE LA FUNCIÓ
                count = inner_count
            count +=1

        return list_of_components

    def generate_function(self,token_list:List[Token],init:int,final:int,spreadsheet:Spreadsheet)->Function:
        arguments = []
        function_tokens = token_list[init:final+1]  # name&( tokens are included
        i = 2   # TO START FROM THE FIRST ARGUMENT
        while i < len(function_tokens):
            token = function_tokens[i]
            if token.type == TokenEnum.NUMBER:
                number_arg = Number(number=float(token.get_sequence()))
                arguments.append(number_arg)
            elif token.type == TokenEnum.RANGE:
                range_obj = Range(range=token.get_sequence())
                for cell in range_obj.get_all_cells(spreadsheet):
                    arguments.append(cell)
            elif token.type == TokenEnum.CELL:
                cell = spreadsheet.get_cell(
                    Coordinate(token.get_sequence())
                )
                arguments.append(cell)
            elif token.type == TokenEnum.FUNCTION:
                n_functions = 0
                if token.get_sequence() in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                    n_functions +=1 
                # SALTAR DIRECTAMENT AL PRIMER ARGUMENT DE LA FUNCIO
                inner_count = i +2
                while n_functions > 0:
                    s = function_tokens[inner_count].get_sequence()
                    if s in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                        n_functions +=1
                    elif s == ')':
                        n_functions -=1
                    inner_count +=1
                inner_count -=1
                function_arg = self.generate_function(
                    token_list=function_tokens,
                    init=i,
                    final=inner_count,
                    spreadsheet=spreadsheet,
                )
                arguments.append(function_arg)
                # JUMP FINS AL L_BRACKET DE LA FUNCIÓ
                i = inner_count
            i +=1

        initial_token = token_list[init].get_sequence()
        if initial_token == "SUMA":
            func = Suma(arguments)
        elif initial_token == "MIN":
            func = Min(arguments)
        elif initial_token == "MAX":
            func = Max(arguments)
        elif initial_token == "PROMEDIO":
            func = Promedio(arguments)
        
        return func

    def refresh_depending_cells(self,changed_cell:Cell)->None:

        changed_content = changed_cell.get_content()
        if isinstance(changed_content,Formula):
            formula_components = changed_content.get_components()
            idependon = []
            for comp in formula_components:
                if comp not in idependon:
                    if isinstance(comp,Cell):
                        idependon.append(comp)
                    elif isinstance(comp,Function):
                        idependon_from_function = self.get_function_idependon(comp)
                        for c in idependon_from_function:
                            if c not in idependon:
                                idependon.append(c)
            
            changed_cell.set_idependon(cells=idependon)

            for cell in idependon:
                cell.add_dependsonme(changed_cell)

    def get_function_idependon(self,function:Function)->List[Cell]:
        arguments = function.arguments
        idependon_function = []
        for cell in arguments:
            if isinstance(cell,Cell):
                idependon_function.append(cell)
            elif isinstance(cell,Function):
                idependon_inner_function = self.get_function_idependon(cell)
                for inner_cell in idependon_inner_function:
                    if inner_cell not in idependon_function:
                        idependon_function.append(inner_cell)
        return idependon_function

        

def main():
    
    tokenizer = Tokenizer()
    parser = Parser(tokenizer.token_infos)
    generator = PostFixGenerator()
    evaluator = PostfixEvaluator()
    formula_processor = FormulaProcessor(tokenizer, parser, generator, evaluator)

    string = input("Enter string: ")
    formula_obj = formula_processor.create_formula(string)

    print("FORMULAbjALUE:")
    print(formula_obj.get_for_print())

if __name__ == "__main__":
    main()