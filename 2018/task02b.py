#!/usr/bin/env python3
import collections
with open("input/02.txt") as fh:
    file_data = fh.read().strip()

def levenshtein(s1, s2):
    u"""Calculate the Levenshtein distance of two strings.

    Implementation from Wikibooks:
    https://en.wikibooks.org/w/index.php?title=Algorithm_Implementation/Strings/Levenshtein_distance&oldid=2974448#Python
    Copyright © The Wikibooks contributors (CC BY-SA/fair use citation); edited to match coding style and add an exception.
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # j+1 instead of j since previous_row and current_row are one character longer than s2
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def solve_find(data):
    for line1 in data.split('\n'):
        for line2 in data.split('\n'):
            if levenshtein(line1, line2) == 1:
                return (line1, line2)


def solve(data):
    common = ""
    for a, b in zip(*solve_find(data)):
        if a == b:
            common += a
    return common


test_data = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

test_output = solve(test_data)
test_expected = "fgij" # ("fghij", "fguij")
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
