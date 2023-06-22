import sys
from lib import *
import sys,time


def main(file="",term=None,plot=False):
    if ("--plot" in sys.argv) or ("-p" in sys.argv): plot = True 
    # Checks
    if len(sys.argv)>1: 
        if ("--plot" in sys.argv) or ("-p" in sys.argv): 
            plot = True 
            file = sys.argv[2]
        else: file = sys.argv[1]
    if file == "": 
        print("ERROR: no input file!")
        exit()

    # Declaring SMT Parser:
    smt_parser = smtp.smt_parser()

    # Parsing the file
    cc_dag_instances,atoms,ground_truth = smt_parser.parse(file) 


    start = time.time()
    end_result = "UNSAT" 

    if file != "": 
        print(f"File: {file}")
        print(f"Atoms:\n{atoms}\n")

    for equations in cc_dag_instances:
        solver = cc.CC_DAG()
        atom_parser = gp.parse_atoms(solver) 
        # Drawing the graph in the CC_DAG object instance
        atom_parser.parse(atoms) 
        solver.complete_ccpar()
        # Print the DAG before the Congruence Closure Algorithm 
        if plot: old_graph = solver.visualize_dag(has_find=True)
        # Parsing the formulas and transforming them in tuples for the CC algorithm 
        solver.equalities, solver.inequalities = gp.parse_equations(equations,atom_parser.atom_dict) 
        # Running Congruence Closure 
        result = solver.solve() 
        # Print the DAG after the Congruence Closure Algorithm with dotted edges
        if plot: solver.visualize_dag(G=old_graph,has_find=True)
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
            print()
            print(term.center(term.black_on_green(f"Result: {result}")))
            print()
            print(term.center(term.black_on_red("PRESS ANY KEY TO CONTINUE")))
            inp = term.inkey() # Press any key

        elif file != "":
            print((f"Formulas:\n{equations}"))
            print(f"CC_DAG Result: {result}")
            print()

        
    end = time.time() - start 
    # Ground Truth
    if term != None:  
        print(term.home + term.clear() + term.move_y(term.height//2))
        print(term.center(f"FINAL RESULTS:"))
        print(term.center(term.black_on_red(f"Ground Truth: {ground_truth}")))
        print(term.center(term.black_on_green(f"End Result: {end_result}")))
        print(term.center(term.black_on_blue(f"Total Time: {end}")))
        inp = term.inkey() # Press any key
        exit()
    elif file != "": 
        print(f"FINAL RESULTS:")
        print(f"Ground Truth: {ground_truth}")
        print(f"End Result: {end_result}")
        print(f"Compilation Time: {end}")

    return end_result,end

if __name__ == "__main__": 
    main()
