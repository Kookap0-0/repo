import RPi.GPIO as g 
import time as t 
leds = [16,12,25,17,27,23,22,24]
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
    return [int(element) for element in bin(n)[2:].zfill(8)]
def r1(leds, bin):
    temp = []
    for i in range(len(bin)):
        if bin[i]==1:
            temp.append(leds[i])
    return temp
def r2(leds, bin):
    temp = []
    for i in range(len(bin)):
        if bin[i]==0:
            temp.append(leds[i])
    return temp    
while(True):
    upx = g.input(up)
    downx = g.input(down)
    if(upx!=0 and downx!=0):
        g.output(leds, 1)
        t.sleep(sleep_time)
    else:    
        if(upx):
            if(num==7):
                num=0
            else:
                num+=1
            print(num, f(num))
            g.output(r1(leds,f(num)), 1)
            g.output(r2(leds,f(num)), 0)
            t.sleep(sleep_time)
        if(downx):
            if(num>0):
                num-=1
            else:
                num=0
            print(num, f(num))
            g.output(r1(leds,f(num)), 1)
            g.output(r2(leds,f(num)), 0)
            t.sleep(sleep_time)
        upx = 0
        downx = 0 