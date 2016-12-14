#!/usr/bin/env python3
# Repeat of 2015 day 4 AND 2016 day 5.
# Just wonderul.
import re
import hashlib
import sys
from multiprocessing import Pool


def h2016(d):
    for _ in range(2016):
        d = hashlib.md5(d.encode('ascii')).hexdigest()
    return d

def solve(i):
    data = b"ahsbgdzn"
    d1 = hashlib.md5(data + str(i).encode('ascii')).hexdigest()
    d = h2016(d1)
    m = re.findall(r"(.)\1\1", d)
    if not m:
        return None
    else:
        quintuplet = 5 * m[0]
        for c in range(1, 1001):
            d2 = hashlib.md5(data + str(i + c).encode('ascii')).hexdigest()
            d2 = h2016(d2)
            if quintuplet in d2:
                print(i)
                return i

p = Pool(4)
found = [203, 361, 372, 575, 3027, 3095, 3280, 3340, 3544, 3576, 3858, 3895, 3913, 3957, 4059, 4123]
new = [i for i in p.map(solve, range(4124, 300000)) if i is not None]
print(sorted(found + new))
