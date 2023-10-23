from cherry_objects import *

def interpreter(ast):
    if isinstance(ast,MathExpression):
        return eval(str(interpreter(ast.left)) + str(ast.operator.value) + str(interpreter(ast.right)))
    if isinstance(ast,Token):
        if(ast.type == "INT"):
            return int(ast.value)
    