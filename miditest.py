import mido
from mido import MidiFile

mid = MidiFile('../Marunouchi.mid')



for msg in MidiFile('song.mid').play():
    DO THE SHIT WITH THE PORT N STUFF
    port.send(msg)