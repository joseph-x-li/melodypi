import mido
from mido import MidiFile
import serial
from pprint import pprint
import struct

mid = MidiFile('../Marunouchi.mid')
port = "/dev/ttyUSB0"


def createMessage(note, onOff = False):
    emptyMsg = 0b00000000
    if not (note >= 53 and note <= 89): # ONLY NOTES F3(53) => F6(89)
        return None
    note = note - 53 # conversion to zero indexed
    if onOff:
        emptyMsg = emptyMsg | 0b10000000
    emptyMsg += note
    return emptyMsg

USB = serial.Serial(port, 115200)
USB.flushInput()


for msg in mid.play():
    if not (msg.type == 'note_on' or msg.type == 'note_off'):
        continue
    note = msg.note
    print("NOTE: {}".format(note - 53))
    onOff = msg.type == 'note_on'
    msgChar = createMessage(note, onOff)
    if msgChar is None:
        continue
    USB.write(msgChar)
    # print(struct.pack('>B', msgChar))
    print(msgChar)
    print(msg)


# USB.write(defaultString.encode('utf-8'))