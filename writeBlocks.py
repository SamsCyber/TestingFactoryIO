from time import sleep
import snap7
from snap7.util import *
from snap7.types import *
import struct

plc = snap7.client.Client()
plc.connect("192.168.0.1", 0, 1)

outputData = []


# bytes[0] = plc.list_blocks()
# bytes[1] = plc.get_protection()
area = snap7.types.Areas.PA


startByte = 0
numberOfUnits = 8
word_length = WordLen.Byte
bit = 0

byteArray = plc.read_area(area, 0, startByte, numberOfUnits)

toWriteArray = bytearray(~b & 0xFF for b in byteArray)


while(True):
    # plc.write_area(area, 0, 0, toWriteArray)
    plc.as_write_area(area, 0, startByte, numberOfUnits, word_length, toWriteArray)
    time.sleep(0.0045)




