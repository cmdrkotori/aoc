#!/usr/bin/pypy3
import math
from collections import defaultdict

with open('01.txt') as f:
    text = f.read().strip().split('\n')

l1 = []
l2 = []
for line in text:
    ll = line.split()
    x,y = int(ll[0]), int(ll[1])
    l1.append(x)
    l2.append(y)
l1.sort()
l2.sort()

d = 0
for x,y in zip(l1,l2):
    d += abs(x-y)
print(d)

d = defaultdict(lambda: 0)
s = 0
for y in l2:
    d[y]+=1
for x in l1:
    s += x*d[x]
print(s)
