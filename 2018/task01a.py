#!/usr/bin/env python3
with open("input/01.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    x = 0
    for l in data.split():
        x += int(l)
    return x


print(solve(file_data))
