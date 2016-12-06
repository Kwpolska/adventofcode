#!/usr/bin/env python3
import collections
PART = 2
IDX = 0 if PART == 1 else -1

with open("input/06.txt") as fh:
    file_data = fh.read()


def solve(data):
    words = [l for l in data.split('\n') if l]
    length = len(words[0])
    counters = []
    for i in range(length):
        counters.append(collections.Counter())
    for word in words:
        for i, c in enumerate(word):
            counters[i].update(c)
    output = ""
    for counter in counters:
        output += counter.most_common()[IDX][0]
    print(counters)
    return output


with open("input/test_06.txt") as tf:
    test_data = tf.read()
test_output = solve(test_data)
test_expected = "advent"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
