from pysmt.smtlib.parser import SmtLibParser
from pysmt.oracles import get_logic

class smt_parser():
    def __init__(self):
        self.parser = SmtLibParser()

    def parse(self,filename):
        # NB: Should create an smtlib env here for script values 
        script = self.parser.get_script_fname(filename)
        # Get the last Assert 
        f= script.get_last_formula()
        # Checks on the file
        assert str(get_logic(f)) == "QF_UF" 
        assert script.count_command_occurrences("assert") == 1
        assert script.contains_command("check-sat")
        
        # Get a list of Atoms and the Equations 
        formulas = list(map(lambda x: x.serialize(),list(f.args())))
        atoms   = list(map(lambda x: x.serialize(),list(f.get_atoms())))
        print("*"*80)
        print(f"Atoms:\n{atoms}\nFormulas:\n{formulas}")
        print("*"*80)
        equalities,inequalities = [],[]
        for val in formulas :
            # NB: Only checks if the ! operator is only used for the inequalities,
            #     Should be drastically improved
            if "!" not in val: equalities.append(val)
            else: inequalities.append(val)
        return equalities,inequalities,atoms 

par = smt_parser()
equalities,inequalities,atoms = par.parse("./inputs/input2.smt2")
print(atoms)
print(equalities)
print(inequalities)
