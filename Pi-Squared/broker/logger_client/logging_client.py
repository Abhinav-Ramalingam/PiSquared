import json

import requests
import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

BROKER = '192.168.0.206'
PORT = 1883
USERNAME = 'abhinavram2002'
PASSWORD = '@209AoRQeFkeW'
LOGGER = "192.168.0.206"
LOG_PORT = 1337

props = Properties(PacketTypes.PUBLISH)
props.MessageExpiryInterval = 30  # in seconds


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, props):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if str(msg.topic).startswith("topic/"):
        j = json.loads(msg.payload)
        payload = {"topic": msg.topic, "username": j['username'], "deviceID": j['deviceID'], "message": j['message']}
        response = requests.post("http://{}:{}/log".format(LOGGER, LOG_PORT), json.dumps(payload))


def startClient():
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.username_pw_set(USERNAME, PASSWORD)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message

    mqttc.connect(BROKER, PORT, 60)
    mqttc.subscribe("topic/#")
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.

    mqttc.loop_forever()


if __name__ == '__main__':
    startClient()
