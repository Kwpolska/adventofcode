#!/usr/bin/env python3
import operator
with open("input/08.txt") as fh:
    file_data = fh.read().strip()

ops = {
    '==': operator.eq,
    '!=': operator.ne,
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
}

words = {
    'inc': 1,
    'dec': -1
}


def solve(data):
    lines = [line.split(' ') for line in data.split('\n')]
    registers = {}
    max_val = 0
    # pass 1, find registers
    for line in lines:
        dest, word, arg, if_, src, cmp, val = line
        registers[dest] = 0
        registers[src] = 0
    for line in lines:
        dest, word, arg, if_, src, cmp, val = line
        # Check condition
        val = int(val)
        arg = int(arg)
        if ops[cmp](registers[src], val):
            registers[dest] += words[word] * arg
        max_val = max(max_val, max(registers.values()))

    return max_val


test_data = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
test_output = solve(test_data)
test_expected = 10
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
