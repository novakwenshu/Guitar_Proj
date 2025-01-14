import threading
class Chord:
    def __init__(self, notes):
        self.notes = notes
        self.reversed_notes = self.notes[::-1]

    def Up(self, duration):
        count = 0
        threads = []
        for note in self.reversed_notes:
            if count > 3:
                break
            thread = threading.Thread(target=note.play, args=([duration]))
            threads.append(thread)
            thread.start()
            count += 1

        for thread in threads:
            thread.join()

    def Down(self, duration):
        threads = []
        for note in self.notes:
            thread = threading.Thread(target=note.play, args=([duration]))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()