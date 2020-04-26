import mido
from mido import MidiFile

# This file will be a class.
# Parses specified MIDI file to see how many tracks there are.
# Makes suggestion as to how the file will be played.
# Checks there are no notes shorter than $DELAY, which would cause issues.