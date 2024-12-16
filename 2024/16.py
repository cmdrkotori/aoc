#!/usr/bin/python3
from copy import copy
from heapq import heappush, heappop
with open('16.txt') as f:
    lines = f.read().strip().split('\n')
grid = {}
sx,sy = 0,0
ex,ey = 0,0
w,h = 0,0
dirs = {'<':(-1,0), '^':(0,-1),'>':(1,0), 'v':(0,1)}
dir_next_left =  {'<':'v', 'v':'>', '>':'^', '^':'<'}
dir_next_right = {'<':'^', '^':'>', '>':'v', 'v':'<'}
acceptable = ['.', 'E']

for y,l in enumerate(lines):
    for x,c in enumerate(l):
        grid[x,y] = c
        if c == 'S':
            sx,sy=x,y
        if c == 'E':
            ex,ey=x,y
w = len(lines[0])
h = len(lines)

def dj2():
    seats = set()
    final_score = -1
    visited = {}
    moves = []
    heappush(moves,(0,sx,sy,'>',set(),set()))
    while moves:
        score,x,y,d,seen,trail = heappop(moves)
        if (x,y,d) in seen:
            continue
        if (x,y) in trail:
            continue
        if final_score > 0 and score > final_score:
            continue
        if (x,y,d) in visited and visited[x,y,d] < score:
            continue
        visited[x,y,d] = score
        seen.add((x,y,d))
        trail.add((x,y))
        if (x,y) == (ex,ey):
            final_score = score
            seats.update(trail)
            continue
        def dodir(d,dscore):
            dx,dy = dirs[d]
            if grid[x+dx,y+dy] in acceptable:
                heappush(moves,(score+dscore,x+dx,y+dy,d,copy(seen),copy(trail)))
        dodir(d,1)
        dodir(dir_next_left[d],1001)
        dodir(dir_next_right[d],1001)
    display(grid,seats)
    return final_score,len(seats)

def display(grid,seen):
    for y in range(h):
        line = ''
        for x in range(w):
            line += 'O' if (x,y) in seen else grid[x,y]
        print(line)
    print('')

print(dj2())
