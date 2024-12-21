#!/usr/bin/python3
import functools
from heapq import heappush, heappop
with open('21.txt') as f:
    lines = f.read().strip().split('\n')

dirs = {'<':(-1,0), '>':(1,0), '^':(0,-1), 'v':(0,1)}

dpad=[' ^A','<v>']
npad=['789','456','123',' 0A']

def makelocs(pad):
    locs = {}
    grid = {}
    for y,l in enumerate(pad):
        for x,c in enumerate(l):
            if c != ' ':
                locs[c] = (x,y)
                grid[x,y] = c
    return locs,grid

nlocs,ngrid = makelocs(npad)
dlocs,dgrid = makelocs(dpad)

def null(xlocs,xgrid,A,B,d,xfunc):
    return d

def shortest(locs,grid,A,B):
    x,y = locs[A]
    ex,ey = locs[B]
    visited = {}
    moves = [(0,x,y,'<','')]
    finalscore = -1
    while moves:
        score,x,y,d,path = heappop(moves)
        if (x,y,d) in visited and score > visited[x,y,d]:
            continue
        visited[x,y,d] = score
        if finalscore > -1 and score > finalscore:
            continue
        if (x,y) == (ex,ey):
            if finalscore == -1 or score==finalscore:
                finalscore = score
                yield path+'A'
        for d in dirs:
            dx,dy = dirs[d]
            nx,ny = x+dx,y+dy
            if (nx,ny) in grid and (nx,ny,d) not in visited:
                p = path+d
                heappush(moves,(len(p),nx,ny,d,p))

def makepathmap(locs,grid):
    p = {}
    for c1 in locs:
        for c2 in locs:
            p[c1,c2]=list(shortest(locs,grid,c1,c2))
    return p
npathmap = makepathmap(nlocs,ngrid)
dpathmap = makepathmap(dlocs,dgrid)

@functools.cache
def broot2(frm, to, level, maxlevel):
    if level == 0:
        return min(map(len,dpathmap[frm,to]))
    paths = npathmap[frm,to] if level==maxlevel else dpathmap[frm,to]
    ln = 0
    for p in paths:
        pos = 'A'
        x = 0
        for pp in p:
            x += broot2(pos,pp,level-1,maxlevel)
            pos = pp
        if not ln or x < ln:
            ln = x
    return ln

def brootpath(path, level):
    pos = 'A'
    s = 0
    for x in path:
        s += broot2(pos, x, level, level)
        pos = x
    return s*int(path[0:3])

s1,s2 = 0,0
for l in lines:
    s1 += brootpath(l,2)
    s2 += brootpath(l,25)
print(s1,s2)
