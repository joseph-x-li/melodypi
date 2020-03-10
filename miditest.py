import mido
from mido import MidiFile
import serial

mid = MidiFile('../Marunouchi.mid')
port = "/dev/ttyUSB0"

defaultString = "711111111111111111111111111111111111111"
messageString = "711111111111111111111111111111111111111"

x="700000000000000000000000000000000000000"

USB = serial.Serial(port, 9600)
USB.flushInput()

USB.write(defaultString.encode('utf-8'))

for msg in mid.play():
    if msg.is_meta:
        continue
    note = msg.note
    if not (note >=53 and note <=89): # ONLY NOTES F3(53) => F6(89)
        continue
    if msg.type == 'note_on':
        messageString[note-52] = '1'
    else:
        messageString[note-52] = '0'
    USB.write(messageString.encode('utf-8'))
    print(messageString)
    print(msg)

USB.write(defaultString.encode('utf-8'))