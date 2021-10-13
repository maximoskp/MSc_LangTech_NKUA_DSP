# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:44:37 2020

@author: user
"""

import librosa
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as scw

sr = 44100

# %% ============== EXERCISE 2.1 ==============================

# load files and isolate 0.1 secs (4410 samples, given a 
# 44100 sample rate) in the middle
# eh
eh , _ = librosa.load('audio_files/eh.wav', sr)
eh01 = eh[ eh.size//2 : eh.size//2+4410 ]
# oh
oh , _ = librosa.load('audio_files/oh.wav', sr)
oh01 = oh[ oh.size//2 : oh.size//2+4410 ]
# th
th , _ = librosa.load('audio_files/th.wav', sr)
th01 = th[ th.size//2 : th.size//2+4410 ]
# dd
dd , _ = librosa.load('audio_files/dd.wav', sr)
dd01 = dd[ dd.size//2 : dd.size//2+4410 ]

# plot first 4410 samples from each waveforms (0.1 sec)
plt.subplot(221)
plt.plot( eh01 ); plt.title('eh')
plt.subplot(222)
plt.plot( oh01 ); plt.title('oh')
plt.subplot(223)
plt.plot( th01 ); plt.title('th')
plt.subplot(224)
plt.plot( dd01 ); plt.title('dd')

# %% ============== EXERCISE 2.2 ==============================
# - 'eh' and 'oh' have 13 consintly repeating patterns within 
# the extent of the recording
# - 'dd' has 26 consistenly repeating patterns (even though 
# there appear to be subpattern that actually repeat 13 times)
# - 'th' does not have periodicity
# 
# by analogy, we have 130Hz for 'eh' and 'oh' - but also for 'dd'


# %% ============== EXERCISE 2.3 ==============================
# mix 'oh' with 'eh'
ehoh = eh01 + oh01

plt.subplot(211)
plt.plot(ehoh); plt.title('eh + oh')
# even though less clear, there are still 13 repeating patterns

# mix 'oh' with 'eh'
thoh = th01 + oh01
plt.subplot(212)
plt.plot(thoh); plt.title('th + oh')
# the 'oh' signal became rougher - more similar to 'd', as we can
# can hear from the recording:
# scw.write('audio_files/thoh.wav', sr, thoh)

# %% ============== BONUS ==============================
# %% ----------- 1 -------------------

t = np.arange(sr)/sr

part1 = 0.5*np.sin( 2*np.pi*200*t )
part2 = 0.5*np.sin( 2*np.pi*300*t )

s1 = part1 + part2

# %% ----------- 2 -------------------
# simply change the phase of s2
part2p = 0.5*np.sin( 2*np.pi*300*t + np.pi )

s2 = part1 + part2p

# %% ----------- 3 -------------------

plt.subplot(211)
plt.plot(s1[:4410]); plt.title('s1')
plt.subplot(212)
plt.plot(s2[:4410]); plt.title('s2')

scw.write('audio_files/s1.wav', sr, s1.astype(np.float32))
scw.write('audio_files/s2.wav', sr, s2.astype(np.float32))


# %% ----------- 4 -------------------
s3 = s1 + s2

plt.subplot(311)
plt.plot(s1[:4410]); plt.title('s1')
plt.subplot(312)
plt.plot(s2[:4410]); plt.title('s2')
plt.subplot(313)
plt.plot(s3[:4410]); plt.title('s3')

scw.write('audio_files/s3.wav', sr, s3.astype(np.float32))
