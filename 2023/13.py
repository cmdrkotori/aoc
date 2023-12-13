#!/usr/bin/python3
import numpy as np
games = open('13.txt').read().strip().split('\n\n')

def are_same(rows,r,wide,limit):
    x = []
    smudges = 0
    for r2 in range(wide):
        for x1,x2 in zip(list(rows[r-r2]),list(rows[r+r2+1])):
            if x1 != x2:
                smudges += 1
    return smudges==limit

def which_same(array,limit):
    rows = [''.join(a) for a in array]
    h = len(rows)
    for r in range(h-1):
        if are_same(rows,r,1+min(r,h-r-2),limit):
            return r+1
    return 0

def play_game(limit):
    p = []
    for g in games:
        lines = g.split()
        array = [list(l) for l in lines]
        trans = np.array(array).T.tolist()
        p.append(which_same(array,limit)*100+which_same(trans,limit))
    return sum(p)

print(play_game(0),play_game(1))
