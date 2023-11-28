import paho.mqtt.client as mqtt
import time
from json import loads
from grovepi import *

ledList = [5, 6]
for led in ledList:
    pinMode(led,"OUTPUT")
    analogWrite(led, 0)


time.sleep(1)

def lumos_callback(client, userdata, message):
    payload = str(message.payload, "utf-8")
    data = list(map(int, payload[1:len(payload)-1].split(", ")))
    print(data)
    try:
        x = data[0]
        y = data[1]
        windowWidth = 1280
        windowHeight = 720
        breakpoints = [0, windowWidth / 2, windowWidth]

        # calculate which LED should be turned on
        whichLED = 0
        if x < breakpoints[1]:
            whichLED = 0       # 5
        elif x < breakpoints[2]:
            whichLED = 1       # 6
        else:
            print("uh oh")      # we got a problem
        yBrightness = (y / windowHeight) * 256
        if yBrightness < 0:
            yBrightness = 0
        print(yBrightness)
        for led in ledList:
            if led != ledList[whichLED]:
                analogWrite(led, 0)
        print(whichLED)
        analogWrite(ledList[whichLED], int(yBrightness))
        time.sleep(0.1)
    except KeyboardInterrupt:
        for led in ledList: # turn off all LEDs before stopping
            analogWrite(led, 0)
        print("interrupt")
    except IOError:
        for led in ledList: # turn off all LEDs before stopping
            analogWrite(led, 0)
        print("error")

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
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
