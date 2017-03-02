"""Test robots during construction by commanding Twitch every 5 seconds.

Change which robots move by adding number their numbers into 'ROBOTS'
Cancel their twitching by pressing control-C in the Terminal.
"""
import time
from mod_orchestra import twitch, send_beats

ROBOTS = ("06", "09")

# clears the robots current beat pattern
send_beats(ROBOTS, "0")

# tells the robots to beat once very five seconds
while True:
    twitch(ROBOTS)
    time.sleep(5)
