#!/usr/bin/python
import string
NICE = 0
NSEQ = ['ab', 'cd', 'pq', 'xy']

def test(s):
    # 1. Contains at least three vowels
    vowels = 0
    for v in 'aeiou':
        vowels += s.count(v)
    if vowels < 3:
        return False
    # 2 It contains at least one letter that appears twice in a row
    twice = False
    for i in string.ascii_lowercase:
        if (2 * i) in s:
            twice = True
    # 3. Does not contain some sequences
    if any([i in s for i in NSEQ]):
        return False

    return twice

with open('05-input.txt') as fh:
    for s in fh.readlines():
        NICE += int(test(s))
print(NICE)
