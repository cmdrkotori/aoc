#!/usr/bin/python3
import functools
import math

## PART 1 ##
with open('11.txt') as f:
    text = f.read().strip()
stones = list(map(int, text.split()))

def roll(stones):
    x = []
    for s in stones:
        if s == 0:
            x.append(1)
        elif len(str(s))%2 == 0:
            ss = str(s)
            ln = len(ss)
            s1,s2 = int(ss[:ln//2]), int(ss[ln//2:])
            x.append(s1)
            x.append(s2)
        else:
            x.append(s*2024)
    return x

xn = []
for i in range(25):
    stones = roll(stones)
print(len(stones))

## PART 2 ##
with open('11.txt') as f:
    text = f.read().strip()
stones = list(map(int, text.split()))

results = dict()
def sumstone(s, x):
    if x == 0:
        return 1
    if (s,x) in results:
        return results[(s,x)]
    if s == 0:
        ss = sumstone(1,x-1)
    elif len(str(s))%2 == 0:
        ss = str(s)
        ln = len(ss)
        s1,s2 = int(ss[:ln//2]), int(ss[ln//2:])
        ss = sumstone(s1,x-1)
        ss += sumstone(s2,x-1)
    else:
        ss = sumstone(s*2024,x-1)
    results[(s,x)] = ss
    return ss

sm = 0
for s in stones:
    sm += sumstone(s,75)
print(sm)
