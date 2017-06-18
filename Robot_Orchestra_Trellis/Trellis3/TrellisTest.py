# This is a test example for the Adafruit Trellis w/HT16K33
#
#   Designed specifically to work with the Adafruit Trellis
#   ----> https://www.adafruit.com/products/1616
#   ----> https://www.adafruit.com/products/1611
#
#   These displays use I2C to communicate, 2 pins are required to
#   interface
#   Adafruit invests time and resources providing this open source code,
#   please support Adafruit and open-source hardware by purchasing
#   products from Adafruit!
#
#   Written by Limor Fried/Ladyada for Adafruit Industries.
#   MIT license, all text above must be included in any redistribution
#
#   Python port created by Tony DiCola (tony@tonydicola.com).

import time
import Adafruit_Trellis
import numpy as np
from threading import Timer
from instruments import instruments, ALL
from mod_orchestra import playset

currentBeat = 0
tempo = 120  # Barfs if we go much above 120; playBeat doesn't complete before
             # it's next called. Ugh.
bpm = 60.0 / tempo
curState = np.array([0, 0, 0, 0, 0, 0, 0, 0])

class RepeatedTimer(object):
    """Simple timer class, from StackExchange (obviously)."""
    def __init__(self, interval, function, *args):
        """Initialize the timer object."""
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.is_running = False
        self.start()

    def _run(self):
        """Timer has been triggered: execute callback function."""
        self.is_running = False
        self.start()
        self.function(*self.args)

    def start(self):
        """Start the timer, if it's not already running."""
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        """Stop the timer."""
        self._timer.cancel()
        self.is_running = False



matrix0 = Adafruit_Trellis.Adafruit_Trellis()
matrix1 = Adafruit_Trellis.Adafruit_Trellis()
matrix2 = Adafruit_Trellis.Adafruit_Trellis()
matrix3 = Adafruit_Trellis.Adafruit_Trellis()
matrix4 = Adafruit_Trellis.Adafruit_Trellis()
matrix5 = Adafruit_Trellis.Adafruit_Trellis()
matrix6 = Adafruit_Trellis.Adafruit_Trellis()
matrix7 = Adafruit_Trellis.Adafruit_Trellis()

trellis = Adafruit_Trellis.Adafruit_TrellisSet(matrix0, matrix1, matrix2,
                                               matrix3, matrix4, matrix5,
                                               matrix6, matrix7)

# set to however many you're working with here, up to 8 per I2C bus
NUMTRELLIS = 8
numKeys = NUMTRELLIS * 16


# Connect Trellis Vin to 5V and Ground to ground.
# Connect Trellis INT wire to a digital input (optional)
# Connect Trellis I2C SDA pin to your board's SDA line
# Connect Trellis I2C SCL pin to your board's SCL line
# All Trellises on an I2C bus share the SDA, SCL and INT pin!
# Even 8 tiles use only 3 wires max

# Set this to the number of the I2C bus that the Trellises are attached to:
I2C_BUS = 1

# Setup
print('Trellis Active')

# TODO: Setup the INT input

# begin() with the I2C addresses and bus numbers of each panel in order
trellis.begin((0x70, I2C_BUS), (0x71, I2C_BUS), (0x72, I2C_BUS),
              (0x73, I2C_BUS), (0x74, I2C_BUS), (0x75, I2C_BUS),
              (0x76, I2C_BUS), (0x77, I2C_BUS))

# It's ridiculous to pull in all of Numpy just to do a two-dimensional
# array, but apparently that's what I'm doing.
# Also: yes, I typed this out by hand.
buttonGrid = np.array(
                      [[  0,   1,   2,   3,  16,  17,  18,  19,  32,  33,  34,  35,  48,  49,  50,  51],
                       [  4,   5,   6,   7,  20,  21,  22,  23,  36,  37,  38,  39,  52,  53,  54,  55],
                       [  8,   9,  10,  11,  24,  25,  26,  27,  40,  41,  42,  43,  56,  57,  58,  59],
                       [ 12,  13,  14,  15,  28,  29,  30,  31,  44,  45,  46,  47,  60,  61,  62,  63],
                       [ 64,  65,  66,  67,  80,  81,  82,  83,  96,  97,  98,  99, 112, 113, 114, 115],
                       [ 68 , 69,  70,  71,  84,  85,  86,  87, 100, 101, 102, 103, 116, 117, 118, 119],
                       [ 72,  73,  74,  75,  88,  89,  90,  91, 104, 105, 106, 107, 120, 121, 122, 123],
                       [ 76,  77,  78,  79,  92,  93,  94,  95, 108, 109, 110, 111, 124, 125, 126, 127]]
                     )

# for row in range(8):
#     for column in range(16):
#         trellis.setLED(buttonGrid[row, column])
#         trellis.writeDisplay()
#         time.sleep(0.01)
#
# for row in range(8):
#     for column in range(16):
#         trellis.clrLED(buttonGrid[row, column])
#         trellis.writeDisplay()
#         time.sleep(0.01)


def playBeat():
    global currentBeat
    global curState

    target = buttonGrid[0, currentBeat]

    # Get current state of this column of buttons
    for row in range(8):
        curState[row] = trellis.isLED(buttonGrid[row, currentBeat])

    # Concatenate array into string, for MQTT sending
    # array2string adds square braces; slice to remove them.
    curStateString = np.array2string(curState, separator='')[1:-1]
    # print curStateString

    # flash column header
    # It's rather too slow to flash the whole column, which is what I wanted,
    # so this will have to do. Boo!
    trellis.clrLED(target)
    trellis.writeDisplay()
    trellis.setLED(target)
    trellis.writeDisplay()
    # time.sleep(bpm/4)
    # print curState[0]
    # Return to previous state
    if curState[0] == 1:
        trellis.setLED(target)
    else:
        trellis.clrLED(target)

    # Command the orchestra!
    playset(curStateString)
    # ...and update the display
    trellis.writeDisplay()

    # set up for next beat
    currentBeat += 1
    if currentBeat > 15:
        currentBeat = 0


# Loop
print('Press Ctrl-C to quit.')

trellis.clear()
trellis.writeDisplay()

# Initialise the timer, which will trigger at a rate specified by the
# bpm setting (ie, tempo)
rt = RepeatedTimer(bpm, playBeat)

# The main loop now only needs to handle
try:
    while True:
        time.sleep(0.08)

        # If a button was just pressed or released...
        if trellis.readSwitches():
            # go through every button
            for i in range(numKeys):
                # if it was pressed...
                if trellis.justPressed(i):
                    print('Button: {0}'.format(i))
                    # Alternate the LED
                    if trellis.isLED(i):
                        trellis.clrLED(i)
                    else:
                        trellis.setLED(i)
            # tell the trellis to set the LEDs we requested
            # trellis.writeDisplay()
finally:
    rt.stop()
