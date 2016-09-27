"""Robot Orchestra server code.

Distributes and commands network of robots to play instruments.

TODO: Function to upload beat pattern to subset (array) of instruments.
"""
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()

def message(topic, payload):
    """Abstract out MQTT connection.

    Since it has to be done for each message, wrap it in a function
    """
    mqttc.connect('localhost', 1883)
    mqttc.publish("orchestra/" + topic, payload)


def setup():
    """Configure all the Skutters initially."""
    message("skutter_18:FE:34:FD:91:AD", 1)
    # message("twitch", 1)
    # time.sleep(1)
    message("beats", "1011010010110011")
    # time.sleep(1)
    message("play", 1)
    pass


def main():
    """Do the thing."""
    pass

if __name__ == '__main__':
    setup()
    main()
