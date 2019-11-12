class Participant:
    """Participant Class to store the Participant's data"""
    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score
     
