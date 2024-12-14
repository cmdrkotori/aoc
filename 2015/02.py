#!/usr/bin/python3
with open('02.txt') as f:
    lines = f.read().strip().split('\n')
boxes = [list(map(int,l.split('x'))) for l in lines]

p1,p2 = 0,0
for x,y,z in boxes:
    sides = [x*z, x*y, y*z]
    slack = min(sides)
    p1 += 2*sum(sides) + slack
    p2 += min([x+x+z+z, x+x+y+y, y+y+z+z]) + x*y*z
print(p1,p2)
