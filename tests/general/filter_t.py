import numpy as np
import matplotlib.pyplot as plt

from DataProcessing import DataProcessing

import scipy.signal as sp


f_low = 8
f_high = 30
f_order = 7
fs = 250

dp = DataProcessing()

dp.DesignFilter(f_low,f_high,250,f_order, filt_type ='iir')

din = np.loadtxt('data_cal.txt')
# t = np.arange(1000)
# din = np.sin(2 * np.pi * 25 * t / fs)

ch1 = din.T[2]

# dout = sp.filtfilt(b, a, ch1)

dout = dp.ApplyFilter(ch1)

# print dout
# plt.plot(dout)
# plt.show()

# plt.specgram(ch1, 1024, fs)
# plt.show()

# plt.specgram(dout, 1024, fs)
# plt.show()
