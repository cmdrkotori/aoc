#!/usr/bin/pypy3
import copy

with open('02.txt') as f:
    text = f.read().strip().split('\n')
data = [list(map(int,x.split())) for x in text]

def incsafe(d):
    if d[1] > d[0]:
        return all(d[x+1] > d[x] for x in range(len(d)-1))
    if d[1] < d[0]:
        return all(d[x+1] < d[x] for x in range(len(d)-1))
    return False

def diffsafe(d):
    for x in range(len(d)-1):
        diff = abs(d[x+1] - d[x])
        if diff < 1 or diff > 3:
            return False
    return True

def p1(d):
    return incsafe(d) and diffsafe(d)

def p2(d):
    for x in range(len(d)):
        d2 = copy.copy(d)
        del d2[x]
        if p1(d2):
            return True
    return False

print(sum([1 if p1(d) else 0 for d in data]))
print(sum([1 if p2(d) else 0 for d in data]))
