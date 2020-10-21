# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:19:10 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time


sr = 44100

t = np.arange( sr )/sr

# waveform 1
f1 = 300 # frequency
a1 = 0.5 # amplitude
p1 = 0 # phase
s1 = a1*np.sin( 2*np.pi*f1*t + 2*np.pi*f1*p1 )

# waveform 2
f2 = 450 # frequency
a2 = 0.3 # amplitude
p2 = 0 # phase
s2 = a2*np.sin( 2*np.pi*f2*t + 2*np.pi*f2*p2 )

s3 = s1 + s2

plt.plot( t , s1 )
plt.plot( t , s2 )
plt.plot( t , s3 )
plt.show()

sd.play( s1 , sr )
# time.sleep(1.5)
sd.play( s2 , sr )
# time.sleep(1.5)
sd.play( s3 , sr )
