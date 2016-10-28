"""Robot Orchestra control code.

Distributes beat patterns to a network of robots, then cues sequence playback.
"""
import time
from mod_orchestra import send_beats, set_active, set_inactive, play


# Set up instrument groups
ALL = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11")
#clears the robots' beat patterns
send_beats(ALL, "0")
# These could include things like a 'drums' section
'''This dictionary holds the names and coreesponding numbers of each of the
instruments'''
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
       }

#Opens a seperate text file and uses that to send beat patterns to the instruments
with open('TwinkleTwinkle.txt', 'r') as music:
    total = music.readlines()
# splits the txt file into smaller and smaller fragments
    for line in total:
        beats = line.split(":")
        robot = (beats[0]).replace(':','')
        pattern = (beats[1]).replace(' ', '')
        pattern = pattern.replace('\n','')
# Compares the number in the txt file with the items in the dictionary 'players'
        for number in PLAYERS:
            if robot == number:
                robo_num = PLAYERS[number]
# sends the beat pattern to a specific robot
        send_beats(robo_num,pattern)

#Sets all of the instruments to play
play(ALL)
