"""Robot Orchestra control code.

Distributes beat patterns to a network of robots, then cues sequence playback.
"""
# import time
from mod_orchestra import send_beats, play
from instruments import ALL, PLAYERS


# clears the robots' beat patterns
send_beats(ALL, "0")

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
