#!/usr/bin/env python3
with open("input/01.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    return sum(i // 3 - 2 for i in map(int, data.split()))


test_data = "12\n14\n1969\n100756"
test_output = solve(test_data)
test_expected = 2 + 2 + 654 + 33583
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
