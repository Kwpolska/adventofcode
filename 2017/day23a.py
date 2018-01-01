#!/usr/bin/env python3
with open("input/23.txt") as fh:
    file_data = fh.read().strip()

def p(arg, registers):
    try:
        return int(arg)
    except ValueError:
        return registers[arg]



def solve(data):
    rip = 0
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
    mul_count = 0
    instructions = [l.split() for l in data.split('\n')]
    while rip >= 0 and rip < len(instructions):
        instr, X, Y = instructions[rip]
        if instr == 'set':
            registers[X] = p(Y, registers)
        elif instr == 'sub':
            registers[X] -= p(Y, registers)
        elif instr == 'mul':
            registers[X] *= p(Y, registers)
            mul_count += 1
        elif instr == 'jnz':
            if p(X, registers) != 0:
                rip += p(Y, registers)
                rip -= 1
        rip += 1

    return mul_count


print(solve(file_data))
