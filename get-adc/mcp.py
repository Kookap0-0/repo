import time as t
import mcp3021_driver as mcp_driver
import adc_plot

adc = mcp_driver.MCP3021(3.283, False)
voltage_values = []
time_values = []
duration = 5.0

try:
    start_time = t.time()
    current_time = t.time()
    while(current_time-start_time<duration):
        try:
            # voltage_values.append(adc.get_sc_voltage())
            voltage_values.append(adc.get_voltage())
            current_time = t.time()
            time_values.append(current_time-start_time)

        except KeyboardInterrupt():
            print("Keyboard interruption\n")

finally:
    adc.deinit()

adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range, duration)
# adc_plot.plot_sampling_period_hist(time_values)