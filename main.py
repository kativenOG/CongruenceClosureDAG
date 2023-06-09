import sys
from lib import *

def main(file="",term=None):
    # Checks
    if len(sys.argv)>1: file = sys.argv[1]
    if file == "": 
        print("ERROR: no input file!")
        exit()

    # DECLARATIONS:
    solver = cc.CC_DAG()
    smt_parser = smtp.smt_parser()
    atom_parser = gp.parse_atoms(solver) 

    # IMPLEMENTATION:
    # Parsing the file
    equations,atoms = smt_parser.parse(file) #"./inputs/input1.smt2")#
    # Drawing the graph in the CC_DAG object instance
    atom_parser.parse(atoms) 
    solver.complete_ccpar()
    # Parsing the formulas and transforming them in tuples for the CC algorithm 
    solver.equalities, solver.inequalities = gp.parse_equations(equations,atom_parser.atom_dict) 
    # Running Congruence Closure 
    result = solver.solve() 
    # Prints
    if term != None:
        print(term.home() + term.clear())
        print(term.center("Atoms:"))
        print(term.center(f"{atoms}"))
        print(term.center("Formulas:"))
        print(term.center(f"{equations}"))
    elif (file!=""):
        print((f"Problem: "))
        print((f"Atoms:\n{atoms}\nFormulas:\n{equations}"))
        print(solver.g.nodes(data=True))
        print(f"Graph Nodes:\n{solver}")
        print(f"Atom Dictionary:\n{atom_parser.atom_dict}\n")
        print(solver.equalities)
        print(solver.inequalities)
        print(result)
    return result 

if __name__ == "__main__": 
    main()
