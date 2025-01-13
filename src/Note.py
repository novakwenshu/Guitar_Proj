from .Kstrong import *
from lib.common import *

class Note:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency
    
    def play(self, duration):
       return karplus_strong(self.frequency, duration)
    
    def getName(self):
        return self.name



         