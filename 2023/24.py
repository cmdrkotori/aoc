#!/usr/bin/python3
from itertools import combinations
from math import isclose
import z3
lines = open('24.txt').read().strip().split('\n')
stones = [tuple(map(int, l.replace(' @ ', ', ').split(', '))) for l in lines]
num = len(stones)

collide = 0
r1,r2 = (7,2) if len(stones)<10 else (200000000000000,400000000000000)
for a,b in combinations(stones,2):
    x1,y1,z1,dx1,dy1,dz1 = a
    x2,y2,z2,dx2,dy2,dz2 = b

    m1,m2 = dy1/dx1, dy2/dx2
    if isclose(m1,m2):
        continue
    c1,c2 = y1-m1*x1, y2-m2*x2

    x = (c2 - c1) / (m1 - m2)
    y = m2*x + c2

    ddx1,ddy1 = x - x1, y - y1
    ddx2,ddy2 = x - x2, y - y2
    if ((ddx1 > 0) != (dx1 > 0)) or ((ddy1 > 0) != (dy1 > 0)):
        continue
    if ((ddx2 > 0) != (dx2 > 0)) or ((ddy2 > 0) != (dy2 > 0)):
        continue
    if x < r1 or x > r2 or y < r1 or y > r2:
        continue
    collide += 1
print(collide)

px,py,pz,dpx,dpy,dpz = [z3.Real(c) for c in 'x y z dx dy dz'.split(' ')]
s = z3.Solver()
for i in range(3):
    t = z3.Real(f't{i}')
    x,y,z,dx,dy,dz = stones[i]
    s.add(px + dpx*t == x + dx*t)
    s.add(py + dpy*t == y + dy*t)
    s.add(pz + dpz*t == z + dz*t)
s.check()
m = s.model()
print(sum(int(str(m.evaluate(c))) for c in [px,py,pz]))
