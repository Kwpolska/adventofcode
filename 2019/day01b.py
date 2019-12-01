#!/usr/bin/env python3
with open("input/01.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    total = 0
    for i in map(int, data.split()):
        while True:
            i = i // 3 - 2
            if i <= 0:
                break
            total += i

    return total


test_data = "12\n14\n1969\n100756"
test_output = solve(test_data)
test_expected = 2 + 2 + 966 + 50346
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
