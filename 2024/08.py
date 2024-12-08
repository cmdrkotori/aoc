#!/usr/bin/pypy3
from collections import defaultdict
with open('08.txt') as f:
    lines = f.read().strip().split('\n')
h = len(lines)
w = len(lines[0])
ants = defaultdict(lambda: [])
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c != '.':
            ants[c].append((x,y))

def outside(x,y):
    return x < 0 or x >= w or y < 0 or y >= h

def antinodes(a,b):
    x1,y1 = a
    x2,y2 = b
    dx = x2-x1
    dy = y2-y1
    x3,y3 = x1+dx+dx,y1+dy+dy
    x4,y4 = x2-dx-dx,y2-dy-dy
    pp = []
    if not outside(x3,y3):
        pp.append((x3,y3))
    if not outside(x4,y4):
        pp.append((x4,y4))
    return pp

def antinodes2(a,b):
    x1,y1 = a
    x2,y2 = b
    dx = x2-x1
    dy = y2-y1
    x3,y3 = x1,y1
    x4,y4 = x2,y2
    pp = set()

    b1,b2 = False,False
    while True:
        b1 = outside(x3,y3)
        if not b1:
            pp.add((x3,y3))
        b2 = outside(x4,y4)
        if not b2:
            pp.add((x4,y4))
        if b1 and b2:
            break
        x3 -= dx
        x4 += dx
        y3 -= dy
        y4 += dy
    return pp

def p(f):
    places = set()
    for _,t in ants.items():
        tl = len(t)
        for ta in range(0,tl-1):
            for tb in range(ta+1,tl):
                for n in f(t[ta],t[tb]):
                    places.add(n)
    print(len(places))
p(antinodes)
p(antinodes2)
