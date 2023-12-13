#!/usr/bin/pypy3
lines = open('11.txt').read().strip().split('\n')
nstars = []
ystars = set()
xstars = set()
y = 0
for l in lines:
    x = 0
    for c in l:
        if c == '#':
            nstars.append((y,x))
            xstars.add(x)
            ystars.add(y)
        x += 1
    y += 1
mx,my = x,y

def project(origin,sz,stretch):
    dest = {}
    new = 0
    for y in range(sz):
        if y not in origin:
            new += stretch-1
        dest[y] = new
        new += 1
    return dest

def galaxy(stretch):
    nxstars = project(xstars,mx,stretch)
    nystars = project(ystars,my,stretch)
    stars = {}
    mstars = []
    for (y,x) in nstars:
        stars[nystars[y],nxstars[x]] = '#'
        mstars.append((nystars[y],nxstars[x]))
    dists = []
    for x in range(len(mstars)):
        for y in range(len(mstars)):
            y1,x1 = mstars[x]
            y2,x2 = mstars[y]
            dists.append(abs(y2-y1)+abs(x2-x1))
    return sum(dists)//2

print(galaxy(2),galaxy(1000000))
