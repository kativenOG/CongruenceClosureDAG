from pysmt.smtlib.parser import SmtLibParser

class smt_parser():
    def __init__(self):
        self.parser = SmtLibParser()

    def parse(self,filename):
        # NB: Should create an smtlib env here for script values 
        script = self.parser.get_script_fname(filename)

        # Get all the Asserts
        f = script.get_strict_formula()
        result = [cmd for cmd in script.commands if ((cmd.name == "set-info") and (":status" in cmd.args))]
        ground_truth = result[0].args[1]

        # Checks on the File
        assert len(result) <= 1
        assert script.count_command_occurrences("assert") == 1
        assert script.contains_command("check-sat")

        # Transform formulas to DNF 

        formulas = f.serialize() 
        atoms = list(map(lambda x: x.serialize(),list(f.get_atoms())))

        real_atoms,cc_dag_instances = [],[]
        # Real_atoms:
        for atom in atoms:
            if atom.find("=") != -1:
                equality = atom[1:-1].split("=")
                real_atoms.append(equality[0].strip())
                real_atoms.append(equality[1].strip())
            else:
                real_atoms.append(atom) #[1:-1])

        # Real_formulas:
        print(formulas)
        for_formulas = formulas.split("|")
        print(for_formulas)
         
        for formula in for_formulas:
            real_formulas = []
            separated_formulas = formula[1:-1].split("&")
            if len(separated_formulas)>1:
                real_formulas.extend(list(map(lambda x: x[1:-1].strip(), separated_formulas)))
            else: real_formulas = separated_formulas
            real_formulas = [x for x in real_formulas if x.find("=")!=-1 ]
            cc_dag_instances.append(real_formulas)

        return cc_dag_instances,list(set(real_atoms)),ground_truth.upper()
