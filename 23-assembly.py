#!/usr/bin/python3
import re
with open('23-input.txt') as fh:
    instructions = [i.strip() for i in fh.readlines()]

# Part 1: (0, 0)
# Part 2: (1, 0)
R = {'a': 1, 'b': 0}
P = re.compile("(hlf|tpl|inc|jmp|jie|jio) (.*)")
JIP = re.compile("([ab]), ([+-]\d+)")
i = 0 # instruction counter
maxi = len(instructions) - 1


while i <= maxi:
    d = P.match(instructions[i]).groups()
    inst = d[0]
    reg = d[1]
    print(inst, reg)

    if inst == 'hlf':
        R[reg] = R[reg] // 2
        i += 1
    elif inst == 'tpl':
        R[reg] = R[reg] * 3
        i += 1
    elif inst == 'inc':
        R[reg] = R[reg] + 1
        i += 1
    elif inst == 'jmp':
        i += int(reg)
    elif inst == 'jie':
        reg, jump = JIP.match(reg).groups()
        if R[reg] % 2 == 0:
            i += int(jump)
        else:
            i += 1
    elif inst == 'jio':
        reg, jump = JIP.match(reg).groups()
        if R[reg] == 1:
            i += int(jump)
        else:
            i += 1

print(R)
