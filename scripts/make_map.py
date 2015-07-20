#!/usr/bin/env python
import random
import sys
import pickle
import pdb
from spacegame.Universe import Universe, Sector
import code, traceback, signal

def debug(sig, frame):
    """Interrupt running process, and provide a python prompt for
    interactive debugging."""
    d={'_frame':frame}         # Allow access to frame object.
    d.update(frame.f_globals)  # Unless shadowed by global
    d.update(frame.f_locals)

    i = code.InteractiveConsole(d)
    message  = "Signal received : entering python shell.\nTraceback:\n"
    message += ''.join(traceback.format_stack(frame))
    i.interact(message)

def listen():
    signal.signal(signal.SIGUSR1, debug)  # Register handler


def bang_sector(sector):
    '''make a new sector and put it in the universe.'''
    if sector is None:
        return None
    else:
        newsector=sector
    while u.get_sector(newsector) is not None:
        newsector=random.randint(1,UNIVERSE_SIZE) 
        if len(u.map.keys()) >= UNIVERSE_SIZE:
            return None

    s=Sector.Sector(sector_name=newsector)
    u.add_sector(s)
    return newsector

def check_adjacency(prospective_link):
    try:
        sector=u.map[prospective_link]
        if len(sector.adjacent_sectors) >= MAX_LINKS:
            return False
        else: 
            return True
    except KeyError:
        return True
            

def get_new_sector():
    newsector=random.randint(1,UNIVERSE_SIZE)
    while u.get_sector(newsector) is not None:
        newsector=random.randint(1,UNIVERSE_SIZE)
        if len(u.map.keys()) >= UNIVERSE_SIZE:
            return None
    return newsector


def link_sectors(previous,current):
    sector_A=u.map[previous]
    sector_B=u.map[current]

    if len(sector_A.adjacent_sectors) > MAX_LINKS:
        raise Exception
    sector_A.add_link(sector_B)

    sector_B.add_link(sector_A)
    if len(sector_A.adjacent_sectors) > MAX_LINKS:
        raise Exception

UNIVERSE_SIZE=100
MAX_LINKS=10

listen()
u=Universe.Universe()

prev_sector_id=bang_sector(get_new_sector())

while len(u.map.keys()) <= UNIVERSE_SIZE:
    p=get_new_sector()
    while check_adjacency(p) == False:
        p=get_new_sector()
        
    sector_id=bang_sector(p)
    if sector_id is None:
        break
    if check_adjacency(prev_sector_id) == False:
        prev_sector_id=bang_sector(get_new_sector())
    link_sectors(prev_sector_id,sector_id)
    numlinks=random.randint(1,MAX_LINKS)
    size=len(u.map.keys())
    print("Added sector {sector}.  Universe now {size} sectors big.".format(sector=sector_id,size=size))
    for j in range(0,numlinks):
        if check_adjacency(sector_id) == False:
            print("Adjacency violation in numlinks.  Count in sector_id={c}".format(c=len(u.map[sector_id].adjacent_sectors)))
            break
        potential_id=get_new_sector()
        link_sector_id=bang_sector(potential_id)
        if link_sector_id is None:
            break
        link_sectors(sector_id, link_sector_id)
        size=len(u.map.keys())
        print("Added adjacency count {j} of sector {s} in {sector}.  Universe now {size} sectors big.".format(sector=sector_id,j=j,s=link_sector_id,size=size))
pickle.dump( u, open( "universe.p", "wb" ) )
