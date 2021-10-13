# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:28:30 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

sr = 44100

f1 = 10
f2 = 7

t = np.arange(sr)/sr

s1 = np.sin( 2*np.pi*f1*t )

s2 = np.sin( 2*np.pi*f1*t + np.pi )

s3 = np.sin( 2*np.pi*f2*t + np.pi )

plt.subplot(311)
plt.plot( np.arange( t.size ) , s1+s3 )
plt.subplot(312)
plt.plot( np.arange( t.size ) , s2 )
plt.subplot(313)
plt.plot( np.arange( t.size ) , s1+s3 + s2 )
axes = plt.gca()
axes.set_ylim([-1,1])