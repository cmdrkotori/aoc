#!/usr/bin/python3
import numpy as np
lines = open('18.txt').read().strip().split('\n')
cmds = []
for l in lines:
    a,b,c = l.split()
    cmds.append([a,int(b),c[2:8]])
deltas = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
digs = 'RDLU'

def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)
    x = x_y[:,0]
    y = x_y[:,1]
    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))
    area = np.absolute(S1 - S2) // 2
    return area

def solve(part2):
    coords = []
    x,y,z = 0,0,0
    for C in cmds:
        coords.append((x,y))
        a,b,c = C
        if part2:
            b = int(c[0:5],16)
            a = digs[int(c[5])]
        dy,dx = deltas[a]
        x = x + dx*(b)
        y = y + dy*(b)
        z += b
    return shoelace(coords)+(z//2)+1
print(solve(False),solve(True))

