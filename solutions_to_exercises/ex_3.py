# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:56:08 2020

@author: user
"""

import librosa
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as scw

sr = 44100

# %% ============== EXERCISE 3.1 ==============================

# load files
# eh
eh , _ = librosa.load('audio_files/eh.wav', sr)
# oh
oh , _ = librosa.load('audio_files/oh.wav', sr)
# th
th , _ = librosa.load('audio_files/th.wav', sr)
# dd
dd , _ = librosa.load('audio_files/dd.wav', sr)

# define window size
n_fft = 4096
# prepare window
w = np.hanning( n_fft )

# make frequency bins
freq_bins = librosa.fft_frequencies( sr=sr , n_fft=n_fft )[:-1]
# fff = np.linspace(0, sr, n_fft, endpoint=False)

# apply fft
eh_fft = np.fft.fft( w*eh[:n_fft] )
eh_ps = np.sqrt( eh_fft.real[ :n_fft//2 ]**2 + eh_fft.imag[ :n_fft//2 ]**2 )

plt.plot( freq_bins[:n_fft//8] , eh_ps[:n_fft//8] ); plt.title('eh')

# according to ex_2, fundamental frequency should be 130Hz, which is evaluated
# by the first peak in the FFT plot.
# However, the greatest magnitude in the FFT plot is observed as a component
# component of a formant

# %% ============== EXERCISE 3.2 ==============================
t = np.arange(sr)/sr

s1 = np.sin( 2*np.pi*50*t )
s2 = np.sin( 2*np.pi*70*t )

scw.write('audio_files/s1.wav', sr, s1.astype(np.float32))
scw.write('audio_files/s2.wav', sr, s2.astype(np.float32))

# %% ============== EXERCISE 3.3 ==============================
# we observe that 4096 is fine - frequencies 50 and 70 are in different bins
#
# let's check 2048
freq_bins = librosa.fft_frequencies( sr=sr , n_fft=2048 )[:-1]
'''
0
21.5332
43.0664 -> 50 should be in here
64.5996 -> 50 should be in here
86.1328
107.666
'''

# let's check 1024
freq_bins = librosa.fft_frequencies( sr=sr , n_fft=1024 )[:-1]
'''
0
43.0664 -> 50 and 70 are here - not good
86.1328
129.199
'''

# minimum window size: 2048


# %% ============== EXERCISE 3.3 ==============================
# let's check 1024
freq_bins = librosa.fft_frequencies( sr=sr//2 , n_fft=1024 )[:-1]
'''
0
21.5332
43.0664 -> 50 should be here
64.5996 -> 70 should be here
86.1328
107.666
'''
# now 1024 is fine!