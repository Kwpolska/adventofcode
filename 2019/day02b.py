#!/usr/bin/env python3
with open("input/02.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    membase = [int(i) for i in data.split(',')]
    for noun in range(0, 100):
        for verb in range(0, 100):
            mem = membase.copy()
            mem[1] = noun
            mem[2] = verb

            loc = 0
            while mem[loc] != 99:
                if mem[loc] == 1:
                    mem[mem[loc + 3]] = mem[mem[loc + 1]] + mem[mem[loc + 2]]
                    loc += 4
                elif mem[loc] == 2:
                    mem[mem[loc + 3]] = mem[mem[loc + 1]] * mem[mem[loc + 2]]
                    loc += 4
                else:
                    raise Exception("Invalid opcode")
            if mem[0] == 19690720:
                return 100 * noun + verb
    return "FAIL"


print(solve(file_data))
