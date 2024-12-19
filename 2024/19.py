#!/usr/bin/python3
import functools
with open('19.txt') as f:
    towels,designs = f.read().strip().split('\n\n')
towels = set(towels.split(', '))
designs = designs.split('\n')
mxlen = max(*[len(t) for t in towels])

@functools.cache
def findme3(design):
    found = 0
    for i in range(1,min(mxlen,len(design)+1)):
        pattern = design[:i]
        if pattern in towels:
            if pattern == design:
                found += 1
            else:
                found += findme3(design[i:])
    return found

s1,s2 = 0,0
for d in designs:
    possible = findme3(d)
    if possible:
        s1 += 1
    s2 += possible
print(s1,s2)
