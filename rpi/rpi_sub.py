import paho.mqtt.client as mqtt
import time
from json import loads

leftGesture = None

def lumos_callback(client, userdata, message):
    # print(str(message.payload, "utf-8"))
    info = loads(str(message.payload, "utf-8"))
    hand = info["hand"]
    print(hand)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("uhnoo/lumos")
    client.message_callback_add("uhnoo/lumos", lumos_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)  