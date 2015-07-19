from Player import Player
from Player import NPC
from Sector import Sector


class Universe():
    def __init__(self):
        self._map = {}
        self._players = {}
        self._npcs = {}

    def add_player(self, player):
        try:
            self._players[player.name]=player
        except KeyError:
            logging.error("add_player: can't add player, kwargs did not contain"
                          " playername.")

    def add_sector(self, sector):
        try:
            self._map[sector.name]=sector
        except KeyError:
            logging.error("add_sector: can't add sector, kwargs did not contain"
                          " sectorname.")

    def get_sector(self, sector):
        if sector in self._map.keys():
            return self._map[sector]
        else:
            return None

    @property
    def players(self):
        return self._players
    
    @property
    def map(self):
        return self._map    

