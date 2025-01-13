from lib.common import *
from src.Note import Note
import time
import sounddevice as sd


scale = []
for key, value in fifth_string.items():
    to_add = Note(str(key), int(value))
    scale.append(to_add)


print(len(scale))
for i in range(len(scale)):
   sd.play(scale[i].play(1),samplerate=44100)
   sd.wait()


