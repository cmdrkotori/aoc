#!/usr/bin/pypy3
import functools

@functools.cache
def make_candidate(dots,hashes):
    return '.'*dots + '#'*hashes + '.'

@functools.cache
def overlay(mask,candidate):
    return all(a==b or a=='?' for a,b in zip(mask,candidate))

@functools.cache
def check_em(mask,combos):
    if len(combos) == 0:
        # no matches left for remaining characters
        if '#' in mask:
            # something remained, but nothing to match with
            return 0
        # everything can be zero
        return 1

    hashes = combos[0]
    min_remain = sum(combos[1:]) + len(combos[1:])  # [1] must be at least ".#"
    count = 0
    for dots in range(len(mask)-hashes-min_remain+1):
        candidate = make_candidate(dots,hashes)
        if overlay(mask,candidate):
            count += check_em(mask[len(candidate):],combos[1:])
    return count

lines = open('12.txt').read().strip().split('\n')
masks = []
combos = []
for l in lines:
    m = l.split()
    n = m[1].split(',')
    combos.append(tuple([int(o) for o in n]))
    masks.append(m[0])

c1,c2 = 0,0
for i in range(len(masks)):
    c1 += check_em(masks[i],combos[i])
    c2 += check_em('?'.join([masks[i] for _ in range(5)]),combos[i]*5)
print(c1,c2)
