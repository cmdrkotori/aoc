#!/usr/bin/pypy3
from collections import defaultdict
import copy
with open('09.txt') as f:
    line = f.read().strip()
disk = []
head = 0
isfile = True
filenum = 0
files = []
for l in line:
    x = int(l)
    for y in range(x):
        disk.append(filenum if isfile else -1)
    if isfile:
        files.append([head,x])
    head += x
    if isfile:
        filenum += 1
    isfile = False if isfile else True

s = 0
ndisk = copy.copy(disk)
x = 0
y = len(ndisk)-1
while x < y:
    if ndisk[x] == -1:
        while ndisk[x] == -1 and x != y:
            ndisk[x] = ndisk[y]
            y -= 1
    if ndisk[x] != -1:
        s += x*ndisk[x]
        x += 1
print(s)


def placebefore(head,sz):
    gapsz = -1
    gapbeg = -1
    inagap = False
    for x in range(head):
        if disk[x] != -1:
            inagap = False
            gapbeg = -1
            gapsz = -1
            continue
        if not inagap and disk[x] == -1:
            inagap = True
            gapbeg = x
            gapsz = 1
        elif inagap and disk[x] == -1:
            gapsz += 1
        if gapsz == sz:
            return gapbeg
    return -1

y = len(files)-1
while y > 0:
    head,sz = files[y]
    nhead = placebefore(head,sz)
    if nhead != -1:
        for x in range(sz):
            disk[nhead+x] = y
            disk[head+x] = -1
    y -= 1

s = 0
for x,f in enumerate(disk):
    if f != -1:
        s += x*f
print(s)
