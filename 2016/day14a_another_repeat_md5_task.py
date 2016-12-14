#!/usr/bin/env python3
# Repeat of 2015 day 4 AND 2016 day 5.
# Just wonderul.
import re
import hashlib

def solve(data):
    i = 0
    keys = []
    while len(keys) != 64:
        d = hashlib.md5(data + str(i).encode('ascii')).hexdigest()
        m = re.findall(r"(.)\1\1", d)
        if not m:
            i += 1
            continue
        else:
            print(i, m[0])
            quintuplet = 5 * m[0]
            for c in range(1, 1001):
                d2 = hashlib.md5(data + str(i + c).encode('ascii')).hexdigest()
                if quintuplet in d2:
                    keys.append(i)
                    break
            i += 1
    return keys[63]


test_data = b"abc"
test_output = solve(test_data)
test_expected = 22728
print(test_output, test_expected)
assert test_output == test_expected
print(solve(b"ahsbgdzn"))
