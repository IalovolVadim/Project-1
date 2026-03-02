import numpy as np
import time 
def get_sin_wave_amplitude(freq, time):
    argument = 2 * np.pi * freq * time 
    value = (np.sin(argument)+1)/2
    return value
def wait_for_sampling_period(sampling_frequency):
    time.sleep (1.0/sampling_frequency)


