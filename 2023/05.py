#!/usr/bin/pypy3
# P1: 199602917
# P2: 2254686

# Process input
sections = open('05.txt').read().strip().split('\n\n')
seeds = [int(x) for x in sections[0].replace('seeds: ','').split()]
data = [[[int(x) for x in s.split()] for s in y.split('\n')[1:]] for y in sections]
ranges = [[seeds[x*2],seeds[x*2+1]] for x in range(len(seeds)//2)]

def parse_var(t,x):
    for y in t:
        rnge = y[2]
        dest = y[0]
        src = y[1]
        if x>=src and x<src+rnge:
            return dest+(x-src)
    return x

locations = []
for seed in seeds:
    loc = seed
    for d in data:
        loc = parse_var(d,loc)
    locations.append(loc)
print(min(locations))

def parse_loc(loc):
    for d in data[::-1]:
        for y in d:
            rnge = y[2]
            dest = y[0]
            src = y[1]
            if loc>=dest and loc<=dest+rnge:
                loc = src+(loc-dest)
                break
    return loc

for x in range(0,10000000000000):
    loc = parse_loc(x)
    for r in ranges:
        if loc>=r[0] and loc<r[0]+r[1]:
            print(x)
            exit(0)
