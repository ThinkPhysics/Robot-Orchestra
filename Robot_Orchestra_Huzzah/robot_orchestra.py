"""Robot Orchestra control code.

Distributes beat patterns to a network of robots, then cues sequence playback.
"""
import time
from mod_orchestra import send_beats, set_active, set_inactive, play


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
DRUMS = ("00","11")

# Here are patterns we're going to reuse
CLOSING = "01"
BEAT_1 = "1000"
BEAT_2 = "0100"
BEAT_3 = "0010"
BEAT_4 = "0001"
# You could use similar things to define a chorus, an intro, and so on.

#Remember to clear the beat patterns before starting!
send_beats(ALL, "0")

# Now configure pattern for each instrument
send_beats(ONE, BEAT_1 + CLOSING + BEAT_4 + CLOSING + "1000100010001")
send_beats(TWO, BEAT_2 + CLOSING + BEAT_3 + CLOSING + "0010000000101")
send_beats(THREE, BEAT_3 + CLOSING + BEAT_2 + CLOSING + "0101001001011")
send_beats(FOUR, BEAT_4 + CLOSING + BEAT_1 + CLOSING + "0000010100001")
# ... and so on

# Finally, command all instruments to play at once
play(ALL)
