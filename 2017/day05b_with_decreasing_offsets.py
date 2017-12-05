#!/usr/bin/env python3
with open("input/05.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    instructions = [int(i) for i in data.split()]
    idx = 0
    count = 0
    while idx >= 0 and idx < len(instructions):
        jump_size = instructions[idx]
        if jump_size >= 3:
            instructions[idx] -= 1
        else:
            instructions[idx] += 1
        idx += jump_size
        count += 1
    return count


test_data = "0 3 0 1 -3"
test_output = solve(test_data)
test_expected = 10
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
