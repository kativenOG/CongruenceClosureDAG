import sys
from lib import *

def main(file="",term=None):
    # Checks
    if len(sys.argv)>1: file = sys.argv[1]
    if file == "": 
        print("ERROR: no input file!")
        exit()

    # Declaring SMT Parser:
    smt_parser = smtp.smt_parser()

    # Parsing the file
    cc_dag_instances,atoms,ground_truth = smt_parser.parse(file) 


    end_result = "UNSAT" 
    for equations in cc_dag_instances:
        solver = cc.CC_DAG()
        atom_parser = gp.parse_atoms(solver) 
        # Drawing the graph in the CC_DAG object instance
        atom_parser.parse(atoms) 
        solver.complete_ccpar()
        # Print the DAG before the Congruence Closure Algorithm 
        solver.visualize_dag(True)
        # Parsing the formulas and transforming them in tuples for the CC algorithm 
        solver.equalities, solver.inequalities = gp.parse_equations(equations,atom_parser.atom_dict) 
        # Running Congruence Closure 
        result = solver.solve() 
        # Print the DAG after the Congruence Closure Algorithm with dotted edges
        solver.visualize_dag(has_find=True)
        if result == "SAT": end_result = "SAT" 

        # Prints
        if term != None:
            print(term.home() +  term.clear() + term.move_y(term.height//3))
            print(term.center(term.cyan2("_____RESULT_____")))
            print()
            print(term.center("Atoms:"))
            print(term.center(f"{atom_parser.atom_dict}"))
            print()
            print(term.center("Formulas:"))
            print(term.center(f"{equations}"))
            # print()
            # print(term.center(term.black_on_red(f"Ground Truth: {ground_truth}")))
            print()
            print(term.center(term.black_on_green(f"Result: {result}")))
            print()
            print(term.center(term.black_on_red("PRESS ANY KEY TO CONTINUE")))
            inp = term.inkey() # Press any key

        elif file != "":
            print((f"Atoms:\n{atoms}\nFormulas:\n{equations}\n"))
            print(f"Graph Nodes:\n{solver}")
            print(f"Atom Dictionary:\n{atom_parser.atom_dict}\n")
            print(f"Equalities: {solver.equalities}")
            print(f"Inequalities: {solver.inequalities}")
            print()
            # print(f"Ground Truth: {ground_truth}")
            print(f"CC_DAG Result: {result}")
            print()

        
    # Ground Truth
    if term != None:  
        print(term.home + term.clear() + term.move_y(term.height//2))
        print(term.center(f"RESULTS:"))
        print(term.center(term.black_on_red(f"Ground Truth: {ground_truth}")))
        print(term.center(term.black_on_green(f"End Result: {end_result}")))
        inp = term.inkey() # Press any key
        exit()
    elif file != "": 
        print(f"RESULTS:")
        print(f"Ground Truth: {ground_truth}")
        print(f"End Result: {end_result}")

    return end_result

if __name__ == "__main__": 
    main()
