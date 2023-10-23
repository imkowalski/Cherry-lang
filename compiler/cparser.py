
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
from cherry_objects import MathExpression,Expression

#function that gnerates an abstract syntax tree
def ast(lexer):
    ast = []
    line = 0
    nodes = {}
    return gen_tree(lexer)
    
 
 
def gen_branch(index, lexer,left = None):
    branch = ""
    current = lexer[index]
    next,nnext = "",""
    highest_index = index
    if current.type != 'NEWLINE' and current.type != "EOF":
        next = lexer[index + 1]
        nnext = lexer[index + 2]
        highest_index = index + 2   
    elif current.type == 'NEWLINE' or current.type == "EOF":
        return ("END_OF_TREE",index+2)
 
    
    end_index = highest_index
    if next.type == "OPERATOR":
        nnnext = lexer[index + 3]
        
        if nnnext.type == "OPERATOR" and priority[nnnext.operator_type] >= priority[next.operator_type]:
            right,end_index = gen_branch(index + 2, lexer)
            if left == None :
                left = current
            else:
                index = left.start
            branch = MathExpression(left, next,right,index,end_index) 
        else:
            if left == None :
                left = current
            else:
                index = left.start            
            branch = MathExpression(left, next, nnext,index,highest_index)

    if end_index == highest_index:
        return (branch,highest_index)
    else:
        return (branch,end_index)
 


    
    
 
        
def gen_tree(lexer):
    index = 0
    previous = None
    while True:
        branch,index = gen_branch(index, lexer,previous)
        if lexer[index].type == "EOF" or lexer[index].type == "NEWLINE":
            break;
        previous = branch
    return previous
            
        
