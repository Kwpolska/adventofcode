#!/usr/bin/env python3
directions = []
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
x = 0
y = 0
DIR = NORTH

with open("input/01.txt") as fh:
    directions_t = fh.read().split(', ')
    for t in directions_t:
        directions.append((t[0], int(t[1:].strip())))

for direction, distance in directions:
    if direction == 'L':
        DIR -= 1
    elif direction == 'R':
        DIR += 1

    # wrap around
    DIR %= 4

    if DIR == NORTH:
        y += distance
    elif DIR == SOUTH:
        y -= distance
    elif DIR == EAST:
        x += distance
    elif DIR == WEST:
        x -= distance

print(x, y)
print(abs(x) + abs(y))
