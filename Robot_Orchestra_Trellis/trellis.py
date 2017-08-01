"""Run the Trellis controller off a Raspberry Pi Zero W."""

# Install the Python library:
# https://github.com/tdicola/Adafruit_Trellis_Python

# See notes about I2C here:
# https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

# This code heavily based on Adafruit example code by Limor Fried & Tony DiCola

import time
import Adafruit_Trellis

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

NUMTRELLIS = 8
numKeys = NUMTRELLIS * 16

# Connect Trellis Vin to 5V and Ground to ground.
# Connect Trellis INT wire to a digital input (optional)
# Connect Trellis I2C SDA pin to your board's SDA line
# Connect Trellis I2C SCL pin to your board's SCL line

# Set this to the number of the I2C bus that the Trellises are attached to:
I2C_BUS = 1

print "Robot Orchestra Trellis Controller >>> starting up"

trellis.begin((0x70, I2C_BUS), (0x71, I2C_BUS), (0x72, I2C_BUS),
              (0x73, I2C_BUS), (0x74, I2C_BUS), (0x75, I2C_BUS),
              (0x76, I2C_BUS), (0x77, I2C_BUS))

delay = 0.005

# Light all the LEDs in order
for i in range(numKeys):
    trellis.setLED(i)
    trellis.writeDisplay()
    time.sleep(delay)
# then turn them off again
for i in range(numKeys):
    trellis.clrLED(i)
    trellis.writeDisplay()
    time.sleep(delay)
