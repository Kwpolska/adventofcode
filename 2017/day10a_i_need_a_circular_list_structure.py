#!/usr/bin/env python3
with open("input/10.txt") as fh:
    file_data = fh.read().strip()


def solve(data, size=256):
    lengths = [int(i) for i in data.split(',')]
    L = list(range(0, size))
    current = 0
    skip = 0

    for length in lengths:
        # print("start", length, L, L[current])
        # Select as many as possible.
        right = L[current:current+length]
        right_l = len(right)
        # And the overflow.  The maximum length is <= size
        overflow, overflow_l = [], 0
        if right_l < length:
            overflow = L[0:length - right_l]
            overflow_l = len(overflow)
        assert overflow_l + right_l == length

        sum = right + overflow
        sum.reverse()

        # Insert back into the list.
        new_right = sum[0:right_l]
        new_overflow = sum[right_l:]
        assert len(new_right) == right_l and len(new_overflow) == overflow_l
        L[current:current+length] = new_right
        L[0:length - right_l] = new_overflow

        # Push indexes forward.
        current = (current + length + skip) % size
        skip += 1

        # print("end  ", length, L)

    return L[0] * L[1]


test_data = "3,4,1,5"
test_output = solve(test_data, 5)
test_expected = 12
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
