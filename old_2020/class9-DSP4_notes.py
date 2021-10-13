import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

sr = 44100
t= np.arange(1*sr)/sr

s1 = 1 - 2*np.random.random( t.size )

'''

s2 = 1 - 2*np.random.random( t.size )

s = s1 + s2

plt.plot( s1+s2 ) # equivalent to: plot(s)
plt.clf()
plt.plot( s1 )
plt.plot( s2 )

sd.play( 0.2*s1 , sr )

f = np.fft.fft( s1[:1024] )

plt.plot(f[:f.size//2])

'''
