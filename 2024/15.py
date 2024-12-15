#!/usr/bin/python3
from collections import defaultdict
from math import prod
import re
with open('15.txt') as f:
    lines,commands = f.read().strip().split('\n\n')
lines = lines.split('\n')
commands = commands.split('\n')
grid = {}
botx,boty = 0,0
w,h = 0,0
dirs = {'<':(-1,0), '>':(1,0), '^':(0,-1), 'v':(0,1)}

def read1():
    global botx,boty,w,h
    for y,l in enumerate(lines):
        for x,c in enumerate(l):
            grid[x,y] = c
            if c == '@':
                botx,boty=x,y
    w = len(lines[0])
    h = len(lines)

def read2():
    global botx,boty,w,h
    for y,l in enumerate(lines):
        for x,c in enumerate(l):
            nx = x*2
            grid[nx,y] = c
            grid[nx+1,y] = c
            if c == 'O':
                grid[nx,y] = '['
                grid[nx+1,y] = ']'
            if c == '@':
                botx,boty=nx,y
                grid[nx+1,y] = '.'
    w = len(lines[0])*2
    h = len(lines)

def movebot1(x,y,d):
    dx,dy = dirs[d]
    def canmove():
        i = 1
        while True:
            nx,ny = x+(i*dx),y+(i*dy)
            if grid[nx,ny] == '.':
                return i
            if grid[nx,ny] == '#':
                return 0
            i += 1
    c = canmove()
    if c:
        # c == number of boxes to move in direction, +1
        for i in range(c+1):
            nx,ny = x+(i*dx),y+(i*dy)
            if grid[nx,ny] != '#':
                grid[nx,ny] = 'O'
        grid[x,y] = '.'
        x += dx
        y += dy
        grid[x,y] = '@'
    return x,y

def movebot2(x,y,d):
    dx,dy = dirs[d]
    if d == '<' or d == '>':
        def canmove():
            i = 1
            while True:
                nx,ny = x+(i*dx),y+(i*dy)
                if grid[nx,ny] == '.':
                    return i
                if grid[nx,ny] == '#':
                    return 0
                i += 1
        c = canmove()
        if c:
            # c == number of boxes to move in direction, +1
            for i in reversed(range(c+1)):
                nx,ny = x+(i*dx),y+(i*dy)
                if grid[nx,ny] != '#':
                    grid[nx,ny] = grid[nx-dx,ny-dy]
            grid[x,y] = '.'
            x += dx
            y += dy
            grid[x,y] = '@'
    else:
        boxes = set()
        def canmovey(x,y,dy):
            if grid[x,y+dy] == '.':
                return True
            if grid[x,y+dy] == '#':
                return False
            if grid[x,y+dy] == '[':
                boxes.add((x,y+dy))
                return canmovey(x,y+dy,dy) and canmovey(x+1,y+dy,dy)
            if grid[x,y+dy] == ']':
                boxes.add((x-1,y+dy))
                return canmovey(x,y+dy,dy) and canmovey(x-1,y+dy,dy)
        if canmovey(x,y,dy):
            if len(boxes):
                for bx,by in boxes:
                    grid[bx,by] = '.'
                    grid[bx+1,by] = '.'
                for bx,by in boxes:
                    grid[bx,by+dy] = '['
                    grid[bx+1,by+dy] = ']'
            grid[x,y] = '.'
            x += dx
            y += dy
            grid[x,y] = '@'
    return x,y

def showgrid(cmd):
    print(f'Move {cmd}:')
    for y in range(h):
        line = ''
        for x in range(w):
            line += grid[x,y]
        print(line)
    print('')

def gpssum():
    s = 0
    for k,v in grid.items():
        if v == 'O' or v == '[':
            x,y = k
            s += x+(y*100)
    return s

read1()
for cmd in commands:
    for c in cmd:
        botx,boty = movebot1(botx,boty,c)
print(gpssum())

read2()
for cmd in commands:
    for c in cmd:
        botx,boty = movebot2(botx,boty,c)
print(gpssum())
