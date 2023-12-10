#!/usr/bin/pypy3
from collections import defaultdict
dirs = [(-1,0),(1,0),(0,-1),(0,+1)]

#Parse
lines = open('10.txt').read().strip().split('\n')
data = defaultdict(lambda: '.')
cons = defaultdict(lambda: [])
steps = defaultdict(lambda: -1)
pp = defaultdict(lambda: ' ')
y = 0
for l in lines:
    x = 0
    for c in l:
        data[y,x]=c
        if c == 'S':
            sx = x
            sy = y
        if c == '|':
            cons[y,x] = [(y-1,x),(y+1,x)]
        elif c == '-':
            cons[y,x] = [(y,x-1),(y,x+1)]
        elif c == 'L':
            cons[y,x] = [(y-1,x),(y,x+1)]
        elif c == 'J':
            cons[y,x] = [(y-1,x),(y,x-1)]
        elif c == '7':
            cons[y,x] = [(y+1,x),(y,x-1)]
        elif c == 'F':
            cons[y,x] = [(y+1,x),(y,x+1)]
        x+=1
    y+=1
cons[sy,sx] = [(sy+dy,sx+dx) for (dy,dx) in dirs if (sy,sx) in cons[sy+dy,sx+dx]]


#Follow
todo = [(sy,sx)]
steps[sy,sx] = 0
nsteps = 0
while len(todo) > 0:
    nsteps += 1
    npos = []
    for (ty,tx) in todo:
        for (ny,nx) in cons[ty,tx]:
            if data[ny,nx] != '.':
                if steps[ny,nx] == -1 or nsteps < steps[ny,nx] :
                    steps[ny,nx] = nsteps
                    npos.append((ny,nx))
    todo = npos
print(max(steps.values()))

#Draw
y = 0
py = 1
for l in lines:
    x = 0
    px = 1
    for c in l:
        if steps[y,x] != -1:
            pp[py,px] = '#'
            for (dy,dx) in dirs:
                if (y+dy,x+dx) in cons[y,x]:
                    pp[py+dy,px+dx] = '#'
        x+=1
        px += 2
    y+=1
    py+=2
mx,my=x,y
mpx,mpy=px,py

#Flood
todo = [(0,0)]
while len(todo) > 0:
    nxt = []
    for (ty,tx) in todo:
        for dy,dx in dirs:
            y,x = ty+dy,tx+dx
            if y < 0 or y>mpy or x<0 or x>mpx:
                continue
            if pp[y,x] == ' ':
                pp[y,x] = 'O'
                nxt.append((y,x))
    todo = nxt

#Count
enclosed = 0
for x in range(mx):
    for y in range(my):
        if pp[y*2+1,x*2+1] == ' ':
            enclosed += 1
print(enclosed)
