import RPi.GPIO as g 
import time as t 
button = 13
led = 26
state = 0
period = 1.0
g.setmode(g.BCM)
g.setup(button, g.IN)
g.setup(led, g.OUT)
while(True):
    if(g.input(button)):
        state = not state
        g.output(led, state)
        t.sleep(0.2)