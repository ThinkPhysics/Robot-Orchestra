"""Robot orchestra abstractions.

Provides a simple language grammar for issuing beat patterns and playback
cue to Robot Orchestra instruments, and handles MQTT messaging.
"""
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()
mqtt_server = "10.0.1.4"

instruments = {"00": "skutter_18:FE:34:FD:91:AD",
               "01": "skutter_5C:CF:7F:01:5B:22",
               "02": "skutter_18:FE:34:FD:92:D1",
               "03": "skutter_18:FE:34:F4:D3:BD",
               "04": "skutter_18:FE:34:FD:93:33",
               "05": "skutter_18:FE:34:F4:D6:F4",
               "06": "skutter_5C:CF:7F:01:59:76",
               "07": "skutter_5C:CF:7F:0E:35:2D",
               "08": "skutter_18:FE:34:F4:D0:7B",
               "09": "skutter_18:FE:34:F4:D4:79",
               "10": "skutter_5C:CF:7F:0E:31:16",
               "11": "skutter_5C:CF:7F:0E:2C:EA"
               }


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
