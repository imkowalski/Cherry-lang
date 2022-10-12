'''
structure of the ast:
{
    'type': <KEYWORD>,
    'function': <FUNCTION>,
    'children': <LIST>
}
'''
keywords = ('if', 'endif', 'else', 'endelse', 'elseif', 'endelseif', 'while', 'endwhile', 'true', 'false', 'print', 'read',"func", "endfunc")
functions = ();
variables = ();
def ast(lexed:str):
    '''
    makes an action tree out of the lexed data
    '''
    ast = {}
    index = 0
    
    while index < len(lexed):
        if lexed[index]['type'] == 'KEYWORD':
            if lexed[index]['value'] in keywords or lexed[index]['value'] in functions:
                index += 1
                continue
            else:
                raise Exception("Syntax Error: Unknown keyword or synax error: " + lexed[index]['value'])
    

    return ast