#!/usr/bin/pypy3
from collections import defaultdict
import copy
lines = open('22.txt').read().strip().split('\n')
bricks = []

for l in lines:
    x1,y1,z1,x2,y2,z2 = map(int,l.replace('~',',').split(','))
    dx,dy,dz = x2-x1, y2-y1, z2-z1
    if (dx,dy,dz) != (0,0,0):
        d = abs(max(dx,dy,dz))
        dx /= d
        dy /= d
        dz /= d
    x,y,z = copy.deepcopy((x1,y1,z1))
    cubes = []
    while True:
        cubes.append((x,y,z))
        if (x,y,z) == (x2,y2,z2):
            break
        x += dx
        y += dy
        z += dz
    bricks.append(cubes)
bricks = sorted(bricks, key = lambda b: min(c[2] for c in b))

def dropme(bricks):
    seen=set()
    fallen = list()
    num_moved = 0
    for b in bricks:
        moved = False
        while True:
            down = [(x,y,z-1) for x,y,z in b]
            still = any(z<=0 or (x,y,z) in seen for x,y,z in down)
            if still:
                for x,y,z in b:
                    seen.add((x,y,z))
                fallen.append(b)
                break
            b = down
            moved = True
        if moved:
            num_moved += 1
    return fallen, num_moved

fallen, num = dropme(bricks)
p1,p2 = 0,0
for i in range(len(bricks)):
    structure = copy.copy(fallen)
    structure.pop(i)
    _, num = dropme(structure)
    if num == 0:
        p1 += 1
    p2 += num
print(p1,p2)
