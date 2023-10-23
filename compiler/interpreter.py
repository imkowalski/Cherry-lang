from cherry_objects import *

def interpreter(ast):
    if isinstance(ast,MathExpression):
        return True
    