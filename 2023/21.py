#!/usr/bin/python3
import numpy as np
lines = open('21.txt').read().strip().split('\n')

grid = {}
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        grid[y,x] = c
        if c == 'S':
            oy,ox = y,x
            grid[y,x] = '.'
my,mx = y+1,x+1
todo = [(oy,ox)]

final_step = 26501365
cycle_len = len(lines[0])
check_mod = final_step%cycle_len

curve_fit = []
for step in range(1,cycle_len*5):
    stack = []
    seen = set()
    for y,x in todo:
        for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ty,tx = (y+dy)%my, (x+dx)%mx
            if grid[ty,tx] == '.' and (y+dy,x+dx) not in seen:
                stack.append((y+dy,x+dx))
                seen.add((y+dy,x+dx))
    if step == 64:
        print(f'p1: {len(seen)}')
    todo = stack
    if step%cycle_len == check_mod:
        print(step//cycle_len, len(seen))
        curve_fit.append((step//cycle_len,len(seen)))
        if len(curve_fit)==3:
            #[[65, 3744], [327, 92680], [589, 299976], [851, 625632]]
            curve_fit = np.array(curve_fit)
            a,b,c = tuple(np.polyfit(curve_fit[:, 0], curve_fit[:, 1], 2))
            a,b,c = int(a+0.5), int(b+0.5), int(c+0.5)
            point = final_step//cycle_len
            print(f'p2: {(a*point*point) + (b*point) + c}')
            exit(0)
