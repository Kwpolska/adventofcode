#!/usr/bin/env python3
with open("input/02.txt") as fh:
    fdata = fh.read()
    if not fdata.endswith('\n'):
        fdata += '\n'

KEYPAD = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

INDEXES = {'U': 0, 'D': 0, 'L': 1, 'R': 1}
DIFFS = {'U': -1, 'D': 1, 'L': -1, 'R': 1}
VALID = {0, 1, 2}

def solve(data):
    position = [1, 1]
    output = ""
    for char in data:
        if char == '\n':
            x, y = position
            output += str(KEYPAD[x][y])
            continue
        idx = INDEXES[char]
        diff = DIFFS[char]
        new = position[idx] + diff
        if new not in VALID:
            continue
        else:
            position[idx] = new


    return output

test = "ULL\nRRDDD\nLURDL\nUUUUD\n"
testsol = solve(test)
assert testsol == '1985'
print(solve(fdata))
