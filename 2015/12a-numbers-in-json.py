#!/usr/bin/python3
import re
with open('12-input.txt') as fh:
    m = re.findall('(-?\d+)', fh.read())
    print(sum(int(i) for i in m))
