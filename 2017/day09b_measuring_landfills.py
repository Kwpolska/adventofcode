#!/usr/bin/env python3
with open("input/09.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    count = 0
    in_garbage = False
    in_exclamation = False
    for c in data:
        if in_exclamation:
            in_exclamation = False
            continue
        if c == '!':
            in_exclamation = True
            continue
        if c == '>':
            in_garbage = False
            continue
        if in_garbage:
            count += 1
            continue
        if c == '<':
            in_garbage = True
            continue
    return count


tests_data = ["{<a>,<a>,<a>,<a>}", "{{<a>},{<a>},{<a>},{<a>}}", "{{<!>},{<!>},{<!>},{<a>}}"]
tests_output = [solve(test_data) for test_data in tests_data]
tests_expected = [4, 4, 13]
for test_output, test_expected in zip(tests_output, tests_expected):
    print(test_output, test_expected)
    assert test_output == test_expected
print(solve(file_data))
