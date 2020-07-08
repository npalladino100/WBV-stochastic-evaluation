import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import sounddevice as sd
import wavio

Duration = 3600.0       # seconds
IncreasingTime = 300.0  # seconds
Amplitude = 2000
mean = 0.0    # mean amplitude
std = 0.236576433    # standard deviation

# Filter requirements
order = 4
fs = 1000.0       # sample rate, Hz
cutoff = 60.0  # cutoff frequency of the filter, Hz


def butter_lowpass(cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=4):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Get the filter coefficients
b, a = butter_lowpass(cutoff, fs, order)

# Function parameters
Time = Duration - IncreasingTime        # seconds
Gain = Amplitude


# Function
n = int(Time * fs)  # total number of samples
t = np.arange(0, Time, 1/fs)
data = np.random.normal(mean, std, size=n)

# Filter the data
y = butter_lowpass_filter(data, cutoff, fs, order)
y = Gain*y

# Increasing Function
Time2 = IncreasingTime  # in seconds
n2 = int(Time2 * fs)  # total number of samples
t2 = np.arange(0, Time2, 1/fs)
data2 = np.random.normal(mean, std, size=n2)

# Filter the data
y2 = butter_lowpass_filter(data2, cutoff, fs, order)
y2 = Gain*t2*y2/Time2

wav_const = np.array(y, dtype=np.int16)
wav_inc = np.array(y2, dtype=np.int16)

wavio.write("wav_const.wav", wav_const, fs, sampwidth=2)
wavio.write("wav_inc.wav", wav_inc, fs, sampwidth=2)
