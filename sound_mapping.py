import numpy as np
import pretty_midi
"""
    Sound mapping was inspired by Sonification and Visualization of Neural Data, by Chang, Mindy & Wang, Ge & Berger, Jonathan.
    this is essentially this written in python 
        Out of the large space of possible data to sound mappings, three
        were implemented for the current system, termed avgRatePitch,
        neuronPitch, and eachRatePitch. 
        The avgRatePitch mapping pro-
        vides the most basic summary of average population activity,
        where a range of spike rates is mapped to a range of pitches such
        that higher spike rates correspond to higher pitches. The average
        ﬁring rate across all neurons is sampled every speciﬁed number of
        samples, and the corresponding note is played, creating a steady
        stream of single notes. This mapping can be used both for single
        trials and condition averaged trials. 
        For the neuronPitch mapping,
        which applies to single trials, each neuron is assigned a unique
        pitch, and a note is played at that pitch each time the neuron spikes.
        If speciﬁed, the neurons can be split into two sets, each set with its
        own instrument. 
        The eachRatePitch mapping focuses on the av-
        erage spike rate of each neuron over time. Neurons are grouped
        into 2-4 groups, and each group is assigned an instrument. After a
        speciﬁed number of samples, every ﬁfth neuron within each group
        is selected, and a pitch corresponding to its spike rate is played,
        again with higher spike rates corresponding to higher pitches. The
        neurons within each group are continuously cycled at every sam-
        pled time interval.
    
"""

def bin_spikes(spike_timings, t_start, t_end, bin_size = 100):
    bins = np.arange(t_start, t_end+bin_size, bin_size) # map out bins
    spikes = np.zeros((len(spike_timings), len(bins)-1))
    
    for i, spike in enumerate(spike_timings):
        spikes[i] = np.histogram(spike, bin_size)
    return spikes

def spike_rates_to_pitch(rate, r_min, r_max):
    rate = np.clip(rate, r_min, r_max)
    min_max_normalization = (rate - r_min) / (r_max - r_min) + 1e-9 # normalization; add 1e-9 to avoid zero_div 
    
    return int(48 + min_max_normalization * 32) #

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


### Following functions are kinda optional, I will make them if there is enough time

def neuronPitch():
    return
    
def eachRatePitch():
    return