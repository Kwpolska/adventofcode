#!/usr/bin/env python3
AFTER = 10


def solve(dest):
    target = [int(i) for i in dest]
    LT = len(target)
    scores = [3, 7, 1, 0, 1, 0, 1, 2, 4, 5, 1, 5, 8, 9, 1, 6, 7, 7, 9, 2]
    first = 8
    second = 4
    ls = len(scores)
    while True:
        new = scores[first] + scores[second]
        if new >= 10:
            scores.append(new // 10)
            ls += 1
            if scores[-LT:] == target:
                return ls - LT
            scores.append(new % 10)
        else:
            scores.append(new)
        ls += 1
        first = (first + 1 + scores[first]) % ls
        second = (second + 1 + scores[second]) % ls
        if scores[-LT:] == target:
            print('\n\n\n')
            return ls - LT
        if ls % 10000 == 0: print('\r' + str(ls) + '       ', end='')


tests = [('92510', 18), ('59414', 2018)]

for test_data, test_expected in tests:
    test_output = solve(test_data)
    print(test_output, test_expected)
    assert test_output == test_expected
print(solve('110201'))
