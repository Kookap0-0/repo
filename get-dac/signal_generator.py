import numpy as np
import time as t
def get_sin_wave_amplitude(freq,time):
    return 1+np.sin(2*np.pi*freq*time)
def wait_for_sampling_period(sampling_frequency):
    t.sleep(1/sampling_frequency)
def triangle(freq, time,amp):
    period = 1.0/freq
    new_time = (time%period)/period
    if (t<0.5):
        return 2*amp*new_time
    else:
        return 2*amp*(1-new_time)