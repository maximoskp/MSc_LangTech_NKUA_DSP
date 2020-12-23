# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 07:10:43 2020

@author: user
"""

'''
link to speak and spell demo
https://youtu.be/cgNAqh4Mg9Q

'''

import numpy as np
import numpy.matlib
import librosa
import matplotlib.pyplot as plt
import sounddevice as sd
import time

file_names = ['audio_files/ah/ah_0.wav',
              'audio_files/oh/oh_0.wav',
              'audio_files/eeh/eeh_0.wav',
              'audio_files/ah/ah_1.wav',
              'audio_files/oh/oh_1.wav',
              'audio_files/eeh/eeh_1.wav',
              'audio_files/ah/ah_2.wav',
              'audio_files/oh/oh_2.wav',
              'audio_files/eeh/eeh_2.wav']
sythesized = np.zeros(0)
recorded = np.zeros(0)


for i, file_name in enumerate(file_names):
    y, sr = librosa.load(file_name, sr=44100)
    
    pitch = librosa.yin(y, 50, 1000)
    fr = np.mean(pitch)
    
    n_fft = 8096
    hop_size = 256
    
    p = librosa.stft(y, n_fft=n_fft, hop_length=hop_size)
    d = librosa.amplitude_to_db( np.abs(p), ref=np.max )
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    
    m = np.mean( d , axis=1 )
    m -= np.min( m )
    
    def moving_average(x, w):
        x = np.hstack( ( x[0]*np.ones(w//2) , x , x[-1]*np.ones(w//2-1) ) )
        ma = np.convolve(x, np.ones(w), 'valid') / w
        return ma
    
    a = moving_average(m,50)
    a /= np.max( a )
    
    # plt.plot( freqs , m )
    # plt.plot( freqs , a )
    
    # filter
    f = numpy.matlib.repmat( a , p.shape[1], 1 ).T
    # plt.imshow(f, origin='lower', aspect='auto')
    
    # make noise
    # x = np.random.rand( y.size )
    # xp = librosa.stft(x, n_fft=n_fft, hop_length=hop_size)
    # make saw
    n = np.arange( y.size )
    # fr = frs[i]
    x = (n%(sr/fr))/(sr/fr)
    xp = librosa.stft(x, n_fft=n_fft, hop_length=hop_size)
    
    px = xp*f
    x1 = librosa.istft(px, hop_length=hop_size)
    
    dpx = librosa.amplitude_to_db( np.abs(px), ref=np.max )
    # plt.imshow(dpx, origin='lower', aspect='auto')
    
    sythesized = np.hstack( (sythesized,x1) )
    recorded = np.hstack( (recorded,y) )

sd.play( recorded, sr )
time.sleep( recorded.size/sr + 0.5 )
sd.play( sythesized , sr )