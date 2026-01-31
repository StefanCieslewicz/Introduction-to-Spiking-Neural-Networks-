"""from brian2 import *
prefs.codegen.target = "numpy"

start_scope()

defaultclock.dt = 0.1*ms
runtime = 10*ms

eqs = '''
dv/dt = -v / (5*ms) : 1
'''

threshold = 'v > 1'
reset = 'v = 0'

# Variables x2, x3, x4 (true / false)
variables = ['x2', 'x3', 'x4']

var_neurons = NeuronGroup(
    len(variables)*2,
    eqs,
    threshold=threshold,
    reset=reset,
    method='exact'
)

true_idx  = {var: i*2 for i, var in enumerate(variables)}
false_idx = {var: i*2+1 for i, var in enumerate(variables)}

# Clause neuron
clause = NeuronGroup(
    1,
    eqs,
    threshold=threshold,
    reset=reset,
    method='exact'
)

# Synapses with delay
syn = Synapses(
    var_neurons,
    clause,
    on_pre='v_post += 1.2',
    delay=0.2*ms
)

syn.connect(i=[
    false_idx['x2'],
    false_idx['x3'],
    false_idx['x4']
], j=0)

# Initialize
var_neurons.v = 0
clause.v = 0

# Assignment:
# x2 = TRUE, x3 = TRUE, x4 = FALSE
var_neurons.v[true_idx['x2']]  = 1.5
var_neurons.v[true_idx['x3']]  = 1.5
var_neurons.v[false_idx['x4']] = 1.5

# Monitors
M_vars = SpikeMonitor(var_neurons)
M_clause = SpikeMonitor(clause)

run(runtime)

print("Variable spikes:")
for i, t in zip(M_vars.i, M_vars.t):
    print(f"Neuron {i} @ {t}")

print("\nClause spikes:", M_clause.t)

if len(M_clause.t) > 0:
    print("\nClause SATISFIED ✅")
else:
    print("\nClause UNSATISFIED ❌")
"""

import numpy as np
from sound_mapping import *
from scipy.io import loadmat

file_path = "neurons\m06cat003spk001a.mat"
data = loadmat(file_path, simplify_cells=True)
print(data.keys())

spikes = data['neuron'][:5000]
#print(type(spikes), len(spikes))
#print(spikes)


"""
    bru
"""