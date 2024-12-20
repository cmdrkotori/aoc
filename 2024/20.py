#!/usr/bin/python3
import functools
from copy import copy
from collections import defaultdict
from heapq import heappush, heappop
with open('20.txt') as f:
    lines = f.read().strip().split('\n')

acceptable = ['.', 'E']
dirs = {'<':(-1,0), '^':(0,-1),'>':(1,0), 'v':(0,1)}

grid = defaultdict(lambda: '#')
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        grid[x,y] = c
        if c == 'E':
            ex,ey = x,y
        if c == 'S':
            sx,sy = x,y
w = len(lines[0])
h = len(lines)

def dj4():
    moves = []
    visited = {}
    heappush(moves,(0,sx,sy,'>',{}))
    final_score = None
    while moves:
        score,x,y,d,seen = heappop(moves)
        if (x,y,d) in visited and score > visited[x,y,d]:
            continue
        if final_score and score > final_score:
            continue
        seen[x,y] = score
        visited[x,y,d] = score
        if (x,y) == (ex,ey):
            final_score = score
            return final_score,seen
            continue
        def maybemove(d):
            dx,dy = dirs[d]
            if grid[x+dx,y+dy] in acceptable:
                heappush(moves,(score+1,x+dx,y+dy,d,copy(seen)))
        for k in dirs:
            maybemove(k)

minpath, seen = dj4()

def deltalocs(d):
    for dx in range(-d,d+1):
        for dy in range(-d,d+1):
            if abs(dx)+abs(dy) <= d:
                yield dx,dy

def p2(d):
    cheats = 0
    deltas = list(deltalocs(d))
    for x,y in seen:
        for dx,dy in deltas:
            if (x+dx,y+dy) in seen:
                diff = seen[x+dx,y+dy] - seen[x,y] - abs(dx) - abs(dy)
                if diff >= 100:
                    cheats += 1
    return cheats
print(p2(2))
print(p2(20))
