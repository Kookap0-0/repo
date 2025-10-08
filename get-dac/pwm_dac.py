import RPi.GPIO as g
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.pwm_frequency = pwm_frequency
        self.verbose = verbose
        g.setmode(g.BCM)
        g.setup(self.gpio_pin, g.OUT, initial = 0)
        self.pwm = g.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)
        
    def deinit(self):
        self.pwm.stop()
        g.cleanup()

    def set_voltage(self,voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            return
        duty_cycle = (voltage/self.dynamic_range)*100
        self.pwm.ChangeDutyCycle(duty_cycle)
        
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