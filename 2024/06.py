#!/usr/bin/python3
with open('06.txt') as f:
    lines = f.read().strip().split('\n')
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
nextdir = [1,2,3,0]
w,h = len(lines[0]), len(lines)
npx,npy = -1,-1

def outside(x,y):
    return x < 0 or x >= w or y < 0 or y >= h
def crate(x,y):
    if outside(x,y):
        return False
    if lines[y][x] == '#':
        return True
    if npx == x and npy == y:
        return True
    return False

for y in range(h):
    for x in range(w):
        if lines[y][x] == '^':
            sx,sy = (x,y)

d = 0
def walk(x,y,d):
    dx,dy = dirs[d]
    places,steps = set(),set()
    while True:
        places.add((x,y))
        if (x,y,d) in steps:
            return None
        steps.add((x,y,d))
        while crate(x+dx,y+dy):
            d = nextdir[d]
            dx,dy = dirs[d]
        x += dx
        y += dy
        if outside(x,y):
            return places
pp = walk(sx,sy,0)
print(len(pp))

num = 0
for npx,npy in pp:
    if (npx,npy) == (sx,sy):
        continue
    if walk(sx,sy,0) is None:
        num += 1
print(num)
