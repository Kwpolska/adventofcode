#!/usr/bin/python
a = input()
floor = 0
for n, c in enumerate(a, 1):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor == -1:
        print(n)
        break
