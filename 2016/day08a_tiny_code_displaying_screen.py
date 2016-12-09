#!/usr/bin/env python3
import numpy

with open("input/08.txt") as fh:
    file_data = fh.read()


def solve(data, width, height):
    array = numpy.zeros((height, width), numpy.bool)
    lines = [i for i in data.split('\n') if i]
    l = len(lines)
    # kwpbar.pbar(0, l)
    for n, line in enumerate(lines):
        if line.startswith('rect'):
            # OPERATION = rect
            a, b = (int(i) for i in line[4:].split('x'))
            for x in range(a):
                for y in range(b):
                    array[y][x] = True
        else:
            # OPERATION = rotate
            _, t, d, _, b = line.split()
            a = int(d[2:])
            b = int(b)
            if t == 'column':
                array[:,a] = numpy.roll(array[:,a], b)
            else:
                array[a] = numpy.roll(array[a], b)
    return numpy.count_nonzero(array)


test_data = "rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1"
test_output = solve(test_data, 7, 3)
test_expected = 6 # ".#..#.#\n#.#....\n.#....."
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data, 50, 6))
