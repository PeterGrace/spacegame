#!/usr/bin/env python
import pickle
import pprint

with open("universe.p","rb") as f:
    u=pickle.Unpickler(f).load()
for sec in u.map.keys():
    print("_{s}_|_{j}_".format(s=sec,j=u.map[sec].adjacent_sectors))    
