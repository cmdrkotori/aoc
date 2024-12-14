#!/usr/bin/python3
from collections import defaultdict
from math import prod
import re

from collections import defaultdict
with open('14.txt') as f:
    lines = f.read().strip().split('\n')
robots = [list(map(int, re.findall(r'[0123456789-]+', l))) for l in lines]

w = 101
h = 103
def step(n):
    new = []
    for r in robots:
        x,y,dx,dy = r
        x = (x + dx*n)%w
        y = (y + dy*n)%h
        new.append([x,y,dx,dy])
    return new

def sf(bots):
    s1,s2,s3,s4 = 0,0,0,0
    for r in bots:
        x,y,dx,dy = r
        left = x < w//2
        right = x > w//2
        top = y < h//2
        bottom = y > h//2
        if left and top:
            s1 += 1
        if right and top:
            s2 += 1
        if left and bottom:
            s3 += 1
        if right and bottom:
            s4 += 1
    return s1,s2,s3,s4

print(prod(sf(step(100))))

def bins(bots):
    dx = defaultdict(lambda: 0)
    dy = defaultdict(lambda: 0)
    for x,y,_,_ in bots:
        dx[x] += 1
        dy[y] += 1
    itemsx = [v for _,v in dx.items()]
    itemsy = [v for _,v in dy.items()]
    return max(itemsx)*max(itemsy)

mxscore = 0
for x in range(w*h):
    bots = step(x)
    score = bins(bots)
    if score > mxscore:
        mxscore = score
        y = x
print(y)

