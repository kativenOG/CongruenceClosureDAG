import sys
from lib import *

def main():
    # DECLARATIONS:
    solver = cc.CC_DAG()
    smt_parser = smtp.smt_parser()
    atom_parser = gp.atom_parser(solver) 

    # IMPLEMENTATION:
    # Parsing the file
    equations,atoms = smt_parser.parse(sys.argv[1]) 
    # Drawing the graph in the CC_DAG object instance
    atom_parser.parse(atoms) 
    # Parsing the formulas and transforming them in tuples for the CC algorithm 
    solver.equalities, solver.inequalities = gp.parse_equations(equations,atom_parser.atom_dict) 
    # Running Congruence Closure 
    solver.solve() 

if __name__ == "__main__": #   
    main()
