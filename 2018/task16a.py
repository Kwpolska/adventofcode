#!/usr/bin/env python3
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
    matches_three_or_more = 0
    for problem in data.split('\n\n'):
        before_line, op_line, after_line = problem.split('\n')
        before = json.loads(before_line.split(': ')[-1].strip())
        after = json.loads(after_line.split(': ')[-1].strip())
        op = [int(i) for i in op_line.split()]
        opcode_num, a, b, c = op

        print(op)
        cpu = CPU(before)
        matches = 0
        for operation in CPU.operations:
            operation(cpu, a, b, c)
            if cpu == after:
                print("Matches operation", operation)
                matches += 1
            cpu.undo()
        if matches >= 3:
            matches_three_or_more += 1
        print('\n')

    return matches_three_or_more


test_data = """Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]"""
test_output = solve(test_data)
test_expected = 1
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
