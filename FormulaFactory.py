from Tokenizer import Tokenizer, ParserException, Token, TokenEnum
from Parser_ import Parser
from ExpressionGenerator import PostFixGenerator
from ExpressionEvaluator import PostfixEvaluator
from FormulaProcessor import FormulaProcessor

class FormulaFactory:
    def __init__(self) -> None:
        pass

    def get_formula_processor(self):
        tokenizer = Tokenizer()
        parser = Parser(self.tokenizer.token_infos)
        generator = PostFixGenerator()
        evaluator = PostfixEvaluator()
        formula_processor = FormulaProcessor(tokenizer, parser, generator, evaluator)
        return formula_processor