from pysmt.smtlib.parser import SmtLibParser
# from pysmt.oracles import get_logic

class smt_parser():
    def __init__(self):
        self.parser = SmtLibParser()

    def parse(self,filename):
        # NB: Should create an smtlib env here for script values 
        script = self.parser.get_script_fname(filename)
        # Get the last Assert 
        # f= script.get_last_formula() # No More 
        f= script.get_strict_formula()
        # print(f.serialize())
        # Checks on the File
        assert script.count_command_occurrences("assert") >= 1
        assert script.contains_command("check-sat")
        formulas = f.serialize() #list(map(lambda x: x.serialize(),list(f.args())))
        atoms    = list(map(lambda x: x.serialize(),list(f.get_atoms())))
        print(formulas)
        real_atoms,real_formulas = [],[]
        for atom in atoms:
            if atom.find("=") != -1:
                equality = atom[1:-1].split("=")
                real_atoms.append(equality[0].strip())
                real_atoms.append(equality[1].strip())
            else:
                real_atoms.append(atom) #[1:-1])
        if formulas.find("&") != -1:
            separated_formulas = formulas[1:-1].split("&")
            # separated_formulas[0], separated_formulas[0]= separated_formulas[0][1:-1],separated_formulas[-1][:-1]
            real_formulas.extend(list(map(lambda x: x.strip(),separated_formulas)))
        real_formulas = [x for x in real_formulas if x.find("=")!=-1 ]

        print(real_formulas)

        return real_formulas,list(set(real_atoms))
