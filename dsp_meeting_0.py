# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:28:49 2020

@author: user
"""

import librosa
import matplotlib.pyplot as plt
import numpy as np

y , sr = librosa.load( 'audio_files/ah_2.wav' , 44100 )

# plt.plot( np.arange(y.size) , y )

# select a window size
w_size = 2048

# take a segment number of samples a power of 2
s = y[0:w_size] # beginning of recording: silence (almost)
s = y[20000:(20000 + w_size)] # beginning of recording: silence (almost)
# plt.plot( np.arange(s.size) , s )

# fft
x = np.fft.fft( s )
mag = np.sqrt( x.real**2 + x.imag**2 )
mag = mag[:mag.size//2]
# compute frequency bins
freq_bins = np.linspace(0, sr, w_size, endpoint=False)

# plot power spectrum - keep first halg
plt.plot( freq_bins[:w_size//2] , mag )
