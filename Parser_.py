from Tokenizer import Token, TokenInfo, TokenEnum, ParserException
from typing import List

class Parser:

    def __init__(self,token_infos):
        self.valid_tokens = {}

        for token_enum in token_infos:
            if token_enum.type == TokenEnum.OPERATOR:
                valid_tokens = [
                    TokenEnum.NUMBER, TokenEnum.LEFT_BRACKET, TokenEnum.CELL,
                    TokenEnum.FUNCTION, TokenEnum.RANGE,
                ]
                self.valid_tokens.update({TokenEnum.OPERATOR:valid_tokens})
            elif token_enum.type == TokenEnum.CELL:
                valid_tokens = [
                    TokenEnum.SEMI_COLON, TokenEnum.OPERATOR, TokenEnum.RIGHT_BRACKET,
                ]
                self.valid_tokens.update({TokenEnum.CELL:valid_tokens})
            elif token_enum.type == TokenEnum.NUMBER:
                valid_tokens = [
                    TokenEnum.SEMI_COLON, TokenEnum.OPERATOR, TokenEnum.RIGHT_BRACKET,
                ]
                self.valid_tokens.update({TokenEnum.NUMBER:valid_tokens})
            elif token_enum.type == TokenEnum.LEFT_BRACKET:
                valid_tokens = [
                    TokenEnum.CELL, TokenEnum.NUMBER, TokenEnum.FUNCTION,
                    TokenEnum.RANGE,
                ]
                self.valid_tokens.update({TokenEnum.LEFT_BRACKET:valid_tokens})
            elif token_enum.type == TokenEnum.RIGHT_BRACKET:
                valid_tokens = [
                    TokenEnum.CELL, TokenEnum.NUMBER, TokenEnum.FUNCTION,
                    TokenEnum.SEMI_COLON, TokenEnum.OPERATOR, TokenEnum.RANGE,
                    TokenEnum.RIGHT_BRACKET,
                ]
                self.valid_tokens.update({TokenEnum.RIGHT_BRACKET:valid_tokens})
            elif token_enum.type == TokenEnum.SEMI_COLON:
                valid_tokens = [
                    TokenEnum.CELL, TokenEnum.NUMBER, TokenEnum.FUNCTION,
                    TokenEnum.RANGE,
                ]
                self.valid_tokens.update({TokenEnum.SEMI_COLON:valid_tokens})
            elif token_enum.type == TokenEnum.FUNCTION:
                valid_tokens = [
                    TokenEnum.LEFT_BRACKET,
                ]
                self.valid_tokens.update({TokenEnum.FUNCTION:valid_tokens})
            elif token_enum.type == TokenEnum.RANGE:
                valid_tokens = [
                    TokenEnum.SEMI_COLON, TokenEnum.RIGHT_BRACKET,
                ]
                self.valid_tokens.update({TokenEnum.RANGE:valid_tokens})

    def parse(self, tokens:List[Token]):

        for position, token in enumerate(tokens):
            if position == len(tokens) -1:
                break
            if tokens[position+1].type not in self.valid_tokens.get(token.type):
                raise ParserException(f'{tokens[position+1].get_sequence()} can not be after {token.get_sequence()}')

        return True