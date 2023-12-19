#!/usr/bin/pypy3
from math import prod
import copy
sections = open('19.txt').read().strip().split('\n\n')
works = {}
def lt(a,b): return a<b
def gt(a,b): return a>b
for l in sections[0].split('\n'):
    x = l.replace('}','')
    a,b = x.split('{')
    c = b.split(',')
    check = []
    for d in c:
        # e g f : h
        if ':' in d:
            isless = '<' in d
            e,f = d.split('<' if isless else '>')
            g = lt if isless else gt
            f,h = f.split(':')
            f = int(f)
        else:
            # accept, reject, send
            e,g,f,h = 'a',gt,0,d
        check.append((e,g,f,h))
    works[a] = check

parts = []
for l in sections[1].split('\n'):
    attr = l.replace('}','').replace('{','').split(',')
    p = {}
    for a in attr:
        b,c = a.split('=')
        p[b]=int(c)
    parts.append(p)

s = 0
for p in parts:
    cmd = 'in'
    while cmd != 'A' and cmd != 'R':
        todo = works[cmd]
        for a,op,b,c in todo:
            if op(p[a],b):
                cmd = c
                break
    if cmd == 'A':
        s += sum(p.values())
print(s)

total = 0
def calc_range(cmd, ranges):
    global total
    if cmd == 'R':
        return
    if cmd == 'A':
        total += prod([1+b-a for a,b in ranges.values()])
        return
    for a,op,b,c in works[cmd]:
        u,v = ranges[a]
        ranges2 = copy.deepcopy(ranges)
        ranges2[a] = (max(b+1,u),v) if op == gt else (u,min(b-1,v))
        calc_range(c,ranges2)
        ranges[a]  = (u,min(b,v))   if op == gt else (max(b,u),v)

calc_range('in', {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's':(1,4000)})
print(total)
