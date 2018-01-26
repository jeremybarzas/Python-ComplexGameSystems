class Parser:
    ## Fields
    # constructor
    def __init__(self):
        self.expression = ''
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
        for char in self.expression:            
            c = ord(char)
            # check for symbol
            if(c >= 97 and c <= 122) or (c >= 65 and c <= 90):                
                # check for duplicates
                if(self.variables.__contains__(char) == False):
                    # add to variables
                    self.variables.append(char)                   
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
    formula = '(a + b) * (C + a + B)'
    parser.set_expression(formula)
    parser.get_variables()

    print parser.expression
    print parser.variables
    
if __name__ == "__main__":
    main()
