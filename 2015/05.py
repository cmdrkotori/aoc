#!/usr/bin/python3
from collections import Counter
from collections import defaultdict
with open('05.txt') as f:
    data = f.read().strip().split('\n')

def nice1(x):
    cc = Counter([c for c in x])
    return cc['a'] + cc['e'] + cc['i'] + cc['o'] + cc['u'] >= 3

def nice2(x):
    return any([x[c] == x[c+1] for c in range(len(x)-1)])

def naughty(x):
    return 'ab' in x or 'cd' in x or 'pq' in x or 'xy' in x

def okay1(x):
    return nice1(x) and nice2(x) and not naughty(x)

print(sum([1 if okay1(x) else 0 for x in data]))

def cond1(x):
    pairs = [x[i]+x[i+1] for i in range(len(x)-1)]
    pp = []
    while pairs:
        p = pairs.pop(0)
        if pairs and pairs[0] == p:
            pairs.pop(0)
        pp.append(p)
    cc = Counter(pp)
    return any([v >= 2 for _,v in cc.items()])

def cond2(x):
    return any([x[p]==x[p+2] for p in range(len(x)-2)])

def okay2(x):
    return cond1(x) and cond2(x)

print(sum([1 if okay2(x) else 0 for x in data]))
