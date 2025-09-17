import RPi.GPIO as g 
import time as t 
leds = [24,22,23,27,17,25,12,16]
sleep_time = 0.2
up = 9
down = 10
num = 0
g.setmode(g.BCM)
g.setup(leds, g.OUT)
g.setup(up, g.IN)
g.setup(down, g.IN)
g.output(leds, 0)
def f(n):
    return [int(element) for element in bin(n)][2:].zfill(8)]
while(True):
    if(g.input(up)):
        if(num==6):
            num=0
        else:
            num+=1
        print(num, f(num))
        t.sleep(sleep_time)
    if(g.input(down)):
        if(num>0):
            num-=1
        else:
            num=0
        print(num, f(num))
        t.sleep(sleep_time)