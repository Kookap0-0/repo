import RPi.GPIO as g 
leds = [24,22,23,27,17,25,12,16]
period = 0.5
g.setmode(g.BCM)
g.setup(leds, g.OUT)
g.output(leds, 0)