import networkx as nx 
from itertools import product 
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

    def add_node(self,id,fn,args = []):
        mutable_ccpar = set()
        # mutable_ccpar.add(father)
        mutable_find = []
        mutable_find.append(id)
        self.g.add_node(id,fn=fn, args=args, mutable_find=mutable_find,mutable_ccpar=mutable_ccpar)
                
    # PRINT NODE 
    def node_string(self,id): 
        target = self.g.nodes[id]
        if len(target["args"]) > 0:
            return "{}".format(target["fn"])
        else:
            args_str = ""
            for arg in target["args"]:
                args_str = args_str + self.node_string(arg)
            return "{}({})".format(target["fn"],args_str)

    def update_node(self,id,mutable_find=None,mutable_ccpar=None):
        target = self.g.nodes[id]
        if mutable_find != None: target["mutable_find"] = target["mutable_find"] + mutable_find
        if mutable_ccpar!= None: target["mutable_ccpar"].update(mutable_ccpar)
        # self.g.add_node(id,fn=fn, args=args, mutable_find=mutable_find,mutable_ccpar=mutable_ccpar)

    def NODE(self,id):
        attr_dict = self.g.nodes[id]
        return attr_dict 

    def find(self,id): 
        n = self.NODE(id)
        if n["mutable_find"] == id: 
            return id
        else:
            self.find(n["mutable_find"])

    def ccpar(self,id):
        result = self.NODE(self.find(id))
        return result["mutable_ccpar"]
        
    def union(self,id1,id2):
        n1 = self.NODE(self.find(id1))
        n2 = self.NODE(self.find(id2))
        n1["mutable_find"]  = n2["mutable_find"]
        n2["mutable_ccpar"].update(n1["mutable_ccpar"])
        n1["mutable_ccpar"] = set()
    
    def congruent(self,id1,id2):
        n1 = self.NODE(id1)
        n2 = self.NODE(id2)
        if (n1["fn"] is not n2["fn"]) or (len(n1["args"]) is not len(n2["args"])): return False
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
                    node1 = self.NODE(t1)
                    node2 = self.NODE(t2)
                    self.merge(node1,node2)
            return True
        else: 
            return False

    def check_DAG(self):
        nx.is_directed_acyclic_graph(self.g) # Check if Acyclic when using Input

    def solve(self):
        for eq in self.equalities:
            print(eq,self.find(eq[0]),self.find(eq[1]))
            self.merge(eq[0],eq[1])
        for ineq in self.inequalities:
            val1,val2 =  self.find(ineq[0]),self.find(ineq[1])
            print(f"Ineq: {ineq} -> {val1} and {val2} ")
            if val1 == val2: # If the inequality is not correct it's UNSAT 
                print("UNSAT")
                return "UNSAT"
        print("SAT")
        return "SAT"

    # def draw(self):
    #     try:
    #         plt.tight_layout()
    #         nx.draw_networkx(self.g, arrows=True)
    #         plt.savefig("dac.png", format="PNG")
    #         plt.clf()
    #         return
    #     except:
    #         print("ERROR")
    #         return 

