"""Robot Orchestra control code.

Distributes and commands network of robots to play instruments.
"""
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()

instruments = {"00": "skutter_18:FE:34:FD:91:AD",
               "01": "skutter_5C:CF:7F:01:5B:22",
               "02": "skutter_18:FE:34:FD:92:D1",
               "03": "skutter_18:FE:34:F4:D3:BD",
               "04": "skutter_18:FE:34:FD:93:33"
               }


def message(topic, payload):
    """Abstract out MQTT connection.

    Since it has to be done for each message, wrap it in a function.
    """
    mqttc.connect('localhost', 1883)
    mqttc.publish("orchestra/" + topic, payload)
    # time.sleep(0.2)


def set_active(robots):
    """Target specific robot(s) so they respond to subsequent commands."""
    # print "Setting active: "
    # print robots
    # First set all robots inactive...
    for instrument in instruments:
        message(instruments[instrument], 0)
    # ...now enable just the target robots
    time.sleep(0.2)
    for robot in robots:
        # print robot
        message(instruments[robot], 1)
        # print "Instrument key:" + robot
        # print "Instrument value:" + instruments[robot]
    time.sleep(0.2)


def beats(pattern):
    """Send beat pattern to robots."""
    # print "Beats: " + pattern
    message("beats", pattern)


def play():
    """Issue the play command."""
    message("play", 1)

# Set up instrument groups
all = ("00", "01", "02", "03", "04")
zero = ("00",)
one = ("01",)
two = ("02",)
three = ("03",)
four = ("04",)
# add your own groups here, for example:
drums = ("00", "04")


# First, make sure the beat pattern is zeroed out for all instruments
set_active(all)
beats("0000")

# Now configure pattern for each instrument
set_active(zero)
beats("101000000000000000000101")
set_active(one)
beats("000010100000000000000101")
set_active(two)
beats("000000001010000000000101")
set_active(three)
beats("000000000000101000000101")
set_active(four)
beats("000000000000000010100101")

# ...and finally command all instruments to play at once
set_active(all)
play()
