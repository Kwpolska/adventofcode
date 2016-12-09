#!/usr/bin/env python3
# Repeat of 2015 day 4. I stole my own code from there.
import hashlib


def solve(data):
    answer = ''
    filled = 0
    i = 0
    while filled != 8:
        d = hashlib.md5(data + str(i).encode('ascii')).hexdigest()
        i += 1
        if d.startswith("00000"):
            answer += d[5]
            filled += 1
    return ''.join(answer)


test_data = b"abc"
test_output = solve(test_data)
test_expected = "18f47a30"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(b'abbhdwsy'))
