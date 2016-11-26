#!/usr/bin/python
total = 0
with open('02-input.txt') as fh:
    for l in fh:
        l, w, h = map(int, l.strip().split('x'))
        a = l * w
        b = w * h
        c = h * l
        base = 2*a + 2*b + 2*c
        slack = min(a, b, c)
        total += base + slack
print(total)
