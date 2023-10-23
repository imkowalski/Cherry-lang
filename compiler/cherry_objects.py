from colorama import init, Fore
init()
# The base token class
class Token:
    '''
    This is the base class for all tokens in the language.
    '''
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token( " + str(self.type) + " , " + str(self.value) + " )"
    
    def __repr__(self): 
        return self.__str__()

class OperatorToken(Token):
    '''
    This is the token class for every operational token ie. +,-,*,/
    '''
    def __init__(self,type,operator_type,value):
        super().__init__(type,value)
        self.operator_type = operator_type

class ParantasisToken(Token):
    '''
    This is the token class for the parantasis tokens ie. (,)
    '''
    def __init__(self, type,parantasis_type, value):
        super().__init__(type, value)
        self.parantasis_type = parantasis_type

class VariableToken(Token):
    '''
    This is the token class for the variable tokens ie. $
    '''
    def __init__(self, type, value):
        super().__init__(type, value)

class AssignmentToken(Token):
    '''
    This is the token class for the assignment operator ie. =
    '''
    def __init__(self,type,value):
        super().__init__(type,value)


class Expression:
    def __init__(self,left,operator,right,start,end):
        self.left = left
        self.operator = operator
        self.right = right   
        self.start = start
        self.end = end
    
    def __str__(self):
        return Fore.RED+"{\n\tLeft=[" + str(self.left) + "],"+Fore.LIGHTBLUE_EX+"\n\tOperator=(" + str(self.operator) + "),"+Fore.LIGHTGREEN_EX+"\n\tright=[" + str(self.right) + "],\n\t"+Fore.MAGENTA+"start=" + str(self.start) + ",\n\t"+Fore.YELLOW+"end=" + str(self.end) + Fore.RED+"\n}"+Fore.RESET
    
    
    def __repr__(self):
        return self.__str__()
    


class MathExpression(Expression):
    def __init__(self,left,operator,right,start,end):
        super().__init__(left,operator,right,start,end)
        

class AssignmentExpression(Expression):
    def __init__(self,left,operator,right,start,end):
        super().__init__(left,operator,right,start,end)
