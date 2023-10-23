
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
from cherry_objects import MathExpression

#function that gnerates an abstract syntax tree
def ast(lexer):
    ast = []
    line = 0
    nodes = {}
    return gen_tree( lexer)
    
 
 
def gen_branch(index, lexer,left = None):
    branch = ""
    current = lexer[index]
    next,nnext = "",""
    highest_index = index
    if current.type != 'EOF':
        next = lexer[index + 1]
        nnext = lexer[index + 2]
        highest_index = index + 2
    else:
        return (-1,9999999999999)
    
    print(current,next)
    
    end_index = highest_index
    if next.type == "OPERATOR":
        nnnext = lexer[index + 3]
        if nnnext.type == "OPERATOR" and priority[nnnext.operator_type] > priority[next.operator_type]:
            
            if left == None:
                print("left is none")
                left = current
            right,end_index = gen_branch(index + 2, lexer)
            branch = MathExpression(left, next,right,index,end_index) 
        else:
            branch = MathExpression(left, next, nnext,index,highest_index)

    if end_index == highest_index:
        return (branch,highest_index)
    else:
        return (branch,end_index)
 


    
    
 
        
def gen_tree(lexer):
    index = 0
    previous = None
    while index <= len(lexer):
        print(index)
        branch,index = gen_branch(index, lexer,previous)
        previous = branch
        print(branch)
    return previous
        
