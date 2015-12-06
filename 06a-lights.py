#!/usr/bin/python3
import numpy
import re
import kwpbar

R = re.compile('(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)')

a = numpy.zeros((1000, 1000), numpy.bool)

kwpbar.pbar(0, 300)
with open('06-input.txt') as fh:
    for nl, l in enumerate(fh, 1):
        m = R.match(l)
        action = m.groups()[0]
        x1, y1, x2, y2 = map(int, m.groups()[1:])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == 'turn on':
                    a[x][y] = True
                elif action == 'turn off':
                    a[x][y] = False
                elif action == 'toggle':
                    a[x][y] = not a[x][y]
        kwpbar.pbar(nl, 300)
print()
print(numpy.count_nonzero(a))
