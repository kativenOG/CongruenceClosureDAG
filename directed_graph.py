import networkx as nx 
from matplotlib import pyplot as plt

def draw(graph):
    try:
        plt.tight_layout()
        nx.draw_networkx(graph, arrows=True)
        plt.savefig("dac.png", format="PNG")
        plt.clf()
        return
    except:
        print("ERROR")
        return 

graph = nx.DiGraph()
nx.is_directed_acyclic_graph(graph) # Check if Acyclic when using Input



