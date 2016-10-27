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
    
def twitch(robots):
    set_active(robots)
    message("twitch", 1)

def set_active(robots):
    """Activates a set of robots"""
    for robot in robots:
        message(instruments[robot],1)
        time.sleep(0.02)

def set_inactive(robots):
    """Deactivates a set of robots"""
    for robot in robots:
        message(instruments[robot],0)
        time.sleep(0.02)

def send_beats (robots, beat_pattern):
    """Sends a beat pattern (specified in robot_orchestra.py) to a robot"""
    set_active(robots)
    message("beats", beat_pattern)
    time.sleep(0.02)
    set_inactive(robots)

def play(robots):
    """Activates the robots and then issues the play command."""
    set_active(robots)
    message("play", 1)
    set_inactive(robots)
