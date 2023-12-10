#!/usr/bin/pypy3
from math import prod

# Process input
lines = open('03.txt').read().strip().split('\n')
w = len(lines[0])
h = len(lines)
d = {}
for y in range(h):
    for x in range(w):
        d[y,x] = lines[y][x]
s = [x for x in d if d[x]!='.' and not d[x].isnumeric()]
g = [x for x in s if d[x]=='*']

# Find numbers adjacent to symbols
dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
numbers = {}
def look(y,x):
    if (y,x) in numbers or not (y,x) in d or not d[y,x].isnumeric():
        return
    numbers[y,x] = d[y,x]
    look(y,x-1)
    look(y,x+1)
for y,x in s:
    for dy,dx in dirs:
        look(y+dy,x+dx)

# Part 1: calculate numbers adjacent to symbols
num_list = []
n = 0
found = False
label = {}
for y in range(h):
    for x in range(w+1):
        if (y,x) in numbers:
            if not found:
                found = True
            n = n*10 + int(numbers[y,x])
            label[y,x] = len(num_list)
        elif found:
            num_list.append(n)
            n = 0
            found = False
print(sum(num_list))

# Part 2: calculate gears
gears = []
for y,x in g:
    surround = set([label[y+dy,x+dx] for dy,dx in dirs if (y+dy,x+dx) in d and d[y+dy,x+dx].isnumeric()])
    if len(surround) == 2:
        gears.append(prod([num_list[n] for n in surround]))
print(sum(gears))
