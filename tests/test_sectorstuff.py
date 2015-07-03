from spacegame.Universe.Sector import Sector
from spacegame.Universe.Player import Player
from spacegame.Universe.Station import Station
from spacegame.Universe.Planet import Planet
from spacegame.Universe.Ship import Ship
from spacegame.Universe.Universe import Universe

def test_new_sector():
    sector = Sector()
    assert(sector.id==0)


def test_add_player():
    universe = Universe()
    player = Player(name='Pete')
    universe.add_player(player)
    assert(player in universe.players)
