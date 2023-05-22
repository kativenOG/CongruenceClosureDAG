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

def rec_build(id,cc_dag,brackets_indeces,pos):
    pass

def parse_atoms(atoms,cc_dag):
    atom_dict = {} # NOTATION: "function": id
    incr_id = 1 # id's start from 1, like in Bradley Manna  
    for atom in atoms: 
        # funzione esterna 
        if atom_dict.get(atom,"default") == "default":
            atom_dict[atom] = copy.copy(incr_id)
            incr_id+=1
        # Generating Brackets list for Parsing 
        bi = [i for i,c in enumerate(atom) if c == "("]   
        rbi = [i for i,c in enumerate(atom) if c == ")"]   
        rbi = reversed(rbi)
        brackets_indeces = list(zip(bi,rbi))

        # Recursivly building graph from atom
        incr_id,_= rec_build(incr_id,cc_dag,brackets_indeces,0)
        # incr_id = max(cc_dag.nodes) 
    return atom_dict

# test = "f(f(f(f(a))))"
# parse_atoms(test)
