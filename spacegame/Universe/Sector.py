'''Sector class implements the container that holds the stations, planets, and
   players in a particular sector.'''

import logging


class Sector():

    def __init__(self, **kwargs):
        self._name = kwargs['sector_name']
        self._stations = []
        self._planets = []
        self._players = []
        self._adjoining_sectors = []

    def player_enter(self, player):
            self._players.append(player)
            return True

    def add_station(self, station):
            self._stations.append(station)
            return True

    def add_planet(self, planet):
            self._planets.append(planet)
            return True
            
    @property
    def players(self):
        return self._players

    @property
    def name(self):
        return self._name

    @property
    def stations(self):
        return self._stations

    @property
    def planets(self):
        return self._planets    
