from time import sleep
import sys
import snap7
from snap7.util import *
from snap7.types import *
import struct
from contextlib import suppress

plc = snap7.client.Client()
plc.connect("192.168.0.1", 0, 1)

def inputFail(input, byteOrBit: int) -> int:
    try:
        valByte = int(input)
        if(byteOrBit == 0):
            if(valByte < 0 or valByte >65525):
                raise ValueError
        if(byteOrBit == 1):
            if(valByte < 0 or valByte>7):
                raise ValueError
    except ValueError:
        if(byteOrBit == 0):
            print("Please enter a byte from 0-65,525.")
        if(byteOrBit == 1):
            print("Please enter a bit from 0-7")
        sys.exit()
    return(valByte)

whatByte = inputFail(input("What Byte do you want to interfere with? \n"), 0)
whatBit = inputFail(input("What Bit do you want to interfere with? \n"), 1)

plc = snap7.client.Client()
plc.connect("192.168.0.1", 0, 1)

numberOfUnits = 1
