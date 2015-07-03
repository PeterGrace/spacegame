class CharacterBase():
    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._location = None
        self._inventory = {}


class Player(CharacterBase):
    def __init__(self, **kwargs):
        CharacterBase.__init__(self, **kwargs)


class NPC(CharacterBase):
    def __init__(self, **kwargs):
        CharacterBase.__init__(self, **kwargs)
