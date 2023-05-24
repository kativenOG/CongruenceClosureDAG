import copy
from pyparsing import *
# from congruence_closure import CC_DAG

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
        # print("In")
        real_args = []
        c_len,counter = len(args),0
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
                elif isinstance(args[counter], str): # else: 
                    check_id =  self.atom_dict.get(args[counter],"default")
                    if check_id == "default":  # CREATE SINGLE LITERAL ELEMENT
                        self.id+=1
                        real_args.append(copy.copy(self.id))
                        self.cc_dag.add_node(id=copy.copy(self.id),fn=args[counter],args=[])
                        # print(args[counter])
                        real_args.append(copy.copy(self.id))
                    else: real_args.append(check_id)
                    counter+=1
                else:
                    pass
            # Last Element is a Literal and there are no more arguments to args 
            except: 
                check_id =  self.atom_dict.get(args[counter],"default")
                if check_id == "default":  # CREATE SINGLE LITERAL ELEMENT
                    self.id+=1
                    real_args.append(copy.copy(self.id))
                    self.cc_dag.add_node(id=copy.copy(self.id),fn=args[counter],args=[])
                    real_args.append(copy.copy(self.id))
                else: real_args.append(check_id)
                counter+=1
            
        if fn!= None:
            iter_string = ""
            for instance in list(map(lambda x: self.cc_dag.node_string(x),real_args)):
                iter_string= iter_string + instance +", "
            iter_string = iter_string[:-2]
            real_node = fn + "(" + iter_string  + ")"
                
            check_id =  self.atom_dict.get(real_node,"default")
            if check_id == "default":  # CREATE SINGLE LITERAL ELEMENT
                self.id+=1
                self.cc_dag.add_node(id=copy.copy(self.id),fn=fn,args=real_args)
                return copy.copy(self.id)
            return check_id
        else: return 
        
    def parse(self,atoms):
        for atom in atoms: 
            atom = "(" + atom + ")"
            if self.atom_dict.get(atom,"default") == "default": # dissect the atom if is not already in the dict
                dissected_atom = nestedExpr('(',')').parseString(atom).asList()
                dissected_atom = dissected_atom[0]
                print(f"Dissected Atom: {dissected_atom}")
                self.rec_build(None,dissected_atom)
             
    # TODO: add parenths to each node in the graph 
    def add_ccpar(self):
        pass 

# test = ["f(f(f(f(a, c), c)))"]
# solver = CC_DAG()
# parser = parse_atoms(solver)
# parser.parse(test)
# print(solver)
