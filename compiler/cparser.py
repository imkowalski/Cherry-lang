
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
    return gen_nodes(0, lexer)
    
        

class Expression:
    def __init__(self,left,operator,right):
        self.left = left
        self.operator = operator
        self.right = right   
    
    def __str__(self):
        return "Left:" + str(self.left) + " Operator:" + str(self.operator) + " right:" + str(self.right)
    
    
    def __repr__(self):
        return self.__str__()