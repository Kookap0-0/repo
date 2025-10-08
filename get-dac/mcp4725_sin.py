import mcp4725_driver
import signal_generator as sg
import time as t

amplitude = 3.1
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        mcp = mcp4725_driver.MCP4725(5.145, 0x61, True)
        epoch = t.asctime(t.gmtime(0))
        while True:
            try:
                voltage = 0.5*amplitude*sg.get_sin_wave_amplitude(signal_frequency, t.time())
                mcp.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        mcp.deinit()