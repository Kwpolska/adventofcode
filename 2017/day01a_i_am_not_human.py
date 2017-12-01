#!/usr/bin/env python3
with open("input/01.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    sum = 0
    for i, j in zip(data, data[1:]):
        if i == j:
            sum += int(i)
    # special casing for the last position
    i, j = data[0], data[-1]
    if i == j:
        sum += int(i)

    return sum


test_data = "91212129"
test_output = solve(test_data)
test_expected = 9
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
