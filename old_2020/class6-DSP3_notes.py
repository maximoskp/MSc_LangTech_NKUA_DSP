# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:45:11 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa


'''
fs = 44100
t = np.arange(8096)/fs
freq = 50
x = np.sin( 2*np.pi*freq*t )

w = np.hanning( 8096 )

y = np.fft.fft( x )

frequency_bins = np.arange( y.size )/y.size*fs

plt.plot( np.arange(8096) , w )
plt.plot( np.arange(8096) , x )
plt.plot( np.arange(8096) , w*x )
'''


'''
plt.subplot(311)
plt.plot( frequency_bins , y.real )
plt.subplot(312)
plt.plot( frequency_bins , y.imag )
mag = np.sqrt( np.power( y.real , 2 ) + np.power( y.imag , 2 ) )
plt.subplot(313)
plt.plot( frequency_bins , mag )
'''

'''
fs = 44100
x, sr = librosa.load('audio_files/sofianos/eipa.wav', sr=fs)

sd.play( x[:4410], sr )
plt.plot( np.arange(4410), x[:4410] )
'''