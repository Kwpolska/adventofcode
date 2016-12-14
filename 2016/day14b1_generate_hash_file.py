#!/usr/bin/env python3
# Repeat of 2015 day 4 AND 2016 day 5.
# Just wonderul.
import re
import hashlib
import kwpbar

def h2016(d):
    for _ in range(2016):
        d = hashlib.md5(d.encode('ascii')).hexdigest()
    return d

i = 0
keys = []
data = b"ahsbgdzn"
with open('input/14_hashes.txt', 'w') as fh:
    for i in range(30000):
        d1 = hashlib.md5(data + str(i).encode('ascii')).hexdigest()
        d = h2016(d1)
        m3 = re.findall(r"(.)\1\1", d)
        if m3:
            m5 = re.findall(r"(.)\1\1\1\1", d)
        else:
            m5 = []
        fh.write('{0}:{1}:{2}:{3}\n'.format(i, d, ','.join(m3), ','.join(m5)))
        kwpbar.pbar(i, 30000)
