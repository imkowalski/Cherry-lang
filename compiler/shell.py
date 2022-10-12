import astt
import lexer

data = ""

with open('test.che', 'r') as f:
    data = f.read()
lexed = lexer.lex(data)
#print(astt.ast(lexed))
for value in lexed:
    print(value)