
# The base token class
class Token:
    '''
    This is the base class for all tokens in the language.
    '''
    def __init__(self,token_type,value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return "Token type:" + str(self.token_type) + " Value:" + str(self.value)

class OperatorToken(Token):
    '''
    This is the token class for every operational token ie. +,-,*,/
    '''
    def __init__(self,token_type,operator_type,value):
        super().__init__(token_type,value)
        self.operator_type = operator_type


class AssignmentToken(Token):
    '''
    This is the token class for the assignment operator ie. =
    '''
    def __init__(self,token_type,value):
        super().__init__(token_type,value)


class Expression:
    def __init__(self,left,operator,right):
        self.left = left
        self.operator = operator
        self.right = right   
    
    def __str__(self):
        return "Left:" + str(self.left) + " Operator:" + str(self.operator) + " right:" + str(self.right)
    
    
    def __repr__(self):
        return self.__str__()
    


class MathExpression(Expression):
    def __init__(self,left,operator,right):
        super().__init__(left,operator,right)
        

class AssignmentExpression(Expression):
    def __init__(self,left,operator,right):
        super().__init__(left,operator,right)
