import numpy as np
import time as t
def get_sin_wave_amplitude(freq,time):
    return 1+np.sin(2*np.pi*freq*time)
def wait_for_sampling_period(sampling_frequency):
    t.sleep(1/sampling_frequency)
def triangle(freq, time,amp):
    quater_period = 1/(4*freq)
    t = (time/quater_period - int(time/quater_period))%4
    if (t<=1):
        return amp*(1-t)
    elif(t>1 and t<=2):
        return amp*(t-1)
    elif(t>2 and t<=3):
        return amp*(3-t)
    else:
        return amp*(t-3)
    