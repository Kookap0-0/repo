import time as t
import r2r_adc as r2r
import adc_plot

adc = r2r.R2R_ADC(3.278, 0.01, True)
voltage_values = []
time_values = []
duration = 10.0

try:
    start_time = t.time()
    current_time = t.time()
    while(current_time-start_time<duration):
        try:
            voltage_values.append(adc.get_volatge())
            current_time = t.time()
            time_values.append(current_time-start_time)

        except KeyboardInterrupt():
            print("Keyboard interruption\n")

finally:
    adc.deinit()

adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range, duration)