import copy
from pyparsing import *
from congruence_closure import CC_DAG

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

    def rec_build(self,fn,args): 
        real_args = []
        c_len,counter = len(args),0
        # TODO: MANCA CASO IN  ARGS HA UN SOLO ARGOMENTO 

        # Cycle through args
        while counter < c_len:
            try:
                # Argument is a function with arguments
                if isinstance(args[counter], str) and (not isinstance(args[counter +1], str)):
                    ids = []
                    for arg in args[counter+1]:
                        ids.append(self.rec_build(args[counter],arg))
                    counter+=2
                # Argument is a literal with NO arguments
                elif isinstance(args[counter], str):
                    check_id =  self.atom_dict.get(args[counter],"default")
                    if check_id is "default":  # CREATE SINGLE LITERAL ELEMENT
                        self.id+=1
                        real_args.append(copy.copy(self.id))
                        self.cc_dag.add_node(id=copy.copy(self.id),fn=args[counter],args=[])
                        real_args.append(copy.copy(self.id))
                    else: real_args.append(check_id)
                    counter+=1
            # Last Element is a Literal and there are no more arguments to args 
            except: 
                print("Last Element, cant look further")
                check_id =  self.atom_dict.get(args[counter],"default")
                if check_id is "default":  # CREATE SINGLE LITERAL ELEMENT
                    self.id+=1
                    real_args.append(copy.copy(self.id))
                    self.cc_dag.add_node(id=copy.copy(self.id),fn=args[counter],args=[])
                    real_args.append(copy.copy(self.id))
                else: real_args.append(check_id)
                counter+=1
            
        iter_string = ""
        for instance in list(map(lambda x: self.cc_dag.node_string(x),real_args)):
            iter_string= iter_string + instance +","
        iter_string = iter_string[:-1]
        real_node = fn + "(" + iter_string  + ")"
            
        check_id =  self.atom_dict.get(real_node,"default")
        if check_id is "default":  # CREATE SINGLE LITERAL ELEMENT
            self.id+=1
            self.cc_dag.add_node(id=copy.copy(self.id),fn=fn,args=real_args)
            return copy.copy(self.id)
        return check_id
        
    def parse(self,atoms):
        for atom in atoms: 
            atom = "(" + atom + ")"
            if self.atom_dict.get(atom,"default") is "default": # dissect the atom if is not already in the dict
                dissected_atom = nestedExpr('(',')').parseString(test).asList()
                self.rec_build(dissected_atom)
             
    # TODO: add parenths to each node in the graph 
    def add_ccpar(self):
        pass 

test = ["f(f(f(f(ac,bc),c)))"]
solver = CC_DAG()
parser = parse_atoms(solver)
parser.parse(test)
# test = "(" + test + ")"
# TESTING 
# test = "(f(f(f(a,b),f(c))))"
# print(nestedExpr('(',')').parseString(test).asList())





# OLD IMPLEMENTATION
# main function Generating Brackets list for Parsing 
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

