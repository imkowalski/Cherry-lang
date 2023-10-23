import cparser

import lexer

data = ""

with open('test.che', 'r') as f:
    data = f.read()
lexed = lexer.lex(data)
print(lexed)
    
(cparser.ast(lexed))
