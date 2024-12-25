#!/usr/bin/python3
from collections import defaultdict
with open('24.txt') as f:
    inputs,ops = f.read().strip().split('\n\n')

levels = {}
for i in inputs.split('\n'):
    a,b = i.split(': ')
    levels[a] = True if b=='1' else False

def op_xor(a,b):
    return a^b
def op_or(a,b):
    return a or b
def op_and(a,b):
    return a and b

eqs = []
eqsbypin = defaultdict(lambda: None)
for o in ops.split('\n'):
    a,b,c,_,d = o.split(' ')
    match b:
        case 'AND':
            op = op_and
        case 'OR':
            op = op_or
        case 'XOR':
            op = op_xor
    eqs.append((a,op,c,d))
    if d not in levels:
        levels[d] = None
    if a not in levels:
        levels[a] = None
    if c not in levels:
        levels[c] = None
    eqsbypin[a,b,c] = d
    eqsbypin[c,b,a] = d

def run():
    while any([l==None for _,l in levels.items()]):
        for a,op,c,d in eqs:
            if levels[a] is not None and levels[c] is not None:
                levels[d] = op(levels[a],levels[c])

def num(what):
    z = 0
    for gate,level in sorted(list(levels.items())):
        if gate[0]==what and level:
                z += pow(2,int(gate[1:]))
    return z

run()
print(num('z'))
c0 = None
keys = []
for i in range(45):
    swapped = None
    xpin = f'x{i:02}'
    ypin = f'y{i:02}'

    xor1 = eqsbypin[xpin,'XOR',ypin]
    and1 = eqsbypin[xpin,'AND',ypin]

    # first bit is a half adder and has no carry bit, the rest are
    # full adders with a carry bit so only check the extra gates if
    # there's a carry bit
    if c0:
        and2 = eqsbypin[xor1,'AND',c0]
        if not and2:
            #print(f'Not found xor1:{xor1} AND c0:{c0} in bit {i}, assuming error in earlier gates')
            and1,xor1 = xor1,and1
            swapped = (and1,xor1)
            and2 = eqsbypin[xor1,'AND',c0]

        xor2 = eqsbypin[xor1,'XOR',c0]
        if xor1 and xor1[0] == 'z':
            #print(f'Found xor1:{xor1} swapping with xor2:{xor2} in bit {i}')
            xor1,xor2 = xor2,xor1
            swapped = (xor1,xor2)

        if and1 and and1[0] == 'z': #n1
            #print(f'Found and1:{and1} swapping with xor2:{xor2} in bit {i}')
            and1,xor2 = xor2,and1
            swapped = (and1,xor2)

        if and2 and and2[0] == 'z': #r1
            #print(f'Found and2:{and2} swapping with xor2:{xor2} in bit {i}')
            and2,xor2 = xor2,and2
            swapped = (and2,xor2)

        or1 = eqsbypin[and1,'OR',and2]
        if or1 and or1[0] == 'z' and or1 != 'z45':
            #print(f'Found or1:{or1} swapping with xor2:{xor2} in bit {i}')
            or1,xor2 = xor2,or1
            swapped = (or1,xor2)
    else:
        if and1 and and1[0] == 'z':
            #print(f'Found and1:{and1} swapping with xor1:{xor1} in bit {i}')
            xor1,and1 = and1,xor1
            swapped = (xor1,and1)

    if swapped:
        keys.extend(swapped)
    c0 = and1 if not c0 else or1
print(','.join(sorted(keys)))
