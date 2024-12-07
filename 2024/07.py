#!/usr/bin/pypy3
with open('07.txt') as f:
    lines = f.read().strip().split('\n')
ans,nums = [],[]
for l in lines:
    a,b = l.split(': ')
    ans.append(int(a))
    nums.append(list(map(int,b.split(' '))))

def findanswer1(a,b,c):
    if not b:
        return c == a
    bb = b[1:]
    return findanswer1(a, bb, c*b[0]) or findanswer1(a, bb, c+b[0])

def findanswer2(a,b,c):
    if not b:
        return c == a
    bb = b[1:]
    return findanswer2(a, bb, c*b[0]) or findanswer2(a, bb, c+b[0]) or findanswer2(a, bb, int(f'{c}{b[0]}'))

print(sum([ans[x] for x in range(len(ans)) if findanswer1(ans[x],nums[x][1:],nums[x][0])]))
print(sum([ans[x] for x in range(len(ans)) if findanswer2(ans[x],nums[x][1:],nums[x][0])]))
