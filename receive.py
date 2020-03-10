import serial
import time
import struct
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    ser.flush()
    message_1 = 0xFFFFFFFF
    message_2 = 0x00000000
    while True:
        ser.write(struct.pack('>L', message_1))
        ser.write(struct.pack('>L', message_2))
        print(struct.pack('>L', message_1))
        print(struct.pack('>L', message_2))
        print("sent shit")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)