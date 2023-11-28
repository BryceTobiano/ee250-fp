import time
from grovepi import *

led = 5
pinMode(led,"OUTPUT")
global i
analogWrite(led,0)


if __name__ == '__main__':
    while True: 
        i = i + 20
        if i > 255:
            i = 0
        analogWrite(led,i)
        time.sleep(100)
         
