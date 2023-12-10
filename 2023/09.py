#!/usr/bin/pypy3
from math import lcm
lines = open('09.txt').read().strip().split('\n')
data = [list(map(int,l.split())) for l in lines]

def find_next(arr):
    l = len(arr)
    diff = [b-a for a,b in list(zip(arr[0:l-1],arr[1:]))]
    if not any(diff):
        return arr[-1]
    n = find_next(diff)
    return arr[-1]+n

print(sum([find_next(d) for d in data]))
print(sum([find_next(d[::-1]) for d in data]))
