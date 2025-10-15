import mcp4725_driver
import signal_generator as sg
import time as t

amplitude = 5
signal_frequency = 0.25
sampling_frequency = 100

if __name__ == "__main__":
    try:
        mcp = mcp4725_driver.MCP4725(5.145, 0x61, True)
        epoch = t.asctime(t.gmtime(0))
        while True:
            try:
                voltage = sg.triangle(signal_frequency, t.time(), amplitude)
                mcp.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        mcp.deinit()