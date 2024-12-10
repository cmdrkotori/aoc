#!/usr/bin/pypy3
from collections import defaultdict
with open('10.txt') as f:
    lines = f.read().strip().split('\n')
grid = defaultdict(lambda: -1)
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        grid[x,y] = int(c)
w = len(lines[0])
h = len(lines)
trailheads = set()
ratings = defaultdict(lambda: 0)

def outside(x,y):
    return x < 0 or x >= w or y < 0 or y >= h

def findpath(sx,sy,x,y):
    if outside(x,y):
        return
    c = grid[x,y]
    if c == 9:
        trailheads.add((sx,sy,x,y))
        ratings[sx,sy] += 1
        return
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        if grid[x+dx,y+dy] == c+1:
            findpath(sx,sy,x+dx,y+dy)

for y in range(h):
    for x in range(w):
        if grid[x,y] == 0:
            findpath(x,y,x,y)

scores = defaultdict(lambda: 0)
for sx,sy,_,_ in trailheads:
    scores[sx,sy] += 1
print(sum([v for _,v in scores.items()]))
print(sum([v for _,v in ratings.items()]))
