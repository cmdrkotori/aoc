#!/usr/bin/pypy3
bits = open('15.txt').read().strip().split(',')

def hasher(s):
    v = 0
    for c in s:
        v += ord(c)
        v = (v*17)%256
    return v
print(sum([hasher(b) for b in bits]))

def parse(b):
    if b[-1] == '-':
        label = b[:-1]
        data = -1
    else:
        label,data = b.split('=')
        data = int(data)
    return label,data

hm = [[[],[]] for _ in range(256)]

for b in bits:
    label,data = parse(b)
    h = hasher(label)
    if label in hm[h][0]:
        i = hm[h][0].index(label)
        if data == -1:
            hm[h][0].pop(i)
            hm[h][1].pop(i)
        else:
            hm[h][0][i] = label
            hm[h][1][i] = data
    else:
        if data != -1:
            hm[h][0].append(label)
            hm[h][1].append(data)

power = 0
for box in range(len(hm)):
    for slot,lens in enumerate(hm[box][1]):
        power += (box+1)*(slot+1)*lens
print(power)
