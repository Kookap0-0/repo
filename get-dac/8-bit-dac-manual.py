import RPi.GPIO as g 
import time as t 
dac_bits = [16,12,25,17,27,23,22,24]
g.setmode(g.BCM)
g.setup(dac_bits, g.OUT)
dynamic_range = 3.3
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)
def number_to_dac(number):
    return [int(element) for element in bin(number)[2:].zfill(8)]
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = number_to_dac(voltage_to_number(voltage))
            for i in range(8):
                g.output(dac_bits[i], number[i])

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    g.output(dac_bits, 0)
    g.cleanup()