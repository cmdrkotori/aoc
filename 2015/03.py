#!/usr/bin/python3
from collections import defaultdict
with open('03.txt') as f:
    data = f.read().strip()

dd = {'v':(0,-1), '^':(0,1), '>':(1,0), '<':(-1,0)}
def domove(x,y,d):
    if d in dd:
        dx,dy = dd[d]
        y += dy
        x += dx
        p[x,y] += 1
    return x,y

p = defaultdict(lambda: 0)
p[0,0] = 1
y,x = 0,0
for d in data:
    x,y = domove(x,y,d)
print(len(p))

p = defaultdict(lambda: 0)
y,x,xx,yy = 0,0,0,0
p[0,0]=2
for d1,d2 in zip(*[iter(data)]*2):
    x,y = domove(x,y,d1)
    xx,yy = domove(xx,yy,d2)
print(len(p))
