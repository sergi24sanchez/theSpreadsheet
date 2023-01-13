from Parser_ import Parser
from abc import ABC, abstractclassmethod

class ExpressionGenerator(ABC):

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def generate_expression(self):
        pass

import re
from typing import List
from Tokenizer import Token, Tokenizer, ParserException
from Parser_ import Parser
from Function import FunctionEnum

class PostFixGenerator(ExpressionGenerator):

    def __init__(self):
        self.function_arguments = []

    def get_function_arguments(self):
        return self.function_arguments

    def letter_or_digit(c):
        if c.isalnum(): # operand
            return True
        else:
            return False

    def get_precedence(self,ch):
        if ch in ["+", "-"]:
            return 2
        elif ch in ["*", "/"]:
            return 3
        elif ch in [")"]:
            return 4
        elif ch in [";", "SUMA", "MAX", "MIN", "PROMEDIO"]:
            return 1
        elif ch in ["("]:
            return 0
        else:
            return -1

    # @staticmethod
    def generate_expression(self, tokens: List[Token]) -> List[Token]:
        '''This method should return the postfix expression as a sequence of FormulaComponents'''
        stack = []
        output_list = []
        n_functions = 0
        number_pattern = re.compile("-?\\d+(\\.\\d+)?")
        cell_pattern = re.compile("^([a-zA-Z]+)(\\d+)$")
        range_pattern = re.compile("[a-zA-Z]+\\d+:[a-zA-Z]+\\d+")

        for token in tokens:
            s = token.get_sequence()
            # LOOP FOR TREATING THE ARGUMENTS OF A FUNCTION (ADD DIRECTLY TO THE OUTPUT)
            if n_functions > 0:
                output_list.append(token)
                if s in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                    n_functions += 1
                elif s == ")":
                    n_functions -= 1
                # Go fo the next token
                continue
            
            if number_pattern.match(token.get_sequence()) or cell_pattern.match(token.get_sequence()) or range_pattern.match(token.get_sequence()):
                output_list.append(token)
            elif s == ";":
                pass
            elif s in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                output_list.append(token)
                n_functions += 1

            elif s == "(":
                stack.append(token)
            elif s == ")":
                while stack and stack[-1].get_sequence() != "(":
                    output_list.append(stack.pop())
                if stack and stack[-1].get_sequence() == "(": # pop the matching parenthesis
                    stack.pop()
                else:
                    raise ValueError("Mismatched Parenthesis")

            else:   # If an operator is encountered then taken the further action based on the precedence of the operator
                if stack:
                    while (stack and 
                        self.get_precedence(stack[-1].get_sequence()) >= self.get_precedence(s)):
                        output_list.append(stack.pop())
                stack.append(token)
        while stack:    # pop all the remaining operators from the stack and append them to output
            if stack[-1].sequence == '(':
                raise ValueError("Mismatched Parenthesis")
            output_list.append(stack.pop())
        return output_list


def main():
    tokenizer = Tokenizer()
    parser = Parser(tokenizer.token_infos)
    postfix_generator = PostFixGenerator()
    string = input("Enter string: ")
    try:
        token_sequence = tokenizer.tokenize(string)

        print("INFIX:")
        print([token.get_sequence() for token in token_sequence])
        if parser.parse(token_sequence):
            output = postfix_generator.generate_expression(token_sequence)
        print("POSTFIX")
        print([token.get_sequence() for token in output])
        
    except ParserException as ex:
        print(ex)

if __name__ == "__main__":
    main()