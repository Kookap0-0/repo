import r2r_dac as r2r
import signal_generator as sg
import time as t
amplitude = 3.1
signal_frequency = 5
sampling_frequency = 1000
if __name__ == "__main__":
    try:
        r2r = r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.165, True)
        epoch = t.asctime(t.gmtime(0))
        while True:
            try:
                voltage = sg.triangle(signal_frequency, t.time(), amplitude)
                r2r.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        r2r.deinit()