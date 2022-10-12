#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:10:17 2021

@author: max
"""
# %%
# adding lists python style
x = [1,2,3]
y = [4,5,6]

python_sum = x + y

# numerical sum with numpy
import numpy as np

# constructing a numpy array
# n = np.array([1,2,'lala', 4.5])
n = np.array([1,2,3])
m = np.array([4,5,6])

numpy_sum = n + m

print('block 1')

# %% 

# create plots, graphs, images, etc
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
# y = x**2
y = np.sin(10*x)

plt.plot(x,y, '-x')

# %% 

print('block 3')

b = np.arange(44100)
# last element accessed with b[-1]
t = b/44100

import sounddevice as sd

freq = 200
s = np.sin( 2 * np.pi * freq * t )

plt.plot(t,s, '-x')

sd.play( s , samplerate=44100 )










