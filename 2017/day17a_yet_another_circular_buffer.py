#!/usr/bin/env python3
def solve(data):
    buffer = [0]
    position = 0
    for i in range(1, 2017 + 1):
        position = (position + data) % len(buffer) + 1
        buffer.insert(position, i)
    return buffer[position + 1]


test_data = 3
test_output = solve(test_data)
test_expected = 638
print(test_output, test_expected)
assert test_output == test_expected
print(solve(363))
