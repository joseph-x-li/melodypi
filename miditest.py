import mido
from mido import MidiFile
import serial
from pprint import pprint
import struct

mid = MidiFile('../Marunouchi.mid')
port = "/dev/ttyUSB0"


def modMessages(firstMsg, secondMsg, note, onOff = False):
    if not (note >= 53 and note <= 89): # ONLY NOTES F3(53) => F6(89)
        return (firstMsg, secondMsg)
    note = note - 53 # conversion to zero indexed
    if note <= 30:
        if onOff:
            firstMsg = firstMsg | (1<<(30-note))
        else:
            firstMsg = firstMsg & ~((1<<(30-note)))
    else:
        if onOff:
            secondMsg = secondMsg | (1<<(61-note))
        else:
            secondMsg = secondMsg & ~((1<<(61-note)))
    return (firstMsg, secondMsg)

message_1 = 0x80000000
message_2 = 0x00000000

USB = serial.Serial(port, 115200)
USB.flushInput()


for msg in mid.play():
    if not (msg.type == 'note_on' or msg.type == 'note_off'):
        continue
    note = msg.note
    print("NOTE: {}".format(note - 53))
    onOff = msg.type == 'note_on'
    (message_1, message_2) = modMessages(message_1, message_2, note, onOff)

    USB.write(struct.pack('>LL', message_1, message_2))
    print(message_1)
    print(message_2)
    print(msg)

# USB.write(defaultString.encode('utf-8'))