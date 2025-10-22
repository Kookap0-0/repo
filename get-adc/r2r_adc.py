import RPi.GPIO as g 
import time as t

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        g.setmode(g.BCM)
        g.setup(self.bits_gpio, g.OUT, initial = 0)
        g.setup(self.comp_gpio, g.IN)

    def deinit(self):
        g.output(self.bits_gpio, 0)
        g.cleanup()
    def set_number(self, number):
        temp = [int(element) for element in bin(number)[2:].zfill(8)]
        for i in range(len(self.bits_gpio)):
            g.output(self.bits_gpio[i], temp[i])
    def get_sc_voltage(self):
        return self.dynamic_range/(2**len(self.bits_gpio))


    def sequential_counting_adc(self):
        levels = 2**len(self.bits_gpio)
        for i in range(levels):    
            self.set_number(i)
            t.sleep(0.01)
            comparatorValue = g.input(self.comp_gpio)
            if comparatorValue==1:
                print(i, i*self.get_sc_voltage())
                return
        print(levels, self.dynamic_range)

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.278, 0.01, True)
        
        while True:
            try:
                adc.sequential_counting_adc()

            except KeyboardInterrupt():
                print("Keyboard interruption\n")

    finally:
        adc.deinit()


