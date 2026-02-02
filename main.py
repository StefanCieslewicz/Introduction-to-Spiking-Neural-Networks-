from sound_mapping import *
from scipy.io import loadmat
import snntorch as snn
import brian2 as br2

data_files = [
    "neurons/m06cat003spk001a.mat",
    "neurons/m06cat003spk001b.mat",
]

all_spikes = []

for f in data_files:
    data = loadmat(f, simplify_cells=True)
    neuron_data = data['neuron']

    all_spikes.append(neuron_data[:200])  

# all_spikes is now a list of arrays (spike times)
print("Number of neurons:", len(all_spikes))

t_start = min(s.min() for s in all_spikes  if len(s) > 0)
t_end   = max(s.max() for s in all_spikes  if len(s) > 0)
