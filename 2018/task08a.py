#!/usr/bin/env python3
from typing import List
with open("input/08.txt") as fh:
    file_data = fh.read().strip()


def go(data) -> int:
    sum = 0
    children = data.pop(0)
    meta = data.pop(0)
    for _ in range(children):
        sum += go(data)
    for _ in range(meta):
        sum += data.pop(0)
    return sum


def solve(data) -> int:
    data: List[int] = list(int(i) for i in data.split())
    total: int = 0
    while data:
        total += go(data)
    return total


test_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
test_output = solve(test_data)
test_expected = 138
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
