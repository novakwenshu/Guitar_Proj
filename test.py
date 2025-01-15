from lib.common import *
from src.Note import Note
from src.Chord import Chord
import time
import sounddevice as sd
import numpy as np
from IPython.display import display, Audio
import threading
import simpleaudio

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

c= []
c.append(Note('C3', 131))
c.append(Note('E3', 165))
c.append(Note('G3', 196))
c.append(Note('C4', 262))
c.append(Note('E4', 330))

c_chord = Chord(c)

am = []
am.append(Note('A2', 110))
am.append(Note('E3', 165))
am.append(Note('A3', 196))
am.append(Note('C4', 262))
am.append(Note('E4', 330))


am_chord = Chord(am)
#audio = am_chord.Down(1)

#delay = np.zeros(44100)
#sd.play(delay,samplerate=44100)
#sd.wait()

g_chord = Chord(chord)
audio = np.concat((am_chord.Down(0.5),am_chord.Down(0.5),am_chord.Up(0.25), am_chord.Down(0.25),am_chord.Up(0.25),g_chord.Down(0.5),g_chord.Down(0.5),g_chord.Up(0.25), g_chord.Down(0.25),g_chord.Up(0.25),c_chord.Down(0.5),c_chord.Down(0.5),c_chord.Up(0.25), c_chord.Down(0.25),c_chord.Up(0.25),c_chord.Down(0.5),c_chord.Down(0.5),c_chord.Up(0.25), c_chord.Down(0.25),c_chord.Up(0.25)))
sd.play(audio,samplerate=44100)
sd.wait()












