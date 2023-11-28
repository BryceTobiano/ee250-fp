import time
from grovepi import *

led = 5
pinMode(led,"OUTPUT")
analogWrite(led,0)

if __name__ == '__main__':
    i = 0
    while True: 
        i = i + 50
        if i > 255:
            i = 0
        analogWrite(led,i)
        print("Current Brightness: " + i)
        time.sleep(100)
         
