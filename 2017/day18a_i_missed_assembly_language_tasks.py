#!/usr/bin/env python3
from collections import defaultdict
with open("input/18.txt") as fh:
    file_data = fh.read().strip()


def p(arg, registers):
    if isinstance(arg, int):
        return arg
    return registers[arg]


def solve(data):
    registers = defaultdict(int)
    instructions_raw = data.split('\n')
    instructions = []
    for line in instructions_raw:
        parsed = line.split()
        instruction, args = parsed[0], parsed[1:]
        args2 = []
        for a in args:
            try:
                args2.append(int(a))
            except ValueError:
                args2.append(a)
        instructions.append((instruction, args2))

    rip = 0
    linstr = len(instructions)
    last_sound = None
    while 0 <= rip < linstr:
        instruction, args = instructions[rip]
        print(instruction, args)
        if instruction == 'snd':
            last_sound = registers[args[0]]
        elif instruction == 'set':
            registers[args[0]] = p(args[1], registers)
        elif instruction == 'add':
            registers[args[0]] += p(args[1], registers)
        elif instruction == 'mul':
            registers[args[0]] *= p(args[1], registers)
        elif instruction == 'mod':
            registers[args[0]] %= p(args[1], registers)
        elif instruction == 'rcv':
            if last_sound:
                return last_sound
        elif instruction == 'jgz':
            if registers[args[0]] > 0:
                rip += p(args[1], registers)
                continue
        rip += 1
    return False


test_data = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""
test_output = solve(test_data)
test_expected = 4
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
