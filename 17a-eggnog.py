#!/usr/bin/python3
import itertools
with open('17-input.txt') as fh:
    CONTAINERS = [int(i.strip()) for i in fh.readlines()]
MAX = 150

FOUND = 0

for i in range(1, len(CONTAINERS)):
    for c in itertools.combinations(CONTAINERS, i):
        if sum(c) == 150:
            FOUND += 1

print(FOUND)
