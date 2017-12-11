#!/usr/bin/env python3
with open("input/11.txt") as fh:
    file_data = fh.read().strip()

STEPS = {
    'nw': (-1, 0),
    'n': (0, -1),
    'ne': (1, -1),
    'sw': (-1, 1),
    's': (0, 1),
    'se': (1, 0),
}


# https://www.redblobgames.com/grids/hexagons/#neighbors-axial
def solve(data):
    x, y = 0, 0
    for step in data.split(','):
        sx, sy = STEPS[step]
        x += sx
        y += sy
    print(x, y)
    return (abs(x) + abs(y) + abs(x + y)) / 2


tests_data = ["ne,ne,ne", "ne,ne,sw,sw", "ne,ne,s,s", "se,sw,se,sw,sw"]
tests_output = [solve(test_data) for test_data in tests_data]
tests_expected = [3, 0, 2, 3]
for test_output, test_expected in zip(tests_output, tests_expected):
    print(test_output, test_expected)
    assert test_output == test_expected
print(solve(file_data))
