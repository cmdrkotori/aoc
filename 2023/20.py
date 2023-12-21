#!/usr/bin/pypy3
from collections import defaultdict
from math import lcm
import copy
lines = open('20.txt').read().strip().split('\n')

inputs = defaultdict(lambda: {})
outputs = {}
state = {}
gates = {}

for l in lines:
    a,b = l.split(' -> ')
    g = a[1:] if a[0] in '%&' else a
    out = b.split(', ')
    gates[g] = a[0]
    outputs[g] = out
    state[g] = 0
    for o in out:
        inputs[o][g] = 0
        if o not in gates:
            gates[o] = 'o'

decider = list(inputs['rx'].keys())[0]
cycle_gates = inputs[decider] if 'rx' in inputs else []
cycles = {k: 0 for k in cycle_gates}

states = {0: 'low', 1: 'high'}
pushes,high,low = 0,0,0
while True: # for _ in range(4):
    pushes += 1
    queue = [('broadcaster', 'button', 0)]
    while len(queue):
        x = queue.pop(0)
        g,src,pulse = x
        #print(f'{src} -{states[pulse]} -> {g}')
        inputs[g][src] = pulse
        if pulse == 1:
            high += 1
        else:
            low += 1
        nq = []
        if gates[g] == 'b':
            nq = [(a,g,pulse) for a in outputs[g]]
            new = pulse
        elif gates[g] == '%':
            if pulse == 0:
                new = 1 if state[g]==0 else 0
                nq = [(a,g,new) for a in outputs[g]]
        elif gates[g] == '&':
            new = 0 if all([b == 1 for b in inputs[g].values()]) else 1
            nq = [(a,g,new) for a in outputs[g]]
            if g == decider and pulse == 1:
                cycles[src] = pushes
                if all(cycles.values()):
                    print(lcm(*cycles.values()))
                    exit(0)
        queue.extend(nq)
        if nq:
            state[g] = new
    if pushes == 1000:
        print(low*high)
    #print('')
