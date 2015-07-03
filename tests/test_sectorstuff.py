from spacegame.Universe.Sector import Sector
from spacegame.Universe.Player import Player
from spacegame.Universe.Station import Station
from spacegame.Universe.Planet import Planet
from spacegame.Universe.Ship import Ship
from spacegame.Universe.Universe import Universe

def test_new_sector():
    universe = Universe()
    sector = Sector(sector_name='Test Sector')
    universe.add_sector(sector)
    assert(sector.name in universe.map.keys())


def test_add_player():
    universe = Universe()
    player = Player(player_name='Pete')
    universe.add_player(player)
    assert(player.name in universe.players.keys())

def test_add_planet_to_sector():    
    pass
