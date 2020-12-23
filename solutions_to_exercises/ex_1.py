# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:28:27 2020

@author: user
"""

import librosa
import numpy as np
import matplotlib.pyplot as plt

sr = 44100

# %% ============== EXERCISE 1.2 ==============================

# load files
# eh
eh , _ = librosa.load('audio_files/eh.wav', sr)
# oh
oh , _ = librosa.load('audio_files/oh.wav', sr)
# th
th , _ = librosa.load('audio_files/th.wav', sr)
# dd
dd , _ = librosa.load('audio_files/dd.wav', sr)

# plot first 4410 samples from each waveforms (0.1 sec)
plt.subplot(221)
plt.plot( eh[:4410] ); plt.title('ah')
plt.subplot(222)
plt.plot( oh[:4410] ); plt.title('oh')
plt.subplot(223)
plt.plot( th[:4410] ); plt.title('th')
plt.subplot(224)
plt.plot( dd[:4410] ); plt.title('dd')


# %% ============== EXERCISE 1.3 ==============================
# 
# waveforms of 'eh', 'oh', 'dd' appear to be periodic
# waveform of 'th' appears to be aperiodic
# waveform of 'dd' is rough in comparison to 'ed' and 'od'