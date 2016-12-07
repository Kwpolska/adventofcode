#!/usr/bin/env python3
# Written on mobile — well, mostly. I mixed up inner and outer along the way,
# so I had to finish at a real computer.
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

        if any(re.search(r'([a-z])((?!\1)[a-z])\2\1', s) for s in inner):
            continue

        if any(re.search(r'([a-z])((?!\1)[a-z])\2\1', s) for s in outer):
            count += 1

    return count


test_data = "abba[mnop]qrst\nabcd[bddb]xyyx\naaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn"
test_output = solve(test_data)
test_expected = 2
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
