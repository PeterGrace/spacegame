from Universe.Sector import Sector
from Universe.Player import Player
from Universe.Station import Station
from Universe.Planet import Planet
from Universe.Ship import Ship
from Universe.Universe import Universe

def test_new_sector():
    sector = Sector()
    assert(sector.id==0)

def test_add_player():
    universe = Universe()
    player = Player(name='Pete')
    universe.add_player(player)
    assert(player in universe.players)

