#!/usr/bin/env python3
with open("input/16b.txt") as fh:
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

    def run(self, op, a, b, c):
        print(self.opcodes[op], a, b, c)
        self.opcodes[op](self, a, b, c)

    def run_line(self, line):
        self.run(*(int(i) for i in line.split()))

    operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    opcodes = {
        0: seti,
        1: eqir,
        2: setr,
        3: gtir,
        4: addi,
        5: muli,
        6: mulr,
        7: gtrr,
        8: bani,
        9: gtri,
        10: bori,
        11: banr,
        12: borr,
        13: eqri,
        14: eqrr,
        15: addr
    }


def solve(data):
    cpu = CPU()
    for line in data.split('\n'):
        cpu.run_line(line)
        print(cpu.registers)

    return cpu.registers[0]


print(solve(file_data))
