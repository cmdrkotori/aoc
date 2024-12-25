#!/usr/bin/python3
from collections import defaultdict
with open('25.txt') as f:
    schematics = f.read().strip().split('\n\n')

locks,keys = [],[]

for s in schematics:
    ss = s.split('\n')
    highs = []
    for x in range(len(ss[0])):
        count = 0
        for y in range(len(ss)):
            if ss[y][x] == '#':
                count += 1
        highs.append(count-1)
    if all(c=='#' for c in ss[0]):
        locks.append(highs)
    else:
        keys.append(highs)

def checkkey(key):
    count = 0
    for l in locks:
        if all([key[x]+l[x] <= 5 for x in range(5)]):
            count += 1
    return count

count = 0
for k in keys:
    count += checkkey(k)

print(count)
