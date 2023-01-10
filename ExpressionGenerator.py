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

    def get_precedence(ch):
        if ch in ["+", "-"]:
            return 2
        elif ch in ["*", "/"]:
            return 3
        elif ch in ["(", ")", ";", "SUMA", "MAX", "MIN", "PROMEDIO"]:
            return 1
        else:
            return -1

    def generate_expression(self, tokens:List[Token]) -> List[Token]:

        stack = []
        outputList = []
        arguments = 0
        number_pattern = re.compile("-?\\d+(\\.\\d+)?")
        cell_pattern = re.compile("^([a-zA-Z]+)(\\d+)$")
        range_pattern = re.compile("[a-zA-Z]+\\d+:[a-zA-Z]+\\d+")

        for token in tokens:
            s = token.sequence
            if number_pattern.match(token.sequence) or cell_pattern.match(token.sequence) or range_pattern.match(token.sequence):
                outputList.append(token)
            elif s == ";":
                arguments += 1
            elif s in ["SUMA", "MAX", "MIN", "PROMEDIO"]:
                stack.append(token)
                arguments += 1
            elif s == "(":
                stack.append(token)
            elif s == ")":
                while stack and stack[-1].sequence[0] != "(":
                    outputList.append(stack.pop())

                stack.pop()
                for func in FunctionEnum:
                    if stack and stack[-1].sequence == func.name:
                        self.function_arguments.append(arguments)
                        arguments = 0
            else:   # If an operator is encountered then taken the further action based on the precedence of the operator
                if stack:
                    while self.get_precedence(s) <= self.get_precedence(stack[-1].sequence):
                        outputList.append(stack.pop())
                stack.append(token)
        # if the token is a letter extract letter an following nummber and extract value from that cell
        # threat it as a operand
        while stack:    # pop all the remaining operators from the stack and append them to output
            outputList.append(stack.pop())
        return outputList

    # def generate_expression(self, tokens:List[Token])-> List[Token]:
    #     """
    #     The Shunting Yard Algorithm.
    #     infix  : str : an infix mathematical expression.
    #     """
    #     specials = {'': 50, '.': 40, '|': 30}

    #     postfix = []
    #     stack = []

    #     for token in tokens:
    #         s = token.sequence
    #         if s == '(':
    #             stack.append(s)
    #         elif s == ')':
    #             while stack[-1] != '(':
    #                 postfix.append(stack.pop())
    #             stack.pop()
    #         elif s in specials:
    #             while stack and specials.get(s, 0) <= specials.get(stack[-1], 0):
    #                 postfix.append(stack.pop())
    #             stack.append(s)
    #         else:
    #             postfix.append(s)

    #     while stack:
    #         postfix.append(stack.pop())

    #     return postfix


def main():
    tokenizer = Tokenizer()
    postfix_generator = PostFixGenerator()
    string = input("Enter string: ")
    try:
        tokenizer.tokenize(string)

        # for token in tokenizer.get_tokens():
        #     print(token.sequence)
        
        output = postfix_generator.generate_expression(tokenizer.get_tokens())

        for token in output:
            print(token.sequence)
        
    except ParserException as ex:
        print(ex)

if __name__ == "__main__":
    main()