import sys
from lib import *
#!!!! Code is not Working, still missing part of atom_parser.parse() Implementation 

def main():
    # Objects Declarations 
    solver = cc.CC_DAG()
    smt_parser = smtp.smt_parser()
    atom_parser = gp.atom_parser(solver) 

    # Implementation:
    equations,atoms = smt_parser.parse(sys.argv[1]) # Parsing the file
    atom_parser.parse(atoms) # Drawing the graph in the CC_DAG object instance
    # Parsing the formulas and transforming them in tuples for the CC algorithm 
    solver.equalities, solver.inequalities = gp.parse_equations(equations,atom_parser.atom_dict) 
    solver.solve() # Running Congruence Closure 

if __name__ == "__main__":
    main()
