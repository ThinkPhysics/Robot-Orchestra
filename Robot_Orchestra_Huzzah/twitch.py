"""Test robots during construction by commanding Twitch every 5 seconds.

Change which robots move by adding number their numbers into 'ROBOTS'
Cancel their twitching by pressing control-C in the Terminal.
"""
import time
from mod_orchestra import twitch, send_beats
from instruments import instruments, ALL

ROBOTS = (ALL)

# clears the robots current beat pattern
send_beats(ROBOTS, "0")

# tells the robots to beat once very five seconds
while True:
    print "Bong!"
    twitch(ROBOTS)
    time.sleep(5)
