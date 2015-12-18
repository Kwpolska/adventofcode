#!/usr/bin/python3
import numpy
import kwpbar

NOW = numpy.ndarray((100, 100), numpy.bool)
NEXT = None
runs = 100

with open('18-input.txt') as fh:
    for nl, l in enumerate(fh, 0):
        NOW[nl] = [c == '#' for c in l.strip()]

# Part 2: four lights are stuck
NOW[0][0] = NOW[99][0] = NOW[0][99] = NOW[99][99] = True

for iteration in range(runs):
    NEXT = numpy.ndarray((100, 100), numpy.bool)
    for rownum, rowval in enumerate(NOW):
        for colnum, cell_on in enumerate(rowval):
            # Find neighbors, in a very cheap way.
            neighbors = [
                (rownum-1, colnum),
                (rownum+1, colnum),
                (rownum, colnum-1),
                (rownum, colnum+1),
                (rownum-1, colnum-1),
                (rownum+1, colnum+1),
                (rownum-1, colnum+1),
                (rownum+1, colnum-1)
            ]
            # limit to numbers 0-100
            neighbors = [(i, j) for i, j in neighbors if i in range(100) and j in range(100)]
            neighbors_on = 0
            for nR, nC in neighbors:
                neighbors_on += NOW[nR][nC]

            # Determine new status of the current cell.
            if cell_on:
                NEXT[rownum][colnum] = (neighbors_on == 2 or neighbors_on == 3)
            else:
                NEXT[rownum][colnum] = (neighbors_on == 3)

        kwpbar.pbar((iteration * 100) + rownum, 100 * 100)
    NOW = NEXT
    # Part 2: four lights are stuck
    NOW[0][0] = NOW[99][0] = NOW[0][99] = NOW[99][99] = True

kwpbar.erase_pbar()
print(numpy.count_nonzero(NOW))
