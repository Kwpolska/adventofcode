#!/usr/bin/env python3
import numpy


def solve(data):
    values = [[-1000 for _ in range(302)] for _ in range(302)]
    for x in range(1, 301):
        for y in range(1, 301):
            v = ((x + 10) * y + data) * (x + 10)
            values[x][y] = v // 100 % 10 - 5
    nv = numpy.array(values)
    best = (0, 0, 0)
    best_value = 0
    for s in range(2, 301):
        print(s)
        for x in range(1, 302 - s):
            for y in range(1, 302 - s):
                a = nv[x:(x + s), y:(y + s)]
                assert a.shape == (s, s)
                sq = a.sum()
                if sq > best_value:
                    best = (x, y, s)
                    best_value = sq

    return best


# test_data = [18, 42]
# test_expected = [(90, 269, 16)]
# for td, te in zip(test_data, test_expected):
    # test_output = solve(td)
    # print(test_output, te)
    # assert test_output == te
print(solve(4842))
