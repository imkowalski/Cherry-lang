chars = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
ints = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

operators = ('+', '-', '*',"%", '/')
operator_name = {
    '+': 'ADDITION',
    '-': 'SUBTRACTION',
    '%': 'MODULO',
    '*': 'MULTIPLICATION',
    '/': 'DEVISION',
}
operators_type = [
    'ADDITION',
    'SUBTRACTION',
    'MODULO',
    'MULTIPLICATION',
    'DEVISION'
]

parantasis = ('(', ')')
parantasis_name = {
    '(': 'LEFT_PARANTHASIS',
    ')': 'RIGHT_PARANTHASIS',
}

strings = ('"', "'")
assignment = '='

types = ["KEYWORD", "VARIABLE", "STRING", "INT", "FUNCTION", "OPERATOR"]

ibuilt_in_function = ["print","get"]

priority = {
    "ADDITION": 1,
    "SUBTRACTION": 1,
    "MULTIPLICATION": 2,
    "DEVISION": 2,
    "MODULO": 2,
    "EXPONENT": 3,
    "LEFT_PARANTHASIS": 4,
    "RIGHT_PARANTHASIS": 4,
}