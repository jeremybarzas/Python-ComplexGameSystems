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
        # parse expression adding strings into clauses determined by () and operators { "(" = 40, ")" = 41 }        
        clause = ""
        clausefound = False
        for char in self.expression:
            c = ord(char)                
            if(c == 40):                    
                clausefound = True
            if(clausefound):
                clause += char
            if(c == 41):
                clausefound = False
                self.clauses.append(clause)
                clause = ""
        return

    # calcualte and assign pairs
    def get_pairs(self):
        # parse input adding a tuple of each input character + each variable into pairs
        newvars = []
        variable = ''
        for char in self.expression:
            c = ord(char)
            if(c == 33):
                variable = char
                continue
            if(c >= 97 and c <= 122) or (c >= 65 and c <= 90):
                if(variable == ''):
                    if(newvars.__contains__(char) == False):
                        # add to variables
                        variable += char
                        newvars.append(variable)
                        variable = ''
                else:
                    # add to variables
                    variable += char
                    newvars.append(variable)
                    variable = ''

        for var in newvars:
            tup = (var, '')
            self.pairs.append(tup)          
        return

def main():
    parser = Parser()
    formula = '(a) * (b) * (!c) * (!d)'
    parser.set_expression(formula)
    parser.get_variables()
    parser.get_clauses()
    parser.get_pairs()

    print parser.expression
    print parser.variables
    print parser.clauses
    print parser.pairs
    
if __name__ == "__main__":
    main()
