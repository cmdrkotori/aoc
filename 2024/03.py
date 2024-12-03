#!/usr/bin/pypy3
import re

with open('03.txt') as f:
    text = f.read().strip()

def find(p2):
    sum = 0
    muls = re.finditer(r'mul\((\d*),(\d*)\)', text)
    dos = re.finditer(r'do\(\)', text)
    dont = re.finditer(r'don\'t\(\)', text)
    cmd = {}
    for m in muls:
        cmd[m.span()[0]] = text[m.span()[0]:m.span()[1]]
    if p2:
        for m in dos:
            cmd[m.span()[0]] = text[m.span()[0]:m.span()[1]]
        for m in dont:
            cmd[m.span()[0]] = text[m.span()[0]:m.span()[1]]
    cmd = dict(sorted(cmd.items()))
    on = True
    for k,c in cmd.items():
        if c == 'do()':
            on = True
            continue
        if c == 'don\'t()':
            on = False
            continue
        if on:
            match = re.match(r'mul\((\d*),(\d*)\)', c)
            sum += int(match.group(1)) * int(match.group(2))
    print(sum)

find(False)
find(True)
