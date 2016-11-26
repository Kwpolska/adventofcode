#!/usr/bin/python
SEEN = {(0, 0)}
CURRENT_SANTA = [0, 0]
CURRENT_ROBOT = [0, 0]
CURRENT = CURRENT_SANTA
CURRENT_NAME = "SANTA"
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
        if CURRENT_NAME == "SANTA":
            CURRENT = CURRENT_ROBOT
            CURRENT_NAME = "ROBOT"
        else:
            CURRENT = CURRENT_SANTA
            CURRENT_NAME = "SANTA"
print(len(SEEN))
