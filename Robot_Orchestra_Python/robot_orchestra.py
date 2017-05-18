"""Robot Orchestra control code.

Distributes beat patterns to a network of robots, then cues sequence playback.
"""
# import time
from mod_orchestra import send_beats, play
# from instruments import instruments, ALL

# Set up instrument groups
ALL = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
       "12", "13", "14", "D00", "D01", "D02", "D03", "D04", "D05", "D06",
       "D07", "D08", "D09", "D10", "D11", "D12", "D13", "D14", "D15", "D16",
       "D17", "D18", "D19")

# clears the robots' beat patterns
send_beats(ALL, "0")


# Dictionary holds name and corresponding number for each instrument.
# Note: could include multiple robots for a given name.
# (see DRUMS for an example)
PLAYERS = {"ZERO": ("00",),
           "ONE": ("01",),
           "TWO": ("02",),
           "THREE": ("03",),
           "FOUR": ("04",),
           "FIVE": ("05",),
           "SIX": ("06",),
           "SEVEN": ("07",),
           "EIGHT": ("08",),
           "NINE": ("09",),
           "TEN": ("10",),
           "ELEVEN": ("11",),
           "TWELVE": ("12",),
           "THIRTEEN": ("13",),
           "FOURTEEN": ("14",),
           "DZERO": ("D00",),
           "DONE": ("D01",),
           "DTWO": ("D02",),
           "DTHREE": ("D03",),
           "DFOUR": ("D04",),
           "DFIVE": ("D05",),
           "DSIX": ("D06",),
           "DSEVEN": ("D07",),
           "DEIGHT": ("D08",),
           "DNINE": ("D09",),
           "DTEN": ("D10",),
           "DELEVEN": ("D11",),
           "DTWELVE": ("D12",),
           "DTHIRTEEN": ("D13",),
           "DFOURTEEN": ("D14",),
           "DFIFTEEN": ("D15",),
           "DSIXTEEN": ("D16",),
           "DSEVENTEEN": ("D17",),
           "DEIGHTEEN": ("D18",),
           "DNINETEEN": ("D19",),
           "DRUMS": ("00", "01")
           }

# Open seperate text file to specify beat patterns to send
with open('default.txt', 'r') as music:
    lines = music.readlines()

    # Iterate over lines in input
    for line in lines:
        # Break each input line between robot identifier and pattern
        data = line.split(":")
        robot = data[0]
        # robot = (data[0]).replace(':', '')  // Removed since unnecessary?

        # Get robot target tuple from PLAYERS dictionary
        robo_ids = PLAYERS[robot]

        # Remove white space & EOL from beat pattern
        pattern = (data[1]).replace(' ', '')
        pattern = pattern.replace('\n', '')

        # Now send the beat pattern to the target robots
        print robot + " to play " + pattern
        send_beats(robo_ids, pattern)

# Command playback on all instruments
play(ALL)
print ">>>> Go!"
