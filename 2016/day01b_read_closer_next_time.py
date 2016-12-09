#!/usr/bin/env python3
directions = []
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
loc = [0, 0]
seen = set()
INDEXES = {NORTH: 1, SOUTH: 1, EAST: 0, WEST: 0}
DIFFS = {NORTH: 1, SOUTH: -1, EAST: 1, WEST: -1}

DIR = NORTH

with open("input/01.txt") as fh:
    directions_t = fh.read().split(', ')
    for t in directions_t:
        directions.append((t[0], int(t[1:].strip())))

for direction, distance in directions:
    if direction == 'L':
        DIR = (DIR - 1) % 4
    elif direction == 'R':
        DIR = (DIR + 1) % 4

    for n in range(0, distance):
        loc[INDEXES[DIR]] += DIFFS[DIR]
        # Breaks down with lists for some reason.
        loct = tuple(loc)
        if loct in seen:
            print(loct)
            print(abs(loc[0]) + abs(loc[1]))
            exit(0)
        else:
            seen.add(loct)
