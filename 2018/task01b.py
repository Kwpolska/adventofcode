#!/usr/bin/env python3
with open("input/01.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    x = 0
    seen = {0}
    while True:
        for l in data.split():
            x += int(l)
            if x in seen:
                return x
            seen.add(x)


print(solve(file_data))
