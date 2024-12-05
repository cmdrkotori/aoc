#!/usr/bin/pypy3
from collections import defaultdict

with open('05.txt') as f:
    rules,pages = [x.split('\n') for x in f.read().strip().split('\n\n')]

rra = defaultdict(lambda: set())
rrb = defaultdict(lambda: set())
for r in rules:
    rb,ra = [int(x) for x in r.split('|')]
    rra[rb].add(ra)
    rrb[ra].add(rb)
pp = [[int(x) for x in p.split(',')] for p in pages]

def check(p):
    lp = len(p)
    for x in range(lp):
        if x > 0:
            for y in range(x-1):
                if p[x] not in rra[p[y]]:
                    return False
        if x < lp-1:
            for y in range(x+1,lp):
                if p[x] not in rrb[p[y]]:
                    return False
    return True

print(sum(p[len(p)//2] for p in pp if check(p)))

def canbe(z,i,p):
    for x in range(0,i):
        if z not in rra[p[x]]:
            return False
    for x in range(i,len(p)):
        if z not in rrb[p[x]]:
            return False
    return True

def reorder(p):
    new = []
    new.insert(0,p[0])
    for z in p:
        for x in range(len(new)+1):
            if canbe(z,x,new):
                new.insert(x,z)
                break
    return new

print(sum(reorder(p)[len(p)//2] for p in pp if not check(p)))
