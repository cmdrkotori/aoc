#!/usr/bin/env pypy3
with open('01.txt') as f:
    text = ''.join(f.read().strip().split('\n'))
print(text.count('(')-text.count(')'))
index = 1
delta = 0
for t in text:
    delta += 1 if t=='(' else -1
    if delta == -1:
        print(index)
        raise SystemExit(0)
    index += 1
