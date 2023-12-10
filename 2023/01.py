#!/usr/bin/pypy3
with open('01.txt') as f:
    lines = f.read().strip().split('\n')
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digits = ['___', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def check(t):
    if t[0] in numbers:
        return int(t[0])
    for x in [3,4,5]:
        if t[0:x] in digits:
            return digits.index(t[0:x])
    return None

p1 = [[int(n) for n in l if n in numbers] for l in lines]
p2 = [[check(l[i:]) for i in range(len(l)) if check(l[i:]) != None] for l in lines]
print(sum([d[0]*10 + d[-1] for d in p1 if len(d)]))
print(sum([d[0]*10 + d[-1] for d in p2 if len(d)]))
