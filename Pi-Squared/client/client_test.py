#!/usr/bin/env python3
import json

import paho.mqtt.client as mqtt
from configparser import ConfigParser
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 


parser = ConfigParser()
config = parser.read("./config/client.conf")


properties=Properties(PacketTypes.PUBLISH)
properties.MessageExpiryInterval=30 # in seconds
    

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if (msg.topic == mytopic):
        print(msg.topic+" "+str(msg.payload))
        exit(0)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.username_pw_set(parser['broker']['user'], parser['broker']['password'])
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(parser['broker']['ip'], int(parser['broker']['port']), 60)

mytopic = 'topic/test'
mqttc.subscribe(mytopic,2);

testPayload = json.dumps({"username" : "test", "deviceID": "testID", "message": "hello world!"})

mqttc.publish(mytopic, testPayload,2,properties=properties)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()