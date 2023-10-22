
'''
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
    line = 0;
    nodes = {}
    return gen_branch(0, lexer)
    
        

def gen_branch(index, lexer):
    current = lexer[index]
    branch = {}
    next = lexer[index+1]
    if next["type"] == "EOF":
        print("EOF")
        return current["value"]
    
    print(current,next)
    if next["type"] == "OPERATOR":
        branch["type"] = "EXPRESSION"
        if next["operator_type"] in operators_type:
            branch["left"] = current["value"]
            branch["operator"] = [k for k, v in operator_name.items() if v == next["operator_type"]][0]
            branch["right"] = gen_branch(index+2, lexer)
            return branch
    if current["type"] in parantasis_name.values():
        if next["type"] == "LEFT_PARANTHASIS":
            gen_branch(index+1, lexer)

        
        
        
        
        
    
       