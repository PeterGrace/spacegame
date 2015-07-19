#!/usr/bin/env python
import random
import sys
import pickle
from spacegame.Universe import Universe, Sector


def make_new_sector(backlink,newsector,level=1):
    if u.get_sector(newsector) is None:
        sector=Sector.Sector(sector_name=newsector)
        sector.add_link(backlink)
        u.add_sector(sector)
        size=len(u.map.keys())
        print("Added sector {sector}.  Universe now {size} sectors big.".format(sector=sector.name,size=size))
        numlinks=random.randint(1,MAX_LINKS-1)
        for new_links in range(1,numlinks):
            if len(u.map.keys()) == 1000:
                print "We're done here. Level={level}".format(level=level)
                return True
            newnewsector=random.randint(1,UNIVERSE_SIZE)
            created=False
            while not created:
               created=make_new_sector(newsector, newnewsector,level+1)
               newnewsector=random.randint(1,UNIVERSE_SIZE)
        pickle.dump( u, open( "universe.p", "wb" ) )
        return True
    else:
        return False           



UNIVERSE_SIZE=1000
MAX_LINKS=6

sys.setrecursionlimit(UNIVERSE_SIZE+1)

u=Universe.Universe()

center=random.randint(1,UNIVERSE_SIZE)
s=Sector.Sector(sector_name=center)
u.add_sector(s)
next_to_center=random.randint(1,UNIVERSE_SIZE)
make_new_sector(center,next_to_center)

