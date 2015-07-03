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

def test_add_station_to_sector():    
    universe = Universe()
    sector = Sector(sector_name='Test Sector')
    station = Station(station_name='Test Station')
    sector.add_station(station)
    universe.add_sector(sector)
    assert(station in sector.stations)

def test_add_planet_to_sector():    
    universe = Universe()
    sector = Sector(sector_name='Test Sector')
    planet = Station(station_name='Test Planet')
    sector.add_planet(planet)
    universe.add_sector(sector)
    assert(planet in sector.planets)

