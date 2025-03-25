#!/usr/bin/python3
import hashlib
import itertools
with open('04.txt') as f:
    data = f.read().strip()

def find(num):
    needle = '0'*num
    for x in itertools.count(start=0):
        md5 = hashlib.md5((data + str(x)).encode()).hexdigest()
        if md5[0:num] == needle:
            return x

print(find(5))
print(find(6))
