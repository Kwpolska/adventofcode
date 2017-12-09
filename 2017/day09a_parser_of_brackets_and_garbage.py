#!/usr/bin/env python3
with open("input/09.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    clean = ""
    in_garbage = False
    in_exclamation = False
    # Step 1: remove garbage.
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
            continue
        if c == '<':
            in_garbage = True
            continue
        clean += c

    # Step 2: count braces.
    score = 0
    total = 0
    for c in clean:
        if c == '{':
            score += 1
        if c == '}':
            total += score
            score -= 1
    return total


tests_data = ["{<a>,<a>,<a>,<a>}", "{{<a>},{<a>},{<a>},{<a>}}", "{{<!>},{<!>},{<!>},{<a>}}"]
tests_output = [solve(test_data) for test_data in tests_data]
tests_expected = [1, 9, 3]
for test_output, test_expected in zip(tests_output, tests_expected):
    print(test_output, test_expected)
    assert test_output == test_expected
print(solve(file_data))
