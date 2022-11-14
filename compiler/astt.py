'''
structure of the ast:
{
    'type': <KEYWORD>,
    'function': <FUNCTION>,
    'children': <LIST>
}
'''
keywords = ('if', 'endif', 'true', 'false', 'print', 'read')
variables = ();

def ast(lexed:str):
    '''
    makes an action tree out of the lexed data
    '''
    ast = {}
    index = 0
    
    while index < len(lexed):
        current_d = 1
        if lexed[index]['type'] == 'KEYWORD':
            if lexed[index]['value'] in keywords:
                ast.add
                index += 1
                
            else:
                raise Exception("Syntax Error: Unknown keyword or synax error: " + lexed[index]['value'])
    

    return ast