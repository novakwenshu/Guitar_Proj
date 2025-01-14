from .Kstrong import *
from lib.common import *
import sounddevice as sd



class Note:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency
    
    def play(self, duration):
        buffer = karplus_strong(self.frequency, duration)
        sd.play(buffer,samplerate=44100)
        sd.wait()

    def getName(self):
        return self.name



         