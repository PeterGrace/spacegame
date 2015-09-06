#!/usr/bin/env python
import pickle
import networkx as nx
import pdb

with open("universe.p","rb") as f:
    u=pickle.Unpickler(f).load()

    
G = nx.Graph()

for sect_id in u.map.keys():
    print("Adding node: {0}".format(sect_id))
    G.add_node(u.map[sect_id].name)
    for adj in u.map[sect_id].adjacent_sectors:
        print("Adding edge {0} to node {1}".format(adj.name,sect_id))
        G.add_edge(sect_id,adj.name)


mysector=1
while True:
    jumps=[]
    print "You are in {sector} [{mysector}], you can jump to these sectors:".format(sector=u.map[mysector].nice_name,mysector=mysector)
    for adj in u.map[mysector].adjacent_sectors:
        print "Sector: {s}".format(s=adj.name)
        jumps.append(adj.name)
    input=raw_input("> ")
    if int(input) in jumps:
        mysector=int(input)
    elif int(input) in u.map.keys():
        print nx.astar_path(G,source=mysector,target=int(input))
    else:
        print("Invalid jump entered.")   
    
