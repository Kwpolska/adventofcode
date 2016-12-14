#!/usr/bin/env python3
# Repeat of 2015 day 4 AND 2016 day 5.
# Just wonderul.
import re
import hashlib
import sys

THREADS = 1

def h2016(d):
    for _ in range(2016):
        d = hashlib.md5(d.encode('ascii')).hexdigest()
    return d

def solve(data):
    i = 0
    keys = []
    while len(keys) != 64:
        d1 = hashlib.md5(data + str(i).encode('ascii')).hexdigest()
        d = h2016(d1)
        m = re.findall(r"(.)\1\1", d)
        if not m:
            i += THREADS
            continue
        else:
            quintuplet = 5 * m[0]
            for c in range(1, 1001):
                d2 = hashlib.md5(data + str(i + c).encode('ascii')).hexdigest()
                d2 = h2016(d2)
                if quintuplet in d2:
                    keys.append(i)
                    print(i)
                    break
            i += THREADS
    return keys


test_data = b"abc"
#test_output = solve(test_data)
test_expected = 22551
#print(test_output, test_expected)
#assert test_output == test_expected
print(solve(b"ahsbgdzn"))
