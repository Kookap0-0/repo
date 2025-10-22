import RPi.GPIO as g 
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        g.setmode(g.BCM)
        g.setup(self.gpio_bits, g.OUT, initial = 0)
    def deinit(self):
        g.output(self.gpio_bits, 0)
        g.cleanup()
    def set_number(self, number):
        temp = [int(element) for element in bin(number)[2:].zfill(8)]
        for i in range(len(self.gpio_bits)):
            g.output(self.gpio_bits[i], temp[i])
    def set_voltage(self,voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            return
        self.set_number(int(voltage / self.dynamic_range * 255))

if __name__ == "__main__":
    try:
        dac = R2R_DAC([26, 20, 19, 16, 13, 12, 25, 11], 3.165, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()