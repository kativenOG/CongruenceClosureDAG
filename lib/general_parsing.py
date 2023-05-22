import copy
from pyparsing import *

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

    def rec_build(self,atom,brackets_indeces,pos): # Da finire bro
        particle = atom[brackets_indeces[pos][0]:brackets_indeces[pos][1]] 
        if particle not in self.atom_dict:
            self.atom_dict[atom] = copy.copy(self.id)
            self.id+=1

    def parse(self,atoms):
        # atom_dict = {} # NOTATION: "function": id
        self.id = 1 # id's start from 1, like in Bradley Manna  
        for atom in atoms: 
            # funzione esterna 
            if self.atom_dict.get(atom,"default") is "default":
                self.atom_dict[atom] = copy.copy(self.id)
                self.id+=1
            # Generating Brackets list for Parsing 
            bi = [i for i,c in enumerate(atom) if c == "("]   
            rbi = [i for i,c in enumerate(atom) if c == ")"]   
            rbi = reversed(rbi)
            brackets_indeces = list(zip(bi,rbi))
            # Recursivly building graph from atom
            self.rec_build(atom,brackets_indeces,0)


# test = "f(f(f(f(a))))"
# atom_parser =  atom_parser(atoms,)
