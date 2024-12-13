#!/usr/bin/python3
import re
import numpy as np
from collections import defaultdict
with open('13.txt') as f:
    games = f.read().strip().split('\n\n')

def closeenough(x):
    y = int(x+0.5)
    return abs(x-y) < 0.001

def playgame2(g, p2):
    lines = g.split('\n')
    ax,ay = list(map(int, re.findall(r'\d+', lines[0])))
    bx,by = list(map(int, re.findall(r'\d+', lines[1])))
    x,y = list(map(int, re.findall(r'\d+', lines[2])))
    if p2:
        x+=10000000000000
        y+=10000000000000
    A = np.array([[ax,bx],[ay,by]])
    C = np.array([[x],[y]])
    if np.linalg.det(A) == 0:
        #print('No det!')
        return None
    A1 = np.linalg.inv(A)
    B = np.matmul(A1,C)
    a = B.item(0)
    b = B.item(1)
    if closeenough(a) and closeenough(b):
        return int(a+0.5)*3 + int(b+0.5)
    #print('Not close', a, b)
    return None

def go(p2):
    total = 0
    for g in games:
        cost = playgame2(g,p2)
        if cost:
            total+=cost
    print(total)

go(False)
go(True)
