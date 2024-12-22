#!/usr/bin/pypy3
from collections import defaultdict
with open('22.txt') as f:
    lines = f.read().strip().split('\n')
nums = list(map(int,lines))

def mix(s, num):
    return s^num
def prune(s):
    return s%16777216
def nxt(num):
    num = prune(mix(num*64,num))
    num = prune(mix(num//32,num))
    num = prune(mix(num*2048,num))
    return num

s2 = 0
bananforseq = defaultdict(lambda: 0)
for x in nums:
    s = x
    d = []
    visited = set()
    for n in range(2000):
        os = s
        s = nxt(s)
        d.append(s%10 - os%10)
        if n >= 3:
            seq = (d[-4],d[-3],d[-2],d[-1])
            if seq not in visited:
                bananforseq[seq] += s%10
                visited.add(seq)
    s2 += s
print(s2)
print(max(bananforseq.values()))
