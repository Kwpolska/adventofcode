#!/usr/bin/env python3
with open("input/09.txt") as fh:
    file_data = fh.read()


def solve(data):
    data = data.strip()
    decrypted = ""
    while True:
        p = data.find("(")
        if p == -1:
            decrypted += data
            break
        else:
            decrypted += data[:p]
            data = data[p:]
            sp = data.find(")")
            parenthesis = data[:sp + 1][1:-1]
            data = data[sp + 1:]
            chars, times = (int(i) for i in parenthesis.split('x'))
            decrypted += data[:chars] * times
            data = data[chars:]

    print(decrypted)

    return len(decrypted)


test_data = "X(8x2)(3x3)ABCY"
test_output = solve(test_data)
test_expected = 18
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
