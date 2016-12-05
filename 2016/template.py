#!/usr/bin/env python3
with open("input/💾.txt") as fh:
    file_data = fh.read()


def solve(data):
    return data


test_data = "📄"
test_output = solve(test_data)
test_expected = "🏁"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
