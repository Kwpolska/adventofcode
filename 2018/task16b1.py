#!/usr/bin/env python3
# 16b1: figure out opcode meaning
import collections
import json
with open("input/16a.txt") as fh:
    file_data = fh.read().strip()


class CPU:
    registers = []

    def __init__(self, registers=None):
        if registers is None:
            self.registers = [0, 0, 0, 0]
        else:
            self.registers = registers
        self.starting = self.registers.copy()

    def undo(self):
        self.registers = self.starting.copy()

    def copy(self):
        return CPU(self.registers.copy())

    def __eq__(self, other):
        if isinstance(other, CPU):
            return self.registers == other.registers
        return self.registers == other  # list

    def addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]

    def addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b

    def mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]

    def muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b

    def banr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]

    def bani(self, a, b, c):
        self.registers[c] = self.registers[a] & b

    def borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]

    def bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b

    def setr(self, a, _b, c):
        self.registers[c] = self.registers[a]

    def seti(self, a, _b, c):
        self.registers[c] = a

    def gtir(self, a, b, c):
        self.registers[c] = int(a > self.registers[b])

    def gtri(self, a, b, c):
        self.registers[c] = int(self.registers[a] > b)

    def gtrr(self, a, b, c):
        self.registers[c] = int(self.registers[a] > self.registers[b])

    def eqir(self, a, b, c):
        self.registers[c] = int(a == self.registers[b])

    def eqri(self, a, b, c):
        self.registers[c] = int(self.registers[a] == b)

    def eqrr(self, a, b, c):
        self.registers[c] = int(self.registers[a] == self.registers[b])

    operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


def solve(data):
    candidates = {}
    for opcode_num in range(16):
        candidates[opcode_num] = collections.Counter()

    for problem in data.split('\n\n'):
        before_line, op_line, after_line = problem.split('\n')
        before = json.loads(before_line.split(': ')[-1].strip())
        after = json.loads(after_line.split(': ')[-1].strip())
        op = [int(i) for i in op_line.split()]
        opcode_num, a, b, c = op

        print(op)
        cpu = CPU(before)
        for operation in CPU.operations:
            operation(cpu, a, b, c)
            if cpu == after:
                candidates[opcode_num][operation.__name__] += 1
            cpu.undo()

    functions = {}
    for opcode_num in range(16):
        functions[opcode_num] = candidates[opcode_num].most_common()
        print(opcode_num, candidates[opcode_num].most_common())

    print()

    for op in CPU.operations:
        poss = []
        for opcode_num in range(16):
            if op.__name__ in candidates[opcode_num]:
                poss.append(opcode_num)
        print(op.__name__, poss)

    return functions


solve(file_data)
