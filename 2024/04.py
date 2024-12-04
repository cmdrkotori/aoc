#!/usr/bin/pypy3
from collections import defaultdict

with open('04.txt') as f:
    text = f.read().strip().split('\n')

grid = defaultdict(lambda: '.')
w,h = len(text[0]),len(text)
for y in range(h):
    line = text[y]
    for x in range(w):
        grid[x,y] = line[x]

dxy = [(1,0),(-1,0), (1,1),(0,1),(-1,1), (1,-1),(0,-1),(-1,-1)]
def check(x,y,s,dx,dy):
    if grid[x,y] != s[0]:
        return False
    if len(s) > 1:
        return check(x+dx,y+dy,s[1:],dx,dy)
    return True
print(sum([1 if check(x,y,'XMAS',dx,dy) else 0 for dx,dy in dxy for x in range(w) for y in range(h)]))

diag1 = [[(1,1),(-1,-1)], [(-1,-1),(1,1)]]
diag2 = [[(1,-1),(-1,1)], [(-1,1),(1,-1)]]
def checkdir(x,y,diag):
    for dxy1,dxy2 in diag:
        dx1,dy1 = dxy1
        dx2,dy2 = dxy2
        if grid[x+dx1,y+dy1] == 'M' and grid[x+dx2,y+dy2] == 'S':
            return True
    return False
print(sum([1 if grid[x,y] == 'A' and checkdir(x,y,diag1) and checkdir(x,y,diag2) else 0 for x in range(w) for y in range(h)]))
