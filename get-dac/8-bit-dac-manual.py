import RPi.GPIO as g 
dac_bits = [16,20,21,25,26,17,27,22]
g.setmode(g.BCM)
g.setup(dac_bits, g.OUT)
dynamic_range = 3.165
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