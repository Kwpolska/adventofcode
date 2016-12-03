#!/usr/bin/env python3
with open("input/03.txt") as fh:
    file_data = fh.read()


def solve(data):
    possible = 0
    for line in data.split('\n'):
        if not line:
            continue
        a, b, c = map(int, line.split())
        if (a + b) > c and (a + c) > b and (b + c) > a:
            possible += 1

    return possible


test_data = "5 10 25"
test_output = solve(test_data)
test_expected = 0
assert test_output == test_expected
print(solve(file_data))
