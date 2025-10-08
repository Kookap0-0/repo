import pwm_dac
import signal_generator as sg
import time as t

amplitude = 2.1
signal_frequency = 20
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = pwm_dac.PWM_DAC(12, 500, 3.290, True)
        epoch = t.asctime(t.gmtime(0))
        while True:
            try:
                voltage = 0.5*amplitude*sg.get_sin_wave_amplitude(signal_frequency, t.time())
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()