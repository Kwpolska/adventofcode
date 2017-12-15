#!/usr/bin/env python3
import sys
INT_MAX = 2147483647
SIXTEEN = 0b1111_1111_1111_1111
MAX = 40_000_000
def solve(data):
    a, b = data
    afactor, bfactor = 16807, 48271
    count = 0
    for i in range(MAX):
        if (i % 10000 == 0):
            sys.stderr.write('\r' + str(i))
        a = (a * afactor) % INT_MAX
        b = (b * bfactor) % INT_MAX
        if (a & SIXTEEN) == (b & SIXTEEN):
            count += 1
    print("\n\n")
    return count


test_data = (65, 8921)

test_output = solve(test_data)
test_expected = 588
print(test_output, test_expected)
assert test_output == test_expected
print(solve((783, 325)))
