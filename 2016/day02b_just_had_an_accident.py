#!/usr/bin/env python3
with open("input/02.txt") as fh:
    fdata = fh.read()
    if not fdata.endswith('\n'):
        fdata += '\n'

KEYPAD = (
    (' ', ' ', '1', ' ', ' '),
    (' ', '2', '3', '4', ' '),
    ('5', '6', '7', '8', '9'),
    (' ', 'A', 'B', 'C', ' '),
    (' ', ' ', 'D', ' ', ' '),
)

INDEXES = {'U': 0, 'D': 0, 'L': 1, 'R': 1}
DIFFS = {'U': -1, 'D': 1, 'L': -1, 'R': 1}
VALID = {0, 1, 2, 3, 4}


def solve(data):
    position = [2, 0]
    output = ""
    for char in data:
        if char == '\n':
            x, y = position
            output += str(KEYPAD[x][y])
            continue
        idx = INDEXES[char]
        diff = DIFFS[char]
        newpos = position.copy()
        newpos[idx] += diff
        x, y = newpos
        try:
            if KEYPAD[x][y] == ' ' or x not in VALID or y not in VALID:
                continue
            else:
                position = newpos
        except IndexError:
            continue

    return output

test = "ULL\nRRDDD\nLURDL\nUUUUD\n"
testsol = solve(test)
assert testsol == '5DB3'
print(solve(fdata))
