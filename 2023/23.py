#!/usr/bin/pypy3
from collections import defaultdict
import copy
lines = open('23_s.txt').read().strip().split('\n')
dirs = [(0,1),(0,-1),(1,0),(-1,0)]

grid = defaultdict(lambda: '#')
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        grid[y,x] = c
my,mx = y,x

begin = (0,1)
end = (my,mx-1)

def process_graph(grid,p2):
    node = defaultdict(lambda: {})
    for y in range(my):
        for x in range(mx):
            if grid[y,x] == '#':
                continue
            if p2:
                for dy,dx in dirs:
                    if grid[y+dy,x+dx] != '#':
                        node[y,x][y+dy,x+dx] = 1
            else:
                if grid[y,x] == '.':
                    for dy,dx in dirs:
                        if grid[y+dy,x+dx] != '#':
                            node[y,x][y+dy,x+dx] = 1
                elif grid[y,x] == '^':
                    node[y,x][y-1,x] = 1
                elif grid[y,x] == 'v':
                    node[y,x][y+1,x] = 1
                elif grid[y,x] == '>':
                    node[y,x][y,x+1] = 1
                elif grid[y,x] == '<':
                    node[y,x][y,x-1] = 1
    return node

def shrink_graph(nodes):
    result = copy.deepcopy(nodes)
    keys = list(result.keys())
    for k in keys:
        if len(nodes[k]) == 2:
            a,b = result[k].keys()
            newlength = result[k][a] + result[k][b]
            if k in result[a]:
                result[a][b] = newlength
                del result[a][k]
            if k in result[b]:
                result[b][a] = newlength
                del result[b][k]
            del result[k]
    return result

def print_path(path):
    for y in range(my+1):
        l = []
        for x in range(mx+1):
            l.append('O' if (y,x) in path else grid[y,x])
        print(''.join(l))

def dfs(shrunk,path,start):
    best = 0
    if (start == end):
        #print_path(path)
        return max(path.values())
    for k in shrunk[start]:
        if k in path:
            continue
        new = path.copy()
        new[k] = path[start] + shrunk[start][k]
        candidate = dfs(shrunk,new,k)
        if candidate > best:
            best = candidate
    return best

def find_max(p2):
    nodes = process_graph(grid,p2)
    shrunk = shrink_graph(nodes)
    return dfs(shrunk,{begin: 0},begin)

print(find_max(False))
print(find_max(True))

