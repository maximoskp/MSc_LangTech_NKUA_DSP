#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:10:17 2021

@author: max
"""
#

x = 5
y = 6
z = 1.2
a = [1,2,3]
a = [5,7,9]
a[0]
a[1]
a[2]
b = [1,2, [4,5,6] ]
s = 'My name is Max'
s1 = 'My name is Max'
s2 = "My name is not George"
c = [s1,s2]
s3 = s2.replace(" ", '_')
len(a)
a[0], a[1], a[2]
# a[3]

# %% new block
x1 = [3,4,5]
x2 = [6,7,8]
x3 = x1 + x2 # list concatenation

# %% Numpy library

import numpy as np

x1 = np.array( [1,2,3] )
x2 = np.array( [4,5,6] )
# x2 = np.array( [4,5,6,7] ) # would produce error
x3 = x1 + x2

y1 = [1,2,3]
y2 = [4,5,6,7]
y3 = y1 + y2


# %% 

# python range
r = list( range(10) )
r2 = r*2
# numpy arange
rr = np.arange( 10 )
rr2 = rr*2

# numpy array of time instances
t = np.arange(44100)/44100

# frequency
f = 200

s = np.sin( 2*np.pi*f*t )

# %% 

import matplotlib.pyplot as plt
plt.plot(t, s)

# %%

import sounddevice as sd

sd.play(s , 44100)









