#!/usr/bin/env python3
with open("input/02.txt") as fh:
    file_data = fh.read().strip()


def solve(data, do_swaps_task1=False):
    mem = [int(i) for i in data.split(',')]
    if do_swaps_task1:
        mem[1] = 12
        mem[2] = 2
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
    return ','.join(map(str, mem))


tests_data = ["1,9,10,3,2,3,11,0,99,30,40,50", "1,0,0,0,99", "2,4,4,5,99,0"]
tests_output = [solve(test_data, False) for test_data in tests_data]
tests_expected = ["3500,9,10,70,2,3,11,0,99,30,40,50", "2,0,0,0,99", "2,4,4,5,99,9801"]
for test_output, test_expected in zip(tests_output, tests_expected):
    print(test_output, test_expected)
    assert test_output == test_expected
print(solve(file_data, True))
