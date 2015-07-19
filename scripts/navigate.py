#!/usr/bin/env python
import pickle

with open("universe.p","rb") as f:
    u=pickle.Unpickler(f).load()

mysector=1
while True:
    jumps=[]
    print "You are in sector {mysector}, you can jump to these sectors:".format(mysector=mysector)
    for adj in u.map[mysector].adjacent_sectors:
        print "Sector: {s}".format(s=adj.name)
        jumps.append(adj.name)
    input=raw_input("> ")
    if int(input) in jumps:
        mysector=int(input)
    else:
        print("Invalid jump entered.")   
    
