import copy
from pyparsing import *

# TODO: check on inequalities is stupid and needs to be improved 
def parse_equations(equations,atom_dict):
    operand = Word(alphas) 
    eqopt  = Literal("<=>")
    negopt = Literal("!")
    expr = infixNotation( operand, [ (negopt, 2, opAssoc.LEFT), (eqopt, 2, opAssoc.RIGHT)])
    equalities,inequalities = [],[]
    for eq in equations:
        result = expr.parseString(eq)
        processed_res = [atom_dict.get(x,"default") for x in equations]
        processed_res = list(filter(lambda a: a != "default", processed_res)) # remove default_values
        if len(processed_res) != 2: 
            print(f"ERROR! values: {processed_res} Len:{len(processed_res)}")
            exit()
        elif "!" in result: inequalities.append(processed_res)
        else: equalities.append(processed_res) 
    return equalities,inequalities 

class parse_atoms:

    def __init__(self,cc_dag):
        self.atom_dict = {}
        self.cc_dag = cc_dag
        self.id = 1 #id's start from 1, like in Bradley Manna  

    # TODO: tutto dc (Da finire Bro)
    def rec_build(self,fn,args): 
        real_args = []
        c_len,counter = len(args),0
        while counter < c_len:
            try:
                if isinstance(args[counter], str) and (not isinstance(args[counter +1], str)):
                    counter+=2
                    pass
                elif isinstance(args[counter], str):
                    real_args.append([])
                    counter+=1
                    pass
            except: # last element is a literal and there 
                print("Last Element, cant look further")
        
    def parse(self,atoms):
        self.id = 1 # id's start from 1, like in Bradley Manna  
        for atom in atoms: 
            index = atom.find("(")
            og_id = 0 # Salva id funzione esterna per aggiungere a padre dopo 
            # Self Dict contiene tutto il nome al contrario del parametro fn del node
            if self.atom_dict.get(atom,"default") is "default": 
                self.atom_dict[atom] = copy.copy(self.id)
                self.id+=1
                og_id = copy.copy(self.id)
            else:
                og_id = self.atom_dict[atom]

            pruned_atom = atom[index:]
            dissected_atom = nestedExpr('(',')').parseString(pruned_atom).asList()
             
            
test = "(f(f(f(a,b),f(c))))"
print(nestedExpr('(',')').parseString(test).asList())


# Old implementation, main function
# Generating Brackets list for Parsing 
# bi = [i for i,c in enumerate(atom) if c == "("]   
# rbi = [i for i,c in enumerate(atom) if c == ")"]   
# rbi = reversed(rbi)
# brackets_indeces = list(zip(bi,rbi))
# Recursivly building graph from atom
# self.rec_build(atom,brackets_indeces,0)

# RECURSIVE FUNCTION
# if pos == int(len(brackets_indeces)-1):
#     return 
# else:
#     og_particle = atom[brackets_indeces[pos][0]:brackets_indeces[pos][1]] 
#     particles = og_particle.split(",")
#     for particle in particles:
#         if particle not in self.atom_dict:
#             self.atom_dict[atom] = copy.copy(self.id)
#             self.id+=1

