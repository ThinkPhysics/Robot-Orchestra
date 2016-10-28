'''This small program provide an easy way to test the robots, by causing them
to 'twitch' once every five seconds. Change which robots move by adding
number "01" to "11" into 'ROBOTS'
Cancel their twitching by pressing control-C in the Terminal.
'''
import time
from mod_orchestra import twitch, send_beats

ROBOTS = ("06","09")
#clears the robots current beat pattern
send_beats(ROBOTS, "0")
#tells the robots to beat once very five seconds
while  True == True:
    twitch(ROBOTS)
    time.sleep (5)
