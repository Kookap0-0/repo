import RPi.GPIO as g
import time as t
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.pwm_frequency = pwm_frequency
        self.verbose = verbose
        g.setmode(g.BCM)
        g.setup(self.gpio_pin, g.OUT, initial = 0)
        
    def deinit(self):
        g.output(self.gpio_pin, 0)
        g.cleanup()

    def set_voltage(self,voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            return
        temp = int(voltage / self.dynamic_range * 255)
        g.output(self.gpio_pin, 1)
        t.sleep(temp/(255*self.pwm_frequency))
        g.output(self.gpio_pin, 0)
        t.sleep((255-temp)/(255*self.pwm_frequency))
        
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()