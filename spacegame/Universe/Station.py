class Station():
    def __init__(self, **kwargs):
        self._name = kwargs['station_name']

    @property
    def name(self):
        return self._name    
