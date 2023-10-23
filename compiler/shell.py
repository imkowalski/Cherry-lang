import cparser
import interpreter
import lexer

data = ""

with open('test.che', 'r') as f:
    data = f.read()
lexed = lexer.lex(data)
    
ast = cparser.ast(lexed)

print(interpreter.interpreter(ast))
