#!/usr/bin/python3
import re
from heapq import heappush, heappop
with open('18.txt') as f:
    lines = f.read().strip().split('\n')
blocks = [tuple(map(int,re.findall(r'\d+', l))) for l in lines]
sx,sy = 0,0
ex,ey = 70,70
nblocks = 1024
laid = set()

def outside(x,y):
    return x<0 or x>ex or y<0 or y>ey

def bfs():
    queue = [(0, sx, sy)]
    visited = set()
    while queue:
        ln,x,y = heappop(queue)
        if (x,y) == (ex,ey):
            return ln
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx,ny = x+dx,y+dy
            if outside(nx,ny):
                continue
            if (nx,ny) not in laid and (nx,ny) not in visited:
                visited.add((nx,ny))
                heappush(queue, (ln+1, nx, ny))

for n in range(nblocks):
    laid.add(blocks[n])
print(bfs())

def p2():
    for n in range(nblocks,len(blocks)):
        laid.add(blocks[n])
        if not bfs():
            print(','.join(map(str,blocks[n])))
            return
p2()
