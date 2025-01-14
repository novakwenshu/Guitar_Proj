from lib.common import *
from src.Note import Note
from src.Chord import Chord
import time
import sounddevice as sd
import numpy as np
from IPython.display import display, Audio
import threading

'''
scale = []
for key, value in fifth_string.items():
    to_add = Note(str(key), int(value))
    scale.append(to_add)


print(len(scale))
for i in range(len(scale)):
   sd.play(scale[i].play(1),samplerate=44100)
   sd.wait()

'''
   
chord = []

chord.append(Note('G2', 98))
chord.append(Note('B2', 124))
chord.append(Note('D3', 147))
chord.append(Note('G3', 196))
chord.append(Note('B3', 247))
chord.append(Note('G4', 392))

g_chord = Chord(chord)

g_chord.Down(0.2)
g_chord.Up(0.2)








