#!/usr/bin/pypy3
from math import lcm
lines = open('08.txt').read().strip().split('\n')
directions = list(lines[0])
graph = {}
for l in lines[2:]:
    #JKT = (KFV, CFQ)
    #0123456789012345
    graph[l[0:3]] = [l[7:10], l[12:15]]

node = 'AAA'
steps = 0
d = 0
while node != 'ZZZ':
    node = graph[node][0 if directions[d]=='L' else 1]
    d += 1
    if d >= len(directions):
        d = 0
    steps += 1
print(steps)

nodes = [n for n in graph if n[2]=='A']
steps_until = [0]*len(nodes)
for x in range(len(nodes)):
    steps = 0
    d = 0
    while nodes[x][2] != 'Z':
        n = nodes[x]
        nodes[x] = graph[n][0 if directions[d]=='L' else 1]
        d += 1
        if d >= len(directions):
            d = 0
        steps += 1
    steps_until[x] = steps
print(lcm(*steps_until))
