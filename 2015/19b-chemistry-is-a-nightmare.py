#!/usr/bin/python
# It took four hours for the leaderboard to fill up.  This was to be expected.
# Idea stolen from reddit comments.
REPLACEMENTS = []
FOUND = set()
with open('19-input.txt') as fh:
    d = fh.readlines()
    INPUT = d[-1].strip()
    for l in d[:-2]:
        REPLACEMENTS.append(l.strip().split(" => "))

aREPLACEMENTS = REPLACEMENTS.copy()

F = 0
CURRENT = INPUT
while CURRENT != 'e':
    try:
        f = max(REPLACEMENTS, key=lambda x: len(x[1]))
    except ValueError:
        REPLACEMENTS = aREPLACEMENTS.copy()
        f = max(REPLACEMENTS, key=lambda x: len(x[1]))
    before, after = f
    NEW = CURRENT.replace(after, before, 1)
    if CURRENT != NEW:
        F += 1
    else:
        REPLACEMENTS.remove(f)
    CURRENT = NEW
    print(CURRENT)

print(F)
