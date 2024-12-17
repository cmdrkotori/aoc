#!/usr/bin/pypy3
import re
with open('17.txt') as f:
    registers,codes = f.read().strip().split('\n\n')
registers = list(map(int,re.findall(r'\d+', registers)))
codes = list(map(int,re.findall(r'\d+', codes)))

def runprog(registers,codes):
    A,B,C = 0,1,2
    ip = 0
    output = []
    def combo(x):
        if x <= 3:
            return x
        return registers[x-4]
    while ip < len(codes):
        c = codes[ip]
        b = codes[ip+1]
        match codes[ip]:
            case 0:
                x = int(registers[A] / pow(2,combo(b)))
                registers[A] = x
                ip += 2
            case 1:
                x = registers[B]^b
                registers[B] = x
                ip += 2
            case 2:
                x = combo(b)%8
                registers[B] = x
                ip += 2
            case 3:
                if registers[A]:
                    ip = b
                else:
                    ip += 2
            case 4:
                x = registers[B] ^ registers[C]
                registers[B] = x
                ip += 2
            case 5:
                output.append(combo(b)%8)
                ip += 2
            case 6:
                x = int(registers[A] / pow(2,combo(b)))
                registers[B] = x
                ip += 2
            case 7:
                x = int(registers[A] / pow(2,combo(b)))
                registers[C] = x
                ip += 2
    return output

print(','.join(map(str,runprog(registers,codes))))

lowest = 0
def dfs(digit,start):
    global lowest
    if (digit == -1):
        if start < lowest or not lowest:
            lowest = start
        return
    i = digit
    j = codes[digit]
    searchamount = pow(8,i)
    for x in range(8):
        A = start + searchamount*x
        r = runprog([A,0,0],codes)
        if r[digit:16] == codes[digit:16]:
            dfs(digit-1,A)
dfs(15,pow(8,15))
print(lowest)
