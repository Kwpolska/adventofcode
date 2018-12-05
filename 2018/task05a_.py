#!/usr/bin/env python3
with open("input/05.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    out = ""
    buf = ""
    while len(data) > 10:
        for c in data:
            if buf:
                if buf.lower() == c.lower() and buf != c:
                    # skip
                    buf = ''
                else:
                    out += buf
                    buf = c
            else:
                buf = c
        data = out + buf
        out = ""
        buf = ""
        print(len(data), data)
    return data


test_data = "dabAcCaCBAcCcaDA"
test_output = solve(test_data)
test_expected = "dabCBAcaDA"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
