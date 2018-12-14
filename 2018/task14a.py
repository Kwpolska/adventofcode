#!/usr/bin/env python3
AFTER = 10


def solve(dest):
    scores = [3, 7, 1, 0, 1, 0, 1, 2, 4, 5, 1, 5, 8, 9, 1, 6, 7, 7, 9, 2]
    first = 8
    second = 4
    for _ in range(dest - len(scores) + AFTER):
        new = scores[first] + scores[second]
        if new >= 10:
            scores.append(new // 10)
            scores.append(new % 10)
        else:
            scores.append(new)
        first = (first + 1 + scores[first]) % len(scores)
        second = (second + 1 + scores[second]) % len(scores)
    return ''.join(str(i) for i in scores[dest:dest + 10])


tests = [(9, '5158916779'), (5, '0124515891'), (18, '9251071085'), (2018, '5941429882')]

for test_data, test_expected in tests:
    test_output = solve(test_data)
    print(test_output, test_expected)
    assert test_output == test_expected
print(solve(110201))
