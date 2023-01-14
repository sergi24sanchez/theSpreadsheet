from typing import List
from Tokenizer import Tokenizer, ParserException, Token, TokenEnum
from Parser_ import Parser
from ExpressionGenerator import PostFixGenerator
from ExpressionEvaluator import PostfixEvaluator

from FormulaFactory import FormulaFactory

from Content import Formula

# TYPES OF FORMULA COMPONENT
from Component import Component, Operator, OperatorEnum
from Cell import Cell
from Range import Range
from Number import Number
from Function import Function, Max, Min, Promedio, Suma

class FormulaProcessor:

    def __init__(self) -> None:
        self.tokenizer = Tokenizer()
        self.parser = Parser(self.tokenizer.token_infos)
        self.generator = PostFixGenerator()
        #self.evaluator = PostfixEvaluator()

    # ENCARA NO PODEM CRIDAR A SPREADSHEE
    # def create_formula(self, input_string:str, spreadsheet)-> Formula:
    def create_formula(self, input_string:str)-> Formula:
        # Generate token sequence from input string
        token_sequence = self.tokenizer.tokenize(input_string)
        # Check formula syntax
        self.parser.parse(token_sequence)
        # Generate Postfix expression as tokens
        postfix_expression_as_tokens = self.generator.generate_expression(token_sequence)
        # Convert List[Token] into List[Component]
        @staticmethod
        def convert_tokens_into_components(tokens:List[Token])->List[Component]:
            list_of_components = []
            count = 0
            while count < len(tokens):
                token = tokens[count]
                if token.type == TokenEnum.NUMBER:
                    number = Number(number=float(token.get_sequence()))
                    list_of_components.append(number)

                elif token.type == TokenEnum.RANGE:
                    range_cells = Range(range=token.get_sequence())
                    list_of_components.append(range_cells)

                # elif token.type == TokenEnum.CELL:
                    # fer un get de la cela
                    # cela = spreadsheet.get_cell(token.get_sequence())
                    # list_of_components.append()

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
                    # DE MOMENT NO PODEM CRIDAR A SPREADSHEET
                    # def genera_funcion(tokens,inicio,final,spreadsheet=spreadsheet):
                    def genera_funcion(tokens,inicio,final):
                        arguments = []
                        function_tokens = tokens[inicio:final]  # name&( tokens are included
                        i = 0
                        while i < len(function_tokens)-2:
                            token = function_tokens[i+2]
                            if token.type == TokenEnum.RANGE:
                                range_arg = Range(range=token.get_sequence())
                                arguments.append(range_arg)
                            # elif token.type == TokenEnum.CELL:
                            #     cela_arg = spreadsheet.get_cell(token.get_sequence())
                            #     arguments.append(cela_arg)
                            elif token.type == TokenEnum.NUMBER:
                                number_arg = Number(number=float(token.get_sequence()))
                                arguments.append(number_arg)
                            elif token.type == TokenEnum.FUNCTION:
                                n_functions = 0
                                if token.get_sequence() in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                                    n_functions +=1 
                                # SALTAR DIRECTAMENT AL PRIMER ARGUMENT DE LA FUNCIO
                                inner_count = i +2
                                while n_functions > 0:
                                    s = tokens[inner_count].get_sequence()
                                    if s in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                                        n_functions +=1
                                    elif s == ')':
                                        n_functions -=1
                                    inner_count +=1
                                inner_count -=1
                                function_arg = genera_funcion(tokens,inicio=i,final=inner_count)
                                arguments.append(function_arg)
                                # JUMP FINS AL L_BRACKET DE LA FUNCIÓ
                                i = inner_count
                            i +=1

                        initial_token = tokens[inicio].get_sequence()
                        if initial_token == "SUMA":
                            func = Suma(arguments)
                        elif initial_token == "MIN":
                            func = Min(arguments)
                        elif initial_token == "MAX":
                            func = Max(arguments)
                        elif initial_token == "PROMEDIO":
                            func = Promedio(arguments)
                        
                        return func

                    n_functions = 0
                    if token.get_sequence() in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                        n_functions +=1
                    # SALTAR AL PRIMER ARGUMENT DE LA FUNCIO
                    inner_count = count +2
                    while n_functions > 0:
                        s = tokens[inner_count].get_sequence()
                        if s in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                            n_functions +=1
                        elif s == ')':
                            n_functions -=1
                        inner_count +=1
                    # GO BACK TO THE L_BRACKET OF THE FUNCTION
                    inner_count -=1
                    function_comp = genera_funcion(tokens,inicio=count,final=inner_count)
                    list_of_components.append(function_comp)
                    # JUMP FINS AL L_BRACKET DE LA FUNCIÓ
                    count = inner_count
                count +=1
        
        postfix_as_components = convert_tokens_into_components(postfix_expression_as_tokens)

        return postfix_as_components
                        
    def recalculate_formula_value(formula:Formula):
        pass

def main():
    
    string = input("Enter string: ")
    formula_processor = FormulaProcessor()

    postfix_components = formula_processor.create_formula(string)

    for elem in postfix_components:
        print(elem)

if __name__ == "__main__":
    main()