import mido
from mido import MidiFile
import serial
from pprint import pprint
import struct
import time

mid = MidiFile('../tester.mid')
port = "/dev/ttyUSB0"


def createMessage(note, onOff = False):
    emptyMsg = 0b00000000
    if not (note >= 53 and note <= 89): # ONLY NOTES F3(53) => F6(89)
        return None
    note = note - 53 # conversion to zero indexed
    if onOff:
        emptyMsg = emptyMsg | 0b01000000
    emptyMsg += note
    return emptyMsg

USB = serial.Serial(port, 9600)
USB.flushInput()
time.sleep(3)


for msg in mid.play():
    if not (msg.type == 'note_on' or msg.type == 'note_off'):
        continue
    note = msg.note
    print("NOTE: {}, {}".format(note - 53, "ON" if msg.type == 'note_on' else "OFF"))
    onOff = msg.type == 'note_on'
    msgChar = createMessage(note, onOff)
    if msgChar is None:
        continue
    USB.write(struct.pack('>B', msgChar))
