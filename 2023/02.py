#!/usr/bin/pypy3
from collections import defaultdict
from math import prod

with open('02.txt') as f:
    lines = f.read().strip().split('\n')

games = []
for l in lines:
    gam = [g.split(', ') for g in l.split(': ')[1].split('; ')]
    gg = []
    for g in gam:
        d = defaultdict(int)
        for i in g:
            k,v = i.split(' ')
            d[k] = int(v)
        gg.append(d)
    games.append(gg)

print(sum([games.index(g)+1 if len([d for d in g if d['red']<=12 and d['green']<=13 and d['blue']<=14])==len(g) else 0 for g in games]))

gpow = []
for g in games:
    dmax = defaultdict(int)
    for d in g:
        for k,v in d.items():
            dmax[k] = dmax[k] if dmax[k]>v else v
    gpow.append(prod(dmax.values()))
print(sum(gpow))
