#!/usr/bin/env python3
with open("input/💾.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    return data


tests_data = ["📄1", "📄2"]
tests_output = [solve(test_data) for test_data in tests_data]
tests_expected = ["🏁1", "🏁2"]
for test_output, test_expected in zip(tests_output, tests_expected):
    print(test_output, test_expected)
    assert test_output == test_expected
print(solve(file_data))
