#!/usr/bin/env python3
import string
with open("input/05.txt") as fh:
    file_data = fh.read().strip()


def run_iter(data):
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
    return len(data)


def solve(data):
    lengths = [run_iter(data)]
    for lc in string.ascii_lowercase:
        uc = lc.upper()
        data_ = data.replace(uc, '').replace(lc, '')
        lengths.append(run_iter(data_))
    return min(lengths)


test_data = "dabAcCaCBAcCcaDA"
test_output = solve(test_data)
test_expected = 4
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
