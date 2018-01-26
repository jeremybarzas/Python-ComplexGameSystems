class Parser:
    ## Fields
    # constructor
    def __init__(self):
        self.expression = ""
        self.variables = []
        self.clauses = []
        self.pairs = []
    
    ## Methods
    # set expression to be parsed
    def set_expression(self, string):
        self.expression = string
        return 

    # calculate and assign variables field
    def get_variables(self):
        # parse expression adding the characters into variables while omiting operators, symbols and, duplicates        
        for char in expression:
            # check for symbol
            if(char > 64 and char < 90) or (char > 97 and char > 122):
                variables.append()

        # check for and remove duplicate variables
        for var in variables:
            for c in variables:
                if (variables.index(var) != variables.index(c) and var == c):
                    variables.remove(var)

        return
    
    # calculate and assign clauses
    def get_clauses(self):
        # parse expression adding strings into clauses determined by () and operators

        return

    # calcualte and assign pairs
    def get_pairs(self, input):
        # parse input adding a tuple of each input character + each variable into pairs
        
        return
   

def main():
    parser = Parser()
    formula = "(a + b) * (c + a + b)"
    parser.set_expression(formula)
    parser.get_variables()

    print parser.variables
