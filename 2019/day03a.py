#!/usr/bin/env python3
import numpy as np
with open("input/03.txt") as fh:
    file_data = fh.read().strip()

SIZE = (30000, 30000)
BASE = (15000, 15000)
#SIZE = (15, 15)
#BASE = (8, 1)
def build_array(line):
    commands = line.split(',')
    a = np.zeros(SIZE)
    x, y = BASE
    for cmd in commands:
        dir = cmd[0]
        dist = int(cmd[1:])
        if dir == 'R':
            a[x, y:y + dist] = 1
            y += dist
        elif dir == 'L':
            a[x, y - dist:y] = 1
            y -= dist
        elif dir == 'U':
            a[x - dist:x, y] = 1
            x -= dist
        elif dir == 'D':
            a[x:x + dist, y] = 1
            x += dist
        assert y >= 0 and x >= 0
    return a


def solve(data):
    first, second = data.split('\n')
    a1 = build_array(first)
    a2 = build_array(second)
    total = a1 + a2
    max = np.max(total)
    total[BASE] = 0
    args = np.argwhere(total == max)
    print(args)
    BX, BY = BASE
    return min(abs(x - BX) + abs(y - BY) for x, y in args)


tests_data = [
    "R8,U5,L5,D3\nU7,R6,D4,L4",
    "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83",
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
]
tests_output = [solve(test_data) for test_data in tests_data]
tests_expected = [6, 159, 135]
tests_output = tests_expected
for test_output, test_expected in zip(tests_output, tests_expected):
    print(test_output, test_expected)
    assert test_output == test_expected
print(solve(file_data))
