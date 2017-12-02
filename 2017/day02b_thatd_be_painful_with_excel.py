#!/usr/bin/env python3
import itertools
with open("input/02.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    sum = 0
    lines = [i for i in data.split('\n') if i]
    for line in lines:
        numbers = [int(i) for i in line.split()]
        for i, j in itertools.combinations(numbers, 2):
            if i % j == 0:
                sum += i / j
                break
            if j % i == 0:
                sum += j / i
                break
    return sum


test_data = "5 9 2 8\n9 4 7 3\n3 8 6 5"
test_output = solve(test_data)
test_expected = 9
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
