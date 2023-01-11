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

    def generate_expression(self, tokens: List[Token]) -> List[Token]:
        '''This method should return the postfix expression as a sequence of FormulaComponents'''
        stack = []
        output_list = []
        arguments = 0
        number_pattern = re.compile("-?\\d+(\\.\\d+)?")
        cell_pattern = re.compile("^([a-zA-Z]+)(\\d+)$")
        range_pattern = re.compile("[a-zA-Z]+\\d+:[a-zA-Z]+\\d+")

        for token in tokens:
            s = token.sequence
            if number_pattern.match(token.get_sequence()) or cell_pattern.match(token.get_sequence()) or range_pattern.match(token.get_sequence()):
                output_list.append(token)
            elif s == ";":
                arguments += 1
            elif s in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                stack.append(token)
                arguments += 1
            elif s == "(":
                stack.append(token)
            elif s == ")":
                while stack and stack[-1].get_sequence() != "(":
                    output_list.append(stack.pop())
                if stack and stack[-1].get_sequence() == "(": # pop the matching parenthesis
                    stack.pop()
                else:
                    raise ValueError("Mismatched Parenthesis")
                for func in FunctionEnum:
                    if stack and stack[-1].get_sequence() == func.name:
                        self.function_arguments.append(arguments)
                        arguments = 0
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
    postfix_generator = PostFixGenerator()
    string = input("Enter string: ")
    try:
        tokenizer.tokenize(string)

        print("INFIX:")
        print([token.get_sequence() for token in tokenizer.get_tokens()])
        output = postfix_generator.generate_expression(tokenizer.get_tokens())
        print("POSTFIX")
        print([token.get_sequence() for token in output])
        
    except ParserException as ex:
        print(ex)

if __name__ == "__main__":
    main()