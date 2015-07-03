class CharacterBase():
    def __init__(self, **kwargs):
        self._name = kwargs['player_name']
        self._location = None
        self._inventory = {}

    @property
    def name(self):
        return self._name

class Player(CharacterBase):
    def __init__(self, **kwargs):
        CharacterBase.__init__(self, **kwargs)


class NPC(CharacterBase):
    def __init__(self, **kwargs):
        CharacterBase.__init__(self, **kwargs)
