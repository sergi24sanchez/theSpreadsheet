import re
from re import compile as re_compile
from collections import deque

class TokenInfo:
    def __init__(self, regex, type_):
        self.regex = regex
        self.type = type_


class Token:
    def __init__(self, type_, sequence):
        self.type = type_
        self.sequence = sequence

    def is_of_type(self, type_):
        return self.type == type_
    
    def get_sequence(self):
        return self.sequence


from enum import Enum

class TokenEnum(Enum):
    NUMBER = 1
    RANGE = 2
    CELL = 3
    OPERATOR = 4
    LEFT_BRACKET = 5
    RIGHT_BRACKET = 6
    SEMI_COLON = 7
    FUNCTION = 8


class ParserException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Tokenizer:
    def __init__(self):
        self.token_infos = deque()
        self.adds_tokenizer()

    def add(self, regex, type_):
        self.token_infos.append(
            TokenInfo(re_compile("^(" + regex + ")"), type_)
        )

    def adds_tokenizer(self):
        self.add("SUMA|MIN|MAX|PROMEDIO", TokenEnum.FUNCTION) # function
        self.add("[a-zA-Z]+\\d+:[a-zA-Z]+\\d+", TokenEnum.RANGE) #Cell Range
        self.add("\\(", TokenEnum.LEFT_BRACKET) # open bracket
        self.add("\\)", TokenEnum.RIGHT_BRACKET) # close bracket
        self.add("[+-]", TokenEnum.OPERATOR) # plus or minus
        self.add("[*/]", TokenEnum.OPERATOR) # mult or divide
        self.add("\\^", TokenEnum.OPERATOR) # raised
        self.add("[0-9]+", TokenEnum.NUMBER) # integer number
        self.add("[a-zA-Z]+\\d+", TokenEnum.CELL) #cell
        self.add(";", TokenEnum.SEMI_COLON) #Argument separator

    # @staticmethod
    def tokenize(self, s: str):
        tokens = deque()
        s = s.strip()
        while s != "":
            match = False
            for info in self.token_infos:
                m = info.regex.match(s)
                if m:
                    match = True
                    tok = m.group().strip()
                    s = re.sub(info.regex, "", s, count=1).strip()
                    tokens.append(Token(info.type, tok))
                    break
            if not match:
                raise ParserException(f"Unexpected character in input: {s}")
        return tokens