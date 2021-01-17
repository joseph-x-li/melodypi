# https://github.com/vishnubob/python-midi
# https://github.com/bspaans/python-mingus

import pygame
import mido
import time
from mido import MidiFile
from analysis import analyze


notedict = {
    0: "C",
    1: "C#/Db",
    2: "D",
    3: "D#/Eb",
    4: "E",
    5: "F",
    6: "F#/Gb",
    7: "G",
    8: "G#/Ab",
    9: "A",
    10: "A#/Bb",
    11: "B",
}


def note2beep(note):
    octave, mod = divmod(note, 12)
    ret = str(octave - 2) + notedict[mod]
    return ret


mid = analyze(MidiFile('midi/camp.mid'), merge=False)

mid.save("__generated.mid")


def play_music(midi_filename):
    '''Stream music_file in a blocking manner'''
    clock = pygame.time.Clock()
    pygame.mixer.music.load(midi_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)  # check if playback has finished


# mixer config
freq = 44100  # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)

try:
    play_music("__generated.mid")
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit
