#!/usr/bin/pypy3
lines = open('14.txt').read().strip().split('\n')
grid = [list(l) for l in lines]

def rotate_counterclockwise(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def rotate_clockwise(m):
    return [list(reversed(col)) for col in zip(*m)]

def fall_row_left(row):
    cubes = [-1]
    cubes.extend([i for i in range(len(row)) if row[i] == '#'])
    cubes.append(len(row))
    new = ['.']*len(row)
    for i,j in zip(cubes[:-1], cubes[1::]):
        rocks = sum([1 for k in range(i+1,j) if row[k] == 'O'])
        if i >= 0:
            new[i] = '#'
        for k in range(i+1,i+1+rocks):
            new[k] = 'O'
    return new

def fall_all(m):
    for r in range(len(m)):
        m[r] = fall_row_left(m[r])

def fall_up():
    global grid
    grid = rotate_counterclockwise(grid)
    fall_all(grid)
    grid = rotate_clockwise(grid)

def load_up_beam(m):
    load = 0
    force = len(m)
    for r in m:
        load += sum([force for c in r if c == 'O'])
        force -= 1
    return load

def hash_grid(m):
    return ''.join([''.join(r) for r in m])

def print_grid(m):
    for r in m:
        print(''.join(r))
    print('')

def do_a_barrel_roll(cycle):
    global grid
    # Do north fall
    fall_up()
    if (cycle == 0):
        print(load_up_beam(grid))
    # Make west up, fall up
    grid = rotate_clockwise(grid)
    fall_up()
    # Make south up, fall up
    grid = rotate_clockwise(grid)
    fall_up()
    # Make east up, fall up
    grid = rotate_clockwise(grid)
    fall_up()
    # Make north up
    grid = rotate_clockwise(grid)

seen = {}
desired = 1000000000
for cycle in range(desired):
    do_a_barrel_roll(cycle)
    h = hash_grid(grid)
    if h in seen:
        lcycle,load = seen[h]
        cycle_len = cycle - lcycle
        ncycle = ((desired - lcycle) % cycle_len) + lcycle - 1
        print(list(seen.values())[ncycle][1])
        break
    seen[h] = (cycle, load_up_beam(grid))
