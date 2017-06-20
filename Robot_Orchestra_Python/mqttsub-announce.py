"""Listen for robot announcements.

When an instrument robot connects to the MQTT server, it announces itself.
This code simply echoes those announcements, but in principle we could
automatically update the instrument dictionary as robots join the orchestra.
"""
import paho.mqtt.client as mqtt


def on_connect(client, userdata, rc):
    """Connect to MQTT broker."""
    print "Connected with result code: " + str(rc)
    client.subscribe("orchestra/announce")


def on_message(client, userdata, msg):
    """Output diagnostic when message sent via broker."""
    print "Topic:", msg.topic + '  :  Message: ' + msg.payload

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('10.0.1.5', 1883)
# client.connect('192.168.0.8', 1883)
client.loop_forever()
