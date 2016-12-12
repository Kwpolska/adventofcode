#!/usr/bin/env python3
with open("input/12.txt") as fh:
    file_data = fh.read().strip()


def int_or_register(x, r):
    try:
        return int(x)
    except ValueError:
        return r[x]


def solve(data):
    # 'c' is 0 in part one and 1 in part two
    r = {"a": 0, "b": 0, "c": 1, "d": 0}
    rip = 0
    lines = [i.split() for i in data.split('\n')]
    while True:
        try:
            line = lines[rip]
        except IndexError:
            return r['a']
        instruction = line[0]
        x = line[1]
        try:
            y = line[2]
        except IndexError:
            y = None
        if instruction == 'cpy':
            r[y] = int_or_register(x, r)
        elif instruction == 'inc':
            r[x] += 1
        elif instruction == 'dec':
            r[x] -= 1
        elif instruction == 'jnz':
            if int_or_register(x, r) != 0:
                rip += int(y)
            else:
                rip += 1
        if instruction != 'jnz':
            rip += 1
        #print(rip, line, r)
    return r['a']


test_data = "cpy 41 a\ninc a\ninc a\ndec a\njnz a 2\ndec a"
test_output = solve(test_data)
test_expected = 42
print(test_output, test_expected)
#assert test_output == test_expected
print(solve(file_data))
