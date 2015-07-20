#!/usr/bin/env python
import networkx as nx
import matplotlib.pyplot as plt
import pickle
from make_map import UNIVERSE_SIZE

with open("universe.p","rb") as f:
    u=pickle.Unpickler(f).load()


G = nx.Graph()

for sect_id in u.map.keys():
    print("Adding node: {0}".format(sect_id))
    G.add_node(u.map[sect_id].name)
    for adj in u.map[sect_id].adjacent_sectors:
        print("Adding edge {0} to node {1}".format(adj.name,sect_id))
        G.add_edge(sect_id,adj.name)

print "Nodes: {n}, Edges: {e}".format(n=G.number_of_nodes(),e=G.number_of_edges())

solitary=[ n for n,d in G.degree_iter() if d==0 ]
print solitary
nx.write_adjlist(G,'foo.path')
nx.draw_random(G,node_size=10,with_labels=True)
plt.savefig("path.png")
