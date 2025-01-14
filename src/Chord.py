import threading
import numpy as np
import sounddevice as sd

class Chord:
    def __init__(self, notes):
        self.notes = notes
        self.reversed_notes = self.notes[::-1]

    def Up(self, duration):
        chord = []

        for note in self.reversed_notes[:3]:
            chord.append(note.play(duration))
        
        buffer = np.sum(chord, axis=0)

        # Need to normalize here or else it will produce static
        buffer = buffer / np.max(np.abs(buffer))
        audio = (buffer * 32767).astype(np.int16)

        sd.play(audio,samplerate=44100)
        sd.wait()

    def Down(self, duration):
        chord = []
        for note in self.notes:
            chord.append(note.play(duration))
        
        buffer = np.sum(chord, axis=0)

        buffer = buffer / np.max(np.abs(buffer))
        audio = (buffer * 32767).astype(np.int16)

        sd.play(audio,samplerate=44100)
        sd.wait()