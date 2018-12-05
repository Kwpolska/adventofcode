#!/usr/bin/env python3
import string
with open("input/05.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    while True:
        out = data[0]
        lout = data[0].lower()
        for c in data[1:]:
            lc = c.lower()
            if lout and lout[-1] == lc and out[-1] != c:
                out = out[:-1]
                lout = lout[:-1]
            else:
                out += c
                lout += lc
        if out == data:
            break
        data = out
    return len(data), data


test_data = "dabAcCaCBAcCcaDA"
test_output = solve(test_data)
test_expected = (10, "dabCBAcaDA")
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
