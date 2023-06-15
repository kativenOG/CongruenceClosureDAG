import re 
# Sto per Abbandonare sta Idea

class dnf_converter:
    
    def __init(self,atoms):
        self.atoms = atoms 
        self.atom_dict = {}
        self.equatios_dict = {}

    def generate_atom_dict(self):
        for id,atom in zip(range(len(self.atoms)),self.atoms):
            self.equatios_dict[atom] = id 

    def generate_equations_dict(self,formulas):
        formulas = formulas.split("|")
        formulas = list(map(lambda x: x.split("&"),formulas))
        formulas = [ x for x in formulas if x.find("=")!=-1]
        
        id = 0 
        for formula in formulas:
            start,end = 0,0
            # ODIO STA SOLUZIONE 
            for i,c in enumerate(formula):
                if c != "(" and c != " " and c != "!":
                    start = i
                    break 
            rformula = reversed(formula)
            for i,c in enumerate(rformula):
                if c != ")" and c != " " and c != "!":
                    end = i
                    break 
            real_formula = formula[start:end] # CHE ODIO 

            list(map(lambda x: x.strip(),real_formula.split["="]))
