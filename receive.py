import mido
from mido import MidiFile
import serial
from pprint import pprint
import struct
import time

port = "/dev/ttyUSB0"


USB = serial.Serial(port, 9600)
USB.flushInput()
time.sleep(3)

msgChar = 0b10000000

USB.write(struct.pack('>B', msgChar))