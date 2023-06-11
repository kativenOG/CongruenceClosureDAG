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
    equations,atoms,ground_truth = smt_parser.parse(file) 
    # Drawing the graph in the CC_DAG object instance
    atom_parser.parse(atoms) 
    solver.complete_ccpar()
    # Parsing the formulas and transforming them in tuples for the CC algorithm 
    solver.equalities, solver.inequalities = gp.parse_equations(equations,atom_parser.atom_dict) 
    # Running Congruence Closure 
    result = solver.solve() 
    # Prints
    if term != None:
        print(term.home() + term.clear() + term.move_y(term.height//3))
        print(term.center(term.cyan2("_____RESULT_____")))
        print()
        print(term.center("Atoms:"))
        print(term.center(f"{atoms}"))
        print()
        print(term.center("Formulas:"))
        print(term.center(f"{equations}"))
        print()
        print(term.center(term.black_on_red(f"Ground Truth: {ground_truth}")))
        print()
        print(term.center(term.black_on_green(f"Result: {result}")))
    elif file != "":
        print((f"Problem: "))
        print((f"Atoms:\n{atoms}\nFormulas:\n{equations}"))
        print(solver.g.nodes(data=True))
        print(f"Graph Nodes:\n{solver}")
        print(f"Atom Dictionary:\n{atom_parser.atom_dict}\n")
        print(solver.equalities)
        print(solver.inequalities)
        print(f"Ground Truth: {ground_truth}")
        print(f"Result: {result}")

if __name__ == "__main__": 
    main()
