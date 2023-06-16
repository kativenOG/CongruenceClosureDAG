import networkx as nx 
from itertools import product 
import copy 
# from matplotlib import pyplot as plt

class CC_DAG: 

    def __init__(self): 
        self.g = nx.DiGraph()
        self.equalities = []
        self.inequalities = []
         
    def __str__(self):
        nodes = list(self.g.nodes) 
        result = ""
        for node in nodes:
            node_string = self.node_string(node)
            result += f"{node} {node_string}\n" 
        return result

    def add_node(self,id,fn,args):
        mutable_ccpar = set()
        # mutable_ccpar.add(father)
        mutable_find = id
        self.g.add_node(id,fn=fn, args=args, mutable_find=mutable_find,mutable_ccpar=mutable_ccpar)
                
    # PRINT NODE 
    def node_string(self,id):
        target = self.g.nodes[id]
        if len(target["args"]) == 0:
            return "{}".format(target["fn"])
        else:
            args_str = ""
            for arg in target["args"]:
                args_str = args_str + self.node_string(arg) + ", "
            args_str = args_str[:-2]
            return "{}({})".format(target["fn"],args_str)

    def complete_ccpar(self):
        nodes_list = list(self.g.nodes)#(data=True)) 
        for id in nodes_list:
            self.add_father(id) 
            pass

    def add_father(self,id):
        father_args = self.g.nodes[id]["args"]
        for arg in father_args:
            target = self.g.nodes[arg] 
            target["mutable_ccpar"].add(id)

    def NODE(self,id):
        attr_dict = self.g.nodes[id]
        return attr_dict 

    def find(self,id)->int: 
        n = self.NODE(id)
        if n["mutable_find"] == id: 
            return id
        else:
            new_id = self.find(n["mutable_find"])
            return new_id 

    def ccpar(self,id):
        result = self.NODE(self.find(id))
        return result["mutable_ccpar"]
        
    def union(self,id1,id2):
        n1 = self.NODE(self.find(id1))
        n2 = self.NODE(self.find(id2))
        n1["mutable_find"]  = copy.copy(n2["mutable_find"])
        n2["mutable_ccpar"].update(n1["mutable_ccpar"])
        n1["mutable_ccpar"] = set()
    
    def congruent(self,id1,id2):
        n1 = self.NODE(id1)
        n2 = self.NODE(id2)
        if (n1["fn"] is not n2["fn"]): return False
        if(len(n1["args"]) is not len(n2["args"])): return False
        for i in range(len(n1["args"])):
            val1= self.find(n1["args"][i]) 
            val2= self.find(n2["args"][i]) 
            if val1 != val2: return False
        return True 
        
    def merge(self,id1,id2):
        a1 = self.find(id1)
        a2 = self.find(id2)
        if a1!=a2: 
            pi1 = self.ccpar(id1)
            pi2 = self.ccpar(id2)
            self.union(id1,id2)
            for t1,t2 in product(pi1,pi2):
                if (self.find(t1) is not self.find(t2)) and self.congruent(t1,t2):
                    self.merge(t1,t2)
            return True
        else: 
            return False


    def solve(self):
        for eq in self.equalities:
            val1,val2 =  self.find(eq[0]),self.find(eq[1])
            # print(f"Eq: {eq}")
            self.merge(eq[0],eq[1])
        for ineq in self.inequalities:
            val1,val2 =  self.find(ineq[0]),self.find(ineq[1])
            # print(f"Ineq: {ineq} <-> Mutable_find: [{val1},{val2}] ")
            if val1 == val2: # If the inequality is not correct it's UNSAT 
                return "UNSAT"
        return "SAT"
