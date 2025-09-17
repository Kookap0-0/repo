import RPi.GPIO as g 
import time as t 
led = 26
g.setmode(g.BCM)
g.setup(led, g.OUT)
pwm = g.PWM(led,200)
duty=0.0
pwm.start(duty)
while(True):
    pwm.ChangeDutyCycle(duty)
    t.sleep(0.05)
    duty+=1.0
    if(duty>100.0):
        duty=0.0