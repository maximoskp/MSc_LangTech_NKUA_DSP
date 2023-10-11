#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:03:42 2022

@author: max
"""

from conch.analysis.formants import FormantTrackFunction
from conch.analysis.pitch import PitchTrackFunction
import librosa
import numpy as np

# %% 

# define a function for extracting the desired features and for storing them in proper structures for further processing

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
    sa, _, _, _, _ = get_pitch_and_formants( '../audio_files/ah/ah_' + str(i) + '.wav' )
    ah_pitch_formants.append( sa )
    so, _, _, _, _ = get_pitch_and_formants( '../audio_files/oh/oh_' + str(i) + '.wav' )
    oh_pitch_formants.append( so )
    see, _, _, _, _ = get_pitch_and_formants( '../audio_files/eeh/eeh_' + str(i) + '.wav' )
    eeh_pitch_formants.append( see )
    gt, _, _, _, _ = get_pitch_and_formants( '../audio_files/gt/gt_' + str(i) + '.wav' )
    gt_pitch_formants.append( gt )

