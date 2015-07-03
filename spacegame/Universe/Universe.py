from Player import Player
from Player import NPC

class Universe():
    def __init__(self):
        self._map=[]
        self._players=[]
        self._npcs=[]

    def add_player(self,player):
        try:
            self._players.append(player)
        except KeyError:
            logging.error("add_player: can't add player, kwargs did not contain playername.")

    @property
    def players(self):
        return self._players


