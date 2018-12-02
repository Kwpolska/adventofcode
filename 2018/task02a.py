#!/usr/bin/env python3
import collections
with open("input/02.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    twos = threes = 0
    for line in data.split('\n'):
        c = collections.Counter(line)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    return twos * threes


test_data = "abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab"
test_output = solve(test_data)
test_expected = 12
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
