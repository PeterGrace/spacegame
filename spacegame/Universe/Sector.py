'''Sector class implements the container that holds the stations, planets, and players in a particular sector.'''
import logging

class Sector():

    def __init__(self):
        self._id = 0
        self._name = ""
        self._stations = []
        self._planets = []
        self._players = []
    
    def player_enter(self,**kwargs):

        try:
            append(self._players,kwargs['player'])
            return True
        except KeyError as ex:
            logging.error("player_enter called without player keyword")
            return False


    @property
    def players(self):
        return self._players

    @property
    def id(self):
        return self._id
