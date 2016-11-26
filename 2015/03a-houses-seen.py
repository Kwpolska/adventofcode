#!/usr/bin/python
SEEN = {(0, 0)}
CURRENT = [0, 0]
with open('03-input.txt') as fh:
    for c in fh.read():
        if c == "^":
            CURRENT[1] += 1
        elif c == "v":
            CURRENT[1] -= 1
        elif c == "<":
            CURRENT[0] -= 1
        elif c == ">":
            CURRENT[0] += 1
        SEEN.add(tuple(CURRENT))
print(len(SEEN))
