import numpy as np
import pretty_midi
"""
    Sound mapping was inspired by Sonification and Visualization of Neural Data, by Chang, Mindy & Wang, Ge & Berger, Jonathan.

"""

def spike_rates_to_pitch(rate, r_min, r_max, pitch_min = 32, pitch_max = 64):
    
    return

def avgRatePitch(binned_spikes, bin_duration = 0.01, sample_frequency = 5):
    """ To make it somewhat entertaining the spikes will be converted to some musical instrument """
    pm = pretty_midi.PrettyMIDI() # empty pm object -- will store music
    violin = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Violin"))
    
    avg_spike_rate = binned_spikes.mean()
    avg_min, avg_max = np.min(avg_spike_rate),np.max(avg_spike_rate)
    
    time_total = bin_duration * binned_spikes
    time=0.0
    for i in range(0, len(avg_spike_rate), sample_frequency):
        pitch = spike_rates_to_pitch(avg_spike_rate[i], avg_min, avg_max)
        note = pretty_midi.Note(velocity = 100, 
                                pitch=pitch, 
                                start=time, 
                                end= time + time_total)

        violin.notes.append(note)
        time += time_total
        
    pm.instruments.append(violin)
    return pm

def neuronPitch():
    return
    
def eachRatePitch():
    return