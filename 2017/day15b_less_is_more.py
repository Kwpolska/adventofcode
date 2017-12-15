#!/usr/bin/env python3
import sys
INT_MAX = 2147483647
SIXTEEN = 0b1111_1111_1111_1111
MAX = 5_000_000
def solve(data):
    a, b = data
    afactor, bfactor = 16807, 48271
    count = 0
    for i in range(MAX):
        a = produce_number(a, afactor, 4)
        b = produce_number(b, bfactor, 8)
        if (i % 10000 == 0):
            sys.stderr.write('\r' + str(i))
        if (a & SIXTEEN) == (b & SIXTEEN):
            count += 1
    print("\n\n")
    return count


def produce_number(value, factor, divisor):
    while True:
        value = (value * factor) % INT_MAX
        if value % divisor == 0:
            return value

test_data = (65, 8921)

test_output = solve(test_data)
test_expected = 309
print(test_output, test_expected)
assert test_output == test_expected
print(solve((783, 325)))
