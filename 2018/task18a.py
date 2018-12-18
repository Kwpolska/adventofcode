#!/usr/bin/env python3
import collections
OPEN, TREE, LUMBER = '.|#'
with open("input/18.txt") as fh:
    file_data = fh.read().strip()


def get_nearby(data, x, y):
    c = collections.Counter(OPEN=0, TREE=0, LUMBER=0)
    for xd in {-1, 0, 1}:
        for yd in {-1, 0, 1}:
            xn, yn = x + xd, y + yd
            if 0 <= xn < len(data) and 0 <= yn < len(data):
                if not (xd == 0 and yd == 0):
                    c.update(data[xn][yn])
    return c


def solve(data, dimen, time):
    data = [list(i) for i in data.split('\n')]
    for iteration in range(time):
        new_data = [i.copy() for i in data]
        for x in range(dimen):
            for y in range(dimen):
                current = data[x][y]
                nearby = get_nearby(data, x, y)
                if current == OPEN and nearby[TREE] >= 3:
                    new_data[x][y] = TREE
                elif current == TREE and nearby[LUMBER] >= 3:
                    new_data[x][y] = LUMBER
                elif current == LUMBER and (nearby[TREE] == 0 or nearby[LUMBER] == 0):
                    new_data[x][y] = OPEN

        data = new_data
    trees = lumber = 0
    for x in range(dimen):
        for y in range(dimen):
            if data[x][y] == TREE:
                trees += 1
            elif data[x][y] == LUMBER:
                lumber += 1
    return trees * lumber


test_data = """\
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""
test_output = solve(test_data, 10, 10)
test_expected = 1147
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data, 50, 10))

