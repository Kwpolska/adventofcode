#!/usr/bin/env python3
with open("input/09.txt") as fh:
    file_data = fh.read()


def solve(data):
    size = 0
    while '(' in data:
        p = data.find("(")
        size += p  # index == number of characters before open-paren
        data = data[p:]
        sp = data.find(")")
        parenthesis = data[1:sp]
        data = data[sp + 1:]
        chars, times = (int(i) for i in parenthesis.split('x'))
        # Optimization idea stolen from /u/blockingthesky, thanks!
        # size += solve(data[:chars] * times)
        size += solve(data[:chars]) * times
        data = data[chars:]
    # leftover segment
    size += len(data)

    return size

for test_data, test_expected in (
    ("(3x3)XYZ", 9),
    ("X(8x2)(3x3)ABCY", 20),
    ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
    ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445)
):
    test_output = solve(test_data)
    print(test_output, test_expected)
    assert test_output == test_expected

print(solve(file_data.strip()))
