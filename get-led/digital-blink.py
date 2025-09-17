import RPi.GPIO as g 
import time as t 
led = 26
state = 0
period = 1.0
g.setmode(g.BCM)
g.setup(led, g.OUT)
while(True):
    g.output(led,state)
    state = not state
    t.sleep(period)