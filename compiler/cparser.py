
'''
Node Structure:
[
    {
        "type": <EXPRESSION | COMMAND | ASSIGNMENT>,
        "left": <STRING | VARIABLE>,
        "operator": <OPERATOR>,
        "right": <STRING | VARIABLE | INT | FUNCTION | EXPRESSION>,
    }
]
'''
from cherry_types import *


#function that gnerates an abstract syntax tree
def ast(lexer):
    ast = []
    line = 0
    nodes = {}
    return gen_tree(0, lexer)
    
 
 
def gen_tree(index, lexer):
    current = lexer[index]
    if current != '\n':
        next = lexer[index + 1]
    
    
 
        

