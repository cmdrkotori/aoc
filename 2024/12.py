#!/usr/bin/python3
from collections import defaultdict
with open('12.txt') as f:
    lines = f.read().strip().split('\n')
grid = defaultdict(lambda: '.')
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        grid[x,y] = c
w = len(lines[0])
h = len(lines)

seen=set()
regions = []

def findregion(x,y,c):
    region = set()
    def dfs(x,y,c):
        if (x,y) not in seen and grid[x,y] == c:
            seen.add((x,y))
            region.add((x,y))
            dfs(x-1,y,c)
            dfs(x+1,y,c)
            dfs(x,y-1,c)
            dfs(x,y+1,c)
    dfs(x,y,c)
    return region

def findperimeter(region):
    p = 0
    c = grid[list(region)[0]]
    for (x,y) in r:
        if grid[x-1,y] != c:
            p += 1
        if grid[x+1,y] != c:
            p += 1
        if grid[x,y-1] != c:
            p += 1
        if grid[x,y+1] != c:
            p += 1
    return p

for y in range(h):
    for x in range(w):
        if (x,y) not in seen:
            regions.append(findregion(x,y,grid[x,y]))

costs = 0
for r in regions:
    perimeter = findperimeter(r)
    costs += perimeter*len(r)
print(costs)

def findsides(region):
    fences = set()
    c = grid[list(region)[0]]
    for (x,y) in r:
        px,py = x*3,y*3
        if grid[x-1,y] != c:
            fences.add((px-1,py))
        if grid[x+1,y] != c:
            fences.add((px+1,py))
        if grid[x,y-1] != c:
            fences.add((px,py-1))
        if grid[x,y+1] != c:
            fences.add((px,py+1))
    p = 0
    for (px,py) in list(fences):
        if (px-3,py) not in fences and (px,py-3) not in fences:
            p += 1
    return p

costs = 0
for r in regions:
    sides = findsides(r)
    costs += sides*len(r)
print(costs)
