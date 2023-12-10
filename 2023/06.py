#!/usr/bin/pypy3
from math import floor,ceil,prod
# 1084752
# 28228952
lines = open('06.txt').read().strip().split('\n')
time = [int(x) for x in lines[0].split()[1:]]
dist = [int(x) for x in lines[1].split()[1:]]

def race(t,d):
    #-h^2 + t*h - d > 0
    q = ((t**2 - 4*(d+1))**0.5)/2
    p = t/2
    return 1 + floor(p+q) - ceil(p-q)

print(prod([race(t,d) for t,d in zip(time,dist)]))
time = int(''.join([str(t) for t in time]))
dist = int(''.join([str(d) for d in dist]))
print(race(time,dist))
