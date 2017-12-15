#!/usr/bin/env python3

from day10b_crappy_crypto import solve_bin as knot_cipher

def solve(data):
    squares = 0
    for i in range(0, 128):
        hash_input = f"{data}-{i}"
        hash = knot_cipher(hash_input)
        squares += hash.count('1')
    return squares


test_data = "flqrgnkx"
test_output = solve(test_data)
test_expected = 8108
print(test_output, test_expected)
assert test_output == test_expected
print(solve("hwlqcszp"))
