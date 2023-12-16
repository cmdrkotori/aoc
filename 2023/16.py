#!/usr/bin/pypy3
from collections import defaultdict
lines = open('16.txt').read().strip().split('\n')

field = defaultdict(lambda: '#')
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        field[y,x] = c
my,mx = y+1,x+1

splitters = { '|': [(-1,0),(1,0)], '-':[(0,-1),(0,1)] }
moves = {
    (0,1, '/'):[(-1,0)], (0,1, '\\'):[(1,0)],
    (0,-1,'/'):[(1,0)],  (0,-1,'\\'):[(-1,0)],
    (-1,0,'/'):[(0,1)],  (-1,0,'\\'):[(0,-1)],
    (1,0, '/'):[(0,-1)], (1,0, '\\'):[(0,1)],
    (0,1, '|'):[(-1,0),(1,0)],
    (0,-1,'|'):[(-1,0),(1,0)],
    (1,0, '-'):[(0,-1),(0,1)],
    (-1,0,'-'):[(0,-1),(0,1)] }

def shoot(dy,dx,y,x):
    energized = set()
    seen = set()
    todo = [(dy,dx,y,x)]
    while len(todo):
        dy,dx,y,x = todo.pop()
        if (dy,dx,y,x) in seen or field[y,x] == '#':
            continue
        seen.add((dy,dx,y,x))
        energized.add((y,x))
        if (dy,dx,field[y,x]) not in moves:
            todo.append((dy,dx,y+dy,x+dx))
            continue
        for d2y,d2x in moves[(dy,dx,field[y,x])]:
            todo.append((d2y,d2x,y+d2y,x+d2x))
    return(len(energized))

print(shoot(0,1,0,0))
configs = []
configs.extend([( 1,0,0,x) for x in range(mx)])
configs.extend([(-1,0,my-1,x) for x in range(mx)])
configs.extend([(0, 1,y,0) for y in range(my)])
configs.extend([(0,-1,y,mx-1) for y in range(my)])
print(max([shoot(*c) for c in configs]))
