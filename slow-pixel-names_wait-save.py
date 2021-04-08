# PIP INSTALL WAITING or install it locally https://pypi.org/project/waiting/

import json
import lib.pythoncolornames.colornames as name
from waiting import wait
from lib.pythoncolornames.colornames import *
from lib.pythonthermalprinter.Adafruit_Thermal import *
import time

# Change print speed
PRINT_DELAY = 5

# Change number in this file to set start pixel
SAVE_FILE = 'savestate.txt'

with open(SAVE_FILE, 'r') as r:
    START_PIX = int(r.read())

print(START_PIX)

# use find(r,g,b) from colornames

# set up printer
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

# set printer prefs

#printer.doubleWidthOn()
#printer.setDefault()
#printer.inverseOn()
printer.boldOn()
printer.justify('C')
printer.setSize('M')
printer.upsideDownOn()

# test line width
# printer.println("Double Colonial White")


# test this out to see if hasPaper() returns true
# try it without paper to make sure it returns false
print(printer.hasPaper())

with open("loading_pink-dots.json") as file:
    # Load file content and make new dict
    data = json.load(file)

for idx, pixel in enumerate(data[START_PIX:]):

    # keep track of position in json
    pixel_idx = idx + START_PIX
    
    # get rgb values, use rgb values to get color name
    rgb_name = find(pixel[0], pixel[1], pixel[2])
    
    # wait until printer has paper
    if not printer.hasPaper():
       print("Waiting for paper...")

    wait(printer.hasPaper(), sleep_seconds=20)

    # send color name string to printer
    print(idx, pixel_idx, rgb_name, pixel[0], pixel[1], pixel[2])
    printer.println(rgb_name)

    # save position to text file
    with open (SAVE_FILE, 'w') as a:
        a.write(str(pixel_idx + 1))
    
    # wait an appropriate amound of time for printer
    # this may not be necessary--could save paper
    time.sleep(PRINT_DELAY) # seconds