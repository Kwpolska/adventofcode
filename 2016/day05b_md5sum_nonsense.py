#!/usr/bin/env python3
# Repeat of 2015 day 4. I stole my own code from there.
import hashlib


def solve(data):
    answer = [''] * 8
    filled = 0
    i = 0
    while filled != 8:
        d = hashlib.md5(data + str(i).encode('ascii')).hexdigest()
        i += 1
        if d.startswith("00000"):
            print("Match", d[5])
            try:
                pos = int(d[5])
            except ValueError:
                continue  # ignore invalid position
            if pos == 8 or pos == 9:
                continue  # ignore invalid position
            elif answer[pos] != '':
                continue  # ignore repeat characters
            char = d[6]
            answer[pos] = char
            print(pos, char)
            filled += 1
    return ''.join(answer)


test_data = b"abc"
test_output = solve(test_data)
test_expected = "05ace8e3"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(b'abbhdwsy'))
