"""Robot Orchestra control code.

Distributes beat patterns to a network of robots, then cues sequence playback.
"""
import time
from mod_orchestra import set_active, beats, play


# Set up instrument groups
ALL = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11")
ZERO = ("00",)
ONE = ("01",)
TWO = ("02",)
THREE = ("03",)
FOUR = ("04",)
FIVE = ("05",)
SIX = ("06",)
SEVEN = ("07",)
EIGHT = ("08",)
NINE = ("09",)
TEN = ("10",)
ELEVEN = ("11",)
# add your own groups here, for example:
DRUMS = ("00", "04", "07")


# First, make sure the beat pattern is zeroed out for all instruments
set_active(ALL)
beats("0000")
time.sleep(0.2)

# Here's a pattern we're going to reuse
CLOSING = "1010011"
# You could use similar things to define a chorus, an intro, and so on.

# Now configure pattern for each instrument
set_active(ZERO)
beats("10100000000000000000" + CLOSING)
set_active(ONE)
beats("00001010000000000000" + CLOSING)
set_active(TWO)
beats("00000000101000000000" + CLOSING)
set_active(THREE)
beats("00000000000010100000" + CLOSING)
set_active(FOUR)
beats("00000000000000001010" + CLOSING)
# ... and so on

# Finally, command all instruments to play at once
set_active(ALL)
play()
