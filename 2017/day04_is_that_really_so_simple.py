#!/usr/bin/env python3
with open("input/04.txt") as fh:
    file_data = fh.read().strip()

def solve(data):
    count = 0
    for line in data.split('\n'):
        # PART 1
        # line_l = line.split()
        # PART 2
        line_l = [frozenset(i) for i in line.split()]
        line_s = set(line_l)
        if len(line_l) == len(line_s):
            count += 1
    return count

test_data = "abc def\naa aa bb"
test_output = solve(test_data)
test_expected = 1
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
