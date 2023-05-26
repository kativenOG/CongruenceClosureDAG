import sys
from lib import *

def main():
    # DECLARATIONS:
    solver = cc.CC_DAG()
    smt_parser = smtp.smt_parser()
    atom_parser = gp.parse_atoms(solver) 

    # IMPLEMENTATION:
    # Parsing the file
    equations,atoms = smt_parser.parse(sys.argv[1]) #"./inputs/input1.smt2")#
    # exit()
    # Drawing the graph in the CC_DAG object instance
    atom_parser.parse(atoms) 
    solver.complete_ccpar()
    # print(solver.g.nodes(data=True))
    print(f"Graph Nodes:\n{solver}")
    print(f"Atom Dictionary:\n{atom_parser.atom_dict}\n")
    # Parsing the formulas and transforming them in tuples for the CC algorithm 
    solver.equalities, solver.inequalities = gp.parse_equations(equations,atom_parser.atom_dict) 
    print(solver.equalities)
    print(solver.inequalities)
    print()
    # Running Congruence Closure 
    result = solver.solve() 

if __name__ == "__main__": 
    main()
