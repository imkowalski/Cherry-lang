
from cherry_objects import Token,OperatorToken,ParantasisToken,AssignmentToken,VariableToken
from cherry_types import *


def lex(inp: str):
    """
    Lexer for the Cherry language.
    """
    tokens = []
    index = 0
    line = 1
    while True: # while loop to read all the chars in the input one by one
        if index >= len(inp): # if the index is bigger than the length of the input, break the loop means that its done lexing
            break
        elif inp[index] == ' ' or inp[index] == '\t': # ignores spaces and tabs
            index += 1
            continue
        elif inp[index] == '\n': # if the char is a new line, increase the line number and add it as a token
            index += 1
            line += 1
            tokens.append(Token('NEWLINE', '\n'))
        elif (inp[index] in ints):
            temp = ""
            while True:
                if index >= len(inp):
                    break
                if (inp[index] in ints) == False:
                    break
                temp += inp[index]
                index += 1
                
            tokens.append(Token('INT', int(temp)))
        elif inp[index] in operators:
            tokens.append(OperatorToken('OPERATOR',operator_name[inp[index]], inp[index]))
            index += 1
        elif inp[index] in strings:
            sr = inp[index]
            temp = ""

            while True:
                index += 1
                if index >= len(inp):
                    break
                if inp[index] == '\n':
                    raise Exception("Syntax Error: Unclosed string, at line: " + str(line))
                if inp[index] == sr:
                    index += 1
                    break
                
                temp += inp[index]
                
            tokens.append(Token('STRING', temp))
        elif inp[index].upper() in chars:
            temp = ""
            while True:
                if index >= len(inp):
                    break
                if (inp[index].upper() in chars) == False:
                    break
                temp += inp[index]
                index += 1
            tokens.append(Token('CHAR', temp))
        
        elif inp[index] in parantasis:
            tokens.append(ParantasisToken('PARANTASIS', inp[index], parantasis[inp[index]]))
            index += 1
        elif inp[index] == '#':
            temp = ""
            while True:
                if index >= len(inp):
                    break
                if inp[index] == '\n':
                    break

                temp += inp[index]
                index += 1
            tokens.append(Token('COMMENT', temp))
        elif inp[index] == '$':
            temp = ""
            while True:
                if index >= len(inp):
                    break
                if inp[index] == '\n':
                    break
                if inp[index] == '=':
                    break
                if inp[index] == ' ':
                    break
                temp += inp[index]
                index += 1
            tokens.append(VariableToken('VARIABLE', temp))
        elif inp[index] == ',':
            tokens.append(Token('COMMA', inp[index]))
            index += 1
        elif inp[index] == '=':
            tokens.append(AssignmentToken('ASSIGNMENT', inp[index]))
            index += 1
        else:
            raise Exception('Invalid character: ' + inp[index] + ' at line ' + str(line))
    tokens.append(Token('EOF', None))
    return tokens
