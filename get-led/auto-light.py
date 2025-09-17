import RPi.GPIO as g 
import time as t 
lightresist = 6
led = 26
g.setmode(g.BCM)
g.setup(lightresist, g.IN)
g.setup(led, g.OUT)
while(True):
    g.output(led, g.input(lightresist))
    t.sleep(0.2)