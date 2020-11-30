# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:24:15 2020

@author: user
"""

# %%
from conch.analysis.formants import FormantTrackFunction
from conch.analysis.pitch import PitchTrackFunction
import librosa
import numpy as np

def get_pitch_and_formants(f):
    func = PitchTrackFunction(time_step=0.01, min_pitch=75, max_pitch=600)
    pitch = func(f)
    func = FormantTrackFunction(time_step=0.01,
                                window_length=0.025, num_formants=5, max_frequency=5500)
    formants = func(f)
    # sync
    kp = np.array( list( pitch.keys() ) )
    kf = np.array( list( formants.keys() ) )
    
    synced = {}
    for t in kp:
        # find nearest value in formants
        idx = (np.abs( kf - t )).argmin()
        formants_freqs_list = []
        formants_ratios_list = []
        formants_amps_list = []
        current_pitch = pitch[ t ]
        if current_pitch[0] != 0:
            for fmnt in formants[ kf[ idx ] ]:
                if current_pitch[0] is not None and fmnt[0] is not None:
                    formants_freqs_list.append( fmnt[0] )
                    formants_amps_list.append( fmnt[1] )
                    formants_ratios_list.append( fmnt[0]/current_pitch[0] )
            synced[ t ] = {
                'pitch': pitch[ t ],
                'time': t,
                'formants_freqs': formants_freqs_list,
                'formants_amps': formants_amps_list,
                'formants_ratios': formants_ratios_list,
            }
    
    return synced, pitch, formants, kp, kf
# end get_pitch_and_formants

# %%

# run for audio files
ah_pitch_formants = []
oh_pitch_formants = []
eeh_pitch_formants = []
gt_pitch_formants = []
for i in range(4):
    sa, _, _, _, _ = get_pitch_and_formants( 'audio_files/ah/ah_' + str(i) + '.wav' )
    ah_pitch_formants.append( sa )
    so, _, _, _, _ = get_pitch_and_formants( 'audio_files/oh/oh_' + str(i) + '.wav' )
    oh_pitch_formants.append( so )
    see, _, _, _, _ = get_pitch_and_formants( 'audio_files/eeh/eeh_' + str(i) + '.wav' )
    eeh_pitch_formants.append( see )
    gt, _, _, _, _ = get_pitch_and_formants( 'audio_files/gt/gt_' + str(i) + '.wav' )
    gt_pitch_formants.append( gt )

# %%

import librosa.display
import matplotlib.pyplot as plt

def compount_pitch_formants_plot(file_name, pitch_formants, plt_alias, idx):
    y, sr = librosa.load(file_name, sr=44100)
    n_fft = 8096
    hop_size = 256
    p = librosa.stft(y, n_fft=n_fft, hop_length=hop_size)
    d = librosa.amplitude_to_db( np.abs(p), ref=np.max )
    librosa.display.specshow(d, cmap='gray_r', sr=sr, hop_length=hop_size, x_axis='time', y_axis='linear', ax=plt_alias)
    # and also, if we restrict to speech-relevant frequencies
    lowest_freq = 30
    highest_freq = 5000
    # plt_alias.ylim([lowest_freq, highest_freq])
    plt_alias.set_ylim([lowest_freq, highest_freq])

    # append pitch
    p = []
    t = []
    fmnts = []
    for k in list( pitch_formants.keys() ):
        a = pitch_formants[k]
        p.append( a['pitch'] )
        t.append( a['time'] )
        fmnts.append( a['formants_freqs'] )

    p = np.array( p )
    t = np.array( t )
    plt_alias.plot( t , p , 'r.' )
    for i in range( t.size ):
        for j in range( len(fmnts[i]) ):
            plt_alias.plot( t[i] , fmnts[i][j] , 'b.' )

# %% 

fig,a =  plt.subplots(2,2)

for i in range( 4 ):
    file_name = 'audio_files/ah/ah_' + str(i) + '.wav'
    pitch_formants = ah_pitch_formants[i]
    compount_pitch_formants_plot(file_name, pitch_formants, a[i//2][i%2], i)

fig.savefig('figs/ahs.png', dpi=500)

fig,a =  plt.subplots(2,2)

for i in range( 4 ):
    file_name = 'audio_files/oh/oh_' + str(i) + '.wav'
    pitch_formants = oh_pitch_formants[i]
    compount_pitch_formants_plot(file_name, pitch_formants, a[i//2][i%2], i)

fig.savefig('figs/ohs.png', dpi=500)

fig,a =  plt.subplots(2,2)

for i in range( 4 ):
    file_name = 'audio_files/eeh/eeh_' + str(i) + '.wav'
    pitch_formants = eeh_pitch_formants[i]
    compount_pitch_formants_plot(file_name, pitch_formants, a[i//2][i%2], i)

fig.savefig('figs/eehs.png', dpi=500)

fig,a =  plt.subplots(2,2)

for i in range( 4 ):
    file_name = 'audio_files/gt/gt_' + str(i) + '.wav'
    pitch_formants = gt_pitch_formants[i]
    compount_pitch_formants_plot(file_name, pitch_formants, a[i//2][i%2], i)

fig.savefig('figs/gt.png', dpi=500)

# %%

def isolate_5_formant_stats(s):
    fmnts = np.zeros( ( len(s) , 5 ) )
    nnz = 0
    for i , k in enumerate( list( s.keys() ) ):
        a = s[k]
        tmp_arr = np.array(a['formants_freqs'])
        if tmp_arr.size == 5 and 0 not in tmp_arr:
            fmnts[i, :] = tmp_arr
            nnz += 1
    ret_fmnts = np.zeros( ( nnz , 5 ) )
    nnz = 0
    for i in range( fmnts.shape[0] ):
        if np.sum( fmnts[i,:] ) > 0:
            ret_fmnts[nnz, :] = fmnts[i,:]
            nnz += 1
    return ret_fmnts

# %%

ah_stacked = isolate_5_formant_stats( ah_pitch_formants[0] )
for i in range( 1, 4, 1 ):
    ah_stacked = np.vstack( ( ah_stacked , isolate_5_formant_stats( ah_pitch_formants[i] ) ) )

oh_stacked = isolate_5_formant_stats( oh_pitch_formants[0] )
for i in range( 1, 4, 1 ):
    oh_stacked = np.vstack( ( oh_stacked , isolate_5_formant_stats( oh_pitch_formants[i] ) ) )

_ = plt.boxplot( oh_stacked )
plt.savefig('figs/oh_boxplot.png', dpi=500)

eeh_stacked = isolate_5_formant_stats( eeh_pitch_formants[0] )
for i in range( 1, 4, 1 ):
    eeh_stacked = np.vstack( ( eeh_stacked , isolate_5_formant_stats( eeh_pitch_formants[i] ) ) )

_ = plt.boxplot( eeh_stacked )
plt.savefig('figs/eeh_boxplot.png', dpi=500)

# %%

# combined plot
idx = np.min( np.array( [ah_stacked.shape[0] , oh_stacked.shape[0] , eeh_stacked.shape[0] ] ) )
comp = np.hstack( ( ah_stacked[:idx,:] , oh_stacked[:idx,:] , eeh_stacked[:idx,:] ) )

_ = plt.boxplot( comp )
plt.savefig('figs/comp_boxplot.png', dpi=500)

# %%

letters = [ 'a' , 'o' , 'i' ]
colors = [ 'r' , 'g' , 'b' ]
compv = np.vstack( ( ah_stacked[:idx,:] , oh_stacked[:idx,:] , eeh_stacked[:idx,:] ) )
idxs = np.hstack( ( 0*np.ones( idx ) , 1*np.ones( idx ) , 2*np.ones( idx ) ) ).astype(int)

fig,a =  plt.subplots()

for i in range( compv.shape[0] ):
    a.plot( compv[i,0] , compv[i,1] , '.', color=colors[idxs[i]] )
    a.annotate( letters[ idxs[i] ] , (compv[i,0] , compv[i,1]) , color = colors[ idxs[i] ] )

fig.show()
fig.savefig( 'figs/comp_2d.png' , dpi=500 )

# %%

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(compv)
transformed = pca.transform(compv)

for i in range( compv.shape[0] ):
    a.plot( transformed[i,0] , transformed[i,1] , '.', color=colors[idxs[i]] )
    a.annotate( letters[ idxs[i] ] , (transformed[i,0] , transformed[i,1]) , color = colors[ idxs[i] ] )

fig.show()
fig.savefig( 'figs/comp_PCA.png' , dpi=500 )