import time
from mod_orchestra import twitch, set_inactive

ROBOTS = ("01","02","03","04","05","00","11")
stop = "n"
while  stop == "n":
    twitch(ROBOTS)
    time.sleep (5)
