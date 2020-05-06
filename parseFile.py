import mido
from mido import MidiFile

# This file will be a class.
# Parses specified MIDI file to see how many tracks there are.
# Makes suggestion as to how the file will be played.
# Checks there are no notes shorter than $DELAY, which would cause issues.

class FileParser:
    def __init__(self, filename = None, noteWrapping = False, doubleWidth = False, transpose = 0, speed = 1):
        self.filename = filename
        self.noteWrapping = noteWrapping
        self.doubleWidth = doubleWidth
        self.transpose = transpose
        self.speed = speed
        self.isPlaying = False

    def __repr__(self):
        def helper(x): 
            if x == 0: return ""
            return "Up " if x > 0 else "Down "
        retVal = f"Filename: {self.filename}\nSpeed: {self.speed}x\nTransposed {helper(self.transpose)}By: {abs(self.transpose)} semitone{'' if abs(self.transpose) == 1 else 's'}\n"
        retVal += f"Is Double Width: {self.doubleWidth}\nIs Note Wrapping On: {self.noteWrapping}"
        retVal = "\n------------------------------------------------------------\n" + retVal
        retVal += "\n------------------------------------------------------------\n"
        return retVal

    def setTranspose(self, toThis):
        self.transpose = toThis

    def setNoteWrapping(self, toThis):
        self.noteWrapping = toThis

    def setDoubleWidth(self, toThis):
        self.doubleWidth = toThis
    
    def setFile(self, toThis):
        self.filename = toThis

    def setSpeed(self, toThis):
        self.speed = toThis

    def play(self):
        if self.isPlaying:
            return None
        assert(False == True)
        #random shit

    def pause(self):
        assert(False == True)
        #random shit
    
    def restart(self):
        assert(False == True)
        #random shit

    # def __createNote(self, )

#unit test
x = FileParser()
print(x)