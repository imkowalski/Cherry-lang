
"""
OPERATORS:
PLUS + 
MINUS -
MULTIPLICATION *
DEVISION /

Token Schema:
{type: <type>, value: <value>}
"""


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
            tokens.append({'type': 'NEWLINE', 'value': '\n'})
        elif (inp[index] in ints):
            temp = ""
            while True:
                if index >= len(inp):
                    break
                if (inp[index] in ints) == False:
                    break
                temp += inp[index]
                index += 1
                
            tokens.append({'type': 'INT', 'value': temp})
        elif inp[index] in operators:
            tokens.append({'type': "OPERATOR",'operator_type':operator_name[inp[index]], 'value': inp[index]})
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
                
            tokens.append({'type': 'STRING', 'value': temp})
        elif inp[index].upper() in chars:
            temp = ""
            while True:
                if index >= len(inp):
                    break
                if (inp[index].upper() in chars) == False:
                    break
                temp += inp[index]
                index += 1
            tokens.append({'type': 'KEYWORD', 'value': temp})
        
        elif inp[index] in parantasis:
            tokens.append({'type': parantasis_name[inp[index]], 'value': inp[index]})
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
            tokens.append({'type': 'COMMENT', 'value': temp})
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
            tokens.append({'type': 'VARIABLE', 'value': temp})
        elif inp[index] == ',':
            tokens.append({'type': 'SEPERATOR', 'value': inp[index]})
            index += 1
        elif inp[index] == '=':
            tokens.append({'type': 'ASSIGN', 'value': inp[index]})
            index += 1
        else:
            raise Exception('Invalid character: ' + inp[index] + ' at line ' + str(line))
    tokens.append({'type': 'EOF', 'value': None})
    return tokens
