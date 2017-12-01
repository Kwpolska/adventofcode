#!/usr/bin/env python3
with open("input/01.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    sum = 0
    h = len(data) // 2
    for i, j in zip(data, data[h:]):
        if i == j:
            sum += int(i)
    for i, j in zip(data[h:], data):
        if i == j:
            sum += int(i)

    return sum


test_data = "123425"
test_output = solve(test_data)
test_expected = 4
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
