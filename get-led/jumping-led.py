import RPi.GPIO as g 
import time as t 
leds = [24,22,23,27,17,25,12,16]
period = 0.5
g.setmode(g.BCM)
g.setup(leds, g.OUT)
g.output(leds, 0)
while(True):
    for led in leds:
        g.output(led,1)
        t.sleep(period)
        g.output(led,0)
    for led in reversed(leds):
        g.output(led,1)
        t.sleep(period)
        g.output(led,0)