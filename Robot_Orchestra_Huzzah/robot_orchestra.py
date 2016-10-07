"""Robot Orchestra control code.

Distributes beat patterns to a network of robots, then cues sequence playback.
"""
import time
from mod_orchestra import set_active, beats, play


# Set up instrument groups
all = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11")
zero = ("00",)
one = ("01",)
two = ("02",)
three = ("03",)
four = ("04",)
five = ("05",)
six = ("06",)
seven = ("07",)
eight = ("08",)
nine = ("09",)
ten = ("10",)
eleven = ("11",)
# add your own groups here, for example:
drums = ("00", "04", "07")


# First, make sure the beat pattern is zeroed out for all instruments
set_active(all)
beats("0000")
time.sleep(0.2)

# Here's a pattern we're going to reuse
closing = "1010011"
# You could use similar things to define a chorus, an intro, and so on.

# Now configure pattern for each instrument
set_active(zero)
beats("10100000000000000000" + closing)
set_active(one)
beats("00001010000000000000" + closing)
set_active(two)
beats("00000000101000000000" + closing)
set_active(three)
beats("00000000000010100000" + closing)
set_active(four)
beats("00000000000000001010" + closing)
# ... and so on

# Finally, command all instruments to play at once
set_active(all)
play()
