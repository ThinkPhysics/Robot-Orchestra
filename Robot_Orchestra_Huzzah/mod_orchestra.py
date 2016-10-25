"""Robot orchestra abstractions.

Provides a simple language grammar for issuing beat patterns and playback
cue to Robot Orchestra instruments, and handles MQTT messaging to distribute
those commands.

Can be straightforwardly extended to simplify grammar, which we leave as an
exercise for workshop participants.
"""
import time
import paho.mqtt.client as mqtt
from instruments import instruments

mqttc = mqtt.Client()
mqtt_server = "10.0.1.4"


def message(topic, payload):
    """Abstract out MQTT connection.

    Since it has to be done for each message, wrap it in a function.
    """
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish("orchestra/" + topic, payload)
    # time.sleep(0.2)


def set_active(robots):
    """Target specific robot(s) so they respond to subsequent commands."""
    # print "Setting active: "
    # print robots
    # First set all robots inactive...
    for instrument in instruments:
        # print "Setting instrument " + instrument + " inactive"
        message(instruments[instrument], 0)
        time.sleep(0.02)
    # ...now enable just the target robots
    for robot in robots:
        # print robot
        # print "Setting instrument " + robot + " ACTIVE"
        message(instruments[robot], 1)
        time.sleep(0.02)
        # print "Instrument key:" + robot
        # print "Instrument value:" + instruments[robot]


def beats(pattern):
    """Send beat pattern to robots."""
    # print "Beats: " + pattern
    message("beats", pattern)


def play():
    """Issue the play command."""
    message("play", 1)
