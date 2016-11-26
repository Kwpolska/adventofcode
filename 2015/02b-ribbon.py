#!/usr/bin/python
total = 0
with open('02-input.txt') as fh:
    for l in fh:
        l, w, h = map(int, l.strip().split('x'))
        dim = [l, w, h]
        a = min(dim)
        dim.remove(a)
        b = min(dim)
        ribbon = 2 * a + 2 * b
        bow = l * w * h
        total += ribbon + bow
print(total)
