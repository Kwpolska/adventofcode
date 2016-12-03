#!/usr/bin/env python3
with open("input/03.txt") as fh:
    file_data = fh.read()


def solve(data):
    possible = 0
    table = []
    for line in data.split('\n'):
        if not line:
            continue
        table.append([int(i) for i in line.split()])
    print(table)
    for col in (0, 1, 2):
        for row in range(0, len(table), 3):
            a, b, c = table[row][col], table[row + 1][col], table[row + 2][col]
            if (a + b) > c and (a + c) > b and (b + c) > a:
                possible += 1

    return possible


# test_data = "5 10 25"
# test_output = solve(test_data)
# test_expected = 0
# assert test_output == test_expected
print(solve(file_data))
