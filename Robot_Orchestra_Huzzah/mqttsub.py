"""Listen for (and output) commands issued via MQTT broker."""
import paho.mqtt.client as mqtt


def on_connect(client, userdata, rc):
    """Connect to MQTT broker."""
    print "Connected with result code: " + str(rc)
    client.subscribe("orchestra/skutter_18:FE:34:F4:D6:F4")
    client.subscribe("orchestra/skutter_18:FE:34:F4:D4:79")
    client.subscribe("orchestra/skutter_5C:CF:7F:0E:2C:EA")
    client.subscribe("orchestra/skutter_5C:CF:7F:01:59:76")
    client.subscribe("orchestra/skutter_18:FE:34:F4:D3:BD")
    client.subscribe("orchestra/skutter_5C:CF:7F:01:59:5B")
    client.subscribe("orchestra/skutter_5C:CF:7F:0E:35:2D")
    client.subscribe("orchestra/skutter_18:FE:34:FD:92:D1")
    client.subscribe("orchestra/skutter_5C:CF:7F:0E:31:16")
    client.subscribe("orchestra/twitch")
    client.subscribe("orchestra/beats")
    client.subscribe("orchestra/play")


def on_message(client, userdata, msg):
    """Output diagnostic when message sent via broker."""
    print "Topic: ", msg.topic + '\nMessage: ' + msg.payload

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('localhost', 1883)
client.loop_forever()
