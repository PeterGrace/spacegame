'''Sector class implements the container that holds the stations, planets, and
   players in a particular sector.'''

import logging


class Sector():

    def __init__(self, **kwargs):
        self._name = kwargs['sector_name']
        self._stations = []
        self._planets = []
        self._players = []

    def player_enter(self, **kwargs):
        try:
            append(self._players, kwargs['player_name'])
            return True
        except KeyError as ex:
            logging.error("player_enter called without player keyword")
            return False

    @property
    def players(self):
        return self._players

    @property
    def name(self):
        return self._name

