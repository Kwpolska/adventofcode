#!/usr/bin/env python3
import re

with open("input/07.txt") as fh:
    file_data = fh.read()


def solve(data):
    count = 0
    r2 = 0
    for line in data.split('\n'):
        if not line:
            continue
        sp = re.split('\\[([a-z]+)\\]', line)
        inner = []
        outer = []
        for n, i in enumerate(sp):
            if n % 2 == 0:
                outer.append(i)
            else:
                inner.append(i)

        # Sadly, a regex won’t do it. Python’s re module does not
        # account for overlapping matches.
        matches = []
        for s in outer:
            for ci in range(len(s) - 2):
                if s[ci] == s[ci + 2] and s[ci + 1] != s[ci]:
                    matches.append((s[ci], s[ci + 1]))

        has_match = False
        for match in matches:
            bab = match[1] + match[0] + match[1]
            if any(bab in s for s in inner):
                has_match = True

        if has_match:
            count += 1

    return count


test_data = "aba[bab]xyz\nxyx[xyx]xyx\naaa[kek]eke\nzazbz[bzb]cdb"
test_output = solve(test_data)
test_expected = 3
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
