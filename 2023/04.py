#!/usr/bin/pypy3
lines = open('04_bigboy.txt').read().strip().replace('  ',' ').split('\n')
cards = [l.split(': ')[1].split(' | ') for l in lines]
cards = [[set(x.split(' ')) for x in c] for c in cards]
wins = [len(c[0].intersection(c[1])) for c in cards]
scores = [2**(s-1) if s else 0 for s in wins]
print(sum(scores))

num = [1]*len(cards)
for n in range(len(num)):
    for m in range(wins[n]):
        z = n+m+1
        if z<len(cards):
            num[z] += num[n]
print(sum(num))
