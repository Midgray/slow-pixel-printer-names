import json
#import lib.pythoncolornames.colornames as name
from lib.pythoncolornames.colornames import *
from lib.pythonthermalprinter.Adafruit_Thermal import *
import time

# Change this based on last pixel printed in previous run
START_PIX = 50000

# use find(r,g,b) from colornames

# set up printer
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

# set printer prefs
#printer.doubleWidthOn()
#printer.setDefault()
printer.boldOn()
#printer.inverseOn()
printer.justify('C')
printer.setSize('M')
printer.upsideDownOn()

# test this out to see if hasPaper() returns true
# try it without paper to make sure it returns false
print(printer.hasPaper())

#printer.println("Double Colonial White")

with open("loading_pink-dots.json") as file:
    # Load file content and make new dict
    data = json.load(file)

while printer.hasPaper():
    for idx, pixel in enumerate(data[START_PIX:]):
        
        # get rgb values, use rgb values to get color name
        rgb_name = find(pixel[0], pixel[1], pixel[2])
        
        # send color name string to printer

        print(idx, rgb_name)
        printer.println(rgb_name)
        
        # wait an appropriate amound of time for printer
        # this may not be necessary--could save paper
        time.sleep(5) # seconds. confirm best way to wait for printer

#while not printer.hasPaper():
    
for idx, pixel in enumerate(data[START_PIX:]):