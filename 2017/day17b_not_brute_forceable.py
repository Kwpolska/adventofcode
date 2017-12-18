#!/usr/bin/env python3
import sys
def solve(data):
    # buffer = [0]
    position = 0
    after_zero = None
    for i in range(1, 50_000_000 + 1):
        if i % 5000 == 0:
            sys.stderr.write('\r' + str(i))
        position = (position + data) % i + 1
        # buffer.insert(position, i)
        if position == 1:
            after_zero = i
    # return buffer, buffer[buffer.index(0) + 1]
    sys.stderr.write('\n\n')
    return after_zero

test_data = 3
# test_output = solve(test_data)
# test_expected = 638
# print(test_output, test_expected)
# assert test_output == test_expected
print(solve(363))
