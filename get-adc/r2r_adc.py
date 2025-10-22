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
        levels = 2**len(self.bits_gpio)
        return self.sequential_counting_adc()* self.dynamic_range/levels


    def sequential_counting_adc(self):
        levels = 2**len(self.bits_gpio)
        for i in range(levels):    
            self.set_number(i)
            t.sleep(self.compare_time)
            comparatorValue = g.input(self.comp_gpio)
            if comparatorValue==1:
                print(i, i/levels *self.dynamic_range)
                return i
        print(levels, self.dynamic_range)
        return levels
        

    def successive_approximation_adc(self):
        levels = 2**len(self.bits_gpio)
        low = 0
        high = 256
        while low<=high:
            mid = (low+high)//2
            self.set_number(mid)
            t.sleep(self.compare_time)
            comparatorValue = g.input(self.comp_gpio)
            if comparatorValue==0:
                low = mid+1
            else:
                high = mid-1

        print(mid, mid*self.dynamic_range/levels)
        return mid

    def get_sar_voltage(self):
        levels = 2**len(self.bits_gpio)
        return self.successive_approximation_adc()* self.dynamic_range/levels


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.278, 0.01, True)

        
        while True:
            try:
                #adc.sequential_counting_adc()
                adc.successive_approximation_adc()

            except KeyboardInterrupt():
                print("Keyboard interruption\n")

    finally:
        adc.deinit()


