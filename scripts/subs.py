#!/usr/bin/env python
import networkx as nx
import matplotlib.pyplot as plt
import pickle

with open("universe.p","rb") as f:
    u=pickle.Unpickler(f).load()


G = nx.Graph()

for sect_id in u.map.keys():
    G.add_node(u.map[sect_id].name)
    for adj in u.map[sect_id].adjacent_sectors:
        G.add_edge(sect_id,adj.name)

if not nx.is_connected(G):
    sub_graphs=nx.connected_component_subgraphs(G)
    for sg in sub_graphs:
        print "sg len: {0}".format(len(sg.nodes()))
        print sg.nodes()[0]
