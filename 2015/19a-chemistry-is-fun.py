#!/usr/bin/python
REPLACEMENTS = []
FOUND = set()
with open('19-input.txt') as fh:
    d = fh.readlines()
    INPUT = d[-1].strip()
    for l in d[:-2]:
        REPLACEMENTS.append(l.strip().split(" => "))

for before, after in REPLACEMENTS:
    # We need to find every instance of `before`.
    loc = -1
    i = 0
    indexes = []
    while True:
        i += 1
        loc = INPUT.find(before, loc + 1)
        if loc != -1:
            indexes.append(loc)
        else:
            break
    # And now, replace it.
    for current in indexes:
        FOUND.add(INPUT[0:current] + after + INPUT[current+len(before):])

print(len(FOUND))
