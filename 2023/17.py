#!/usr/bin/pypy3
import heapq
from collections import defaultdict
lines = open('17.txt').read().strip().split('\n')
grid = defaultdict(lambda: None)
for x,l in enumerate(lines):
    for y,c in enumerate(l):
        grid[y,x] = int(c)
my,mx = y,x

def walk(dy,dx,p2):
    h = []
    h.append((0,0,0,dy,dx,0))
    seen = set()
    mt = 10 if p2 else 3
    while h:
        heat,y,x,dy,dx,t = heapq.heappop(h)
        p = y,x,dx,dy,t
        if p in seen:
            continue
        if (y,x) == (my,mx):
            return heat
        seen.add(p)
        for ndy,ndx in [(-1,0),(1,0),(0,1),(0,-1)]:
            if t == mt and (dy,dx) == (ndy,ndx):
                continue
            if p2 and t<4 and (ndy,ndx)!=(dy,dx):
                continue
            if (ndy,ndx) == (-dy,-dx):
                continue
            ny,nx = y+ndy,x+ndx
            if grid[ny,nx]==None:
                continue
            nheat = heat + grid[ny,nx]
            nt = t + 1 if (ndy,ndx) == (dy,dx) else 1
            heapq.heappush(h,(nheat,ny,nx,ndy,ndx,nt))

print(walk(0,1,False))
print(min(walk(0,1,True),walk(1,0,True)))
