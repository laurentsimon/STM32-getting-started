#!/usr/bin/env python3
import serial
import sys
import binascii
import io
import time

#dev = serial.Serial(port="/dev/tty.SLAB_USBtoUART", baudrate=115200, rtscts=True, dsrdtr=True)
dev = serial.Serial("/dev/cu.SLAB_USBtoUART", 115200)
#dev = serial.Serial("/dev/cu.usbmodem1413103", 115200)

dev.flushInput()
time.sleep(0.1)
#dev.reset_input_buffer()
#sio = io.TextIOWrapper(io.BufferedRWPair(dev, dev), newline='\r\n')
print("> Returned data:", file=sys.stderr)

FL = True
def getLine():
    global FL
    x = b''
    while True:
        x = b''.join([x, dev.read()])
        if FL:  
            FL = False
            x = x[1:]
        if len(x) >= 2 and x[-2:] == b'\r\n':
            return x[:-2]
while True:

#    x = sio.readline() #.decode('utf-8')
#    x = dev.read()
#    x = dev.readline()
#    if x == b"\r\n":
#        print("received end\n")
#        continue
#    dev.flushInput()
#    x = dev.readline()

    x = getLine()
#    print("len(x):%d" % len(x))
#    print("hex: %s" % binascii.hexlify(bytearray(x)))
#    print("data:%s" % x)
#    sys.stdout.write(x)
    sys.stdout.buffer.write(x)
#    sys.stdout.buffer.write(b'\n')
    sys.stdout.flush()
