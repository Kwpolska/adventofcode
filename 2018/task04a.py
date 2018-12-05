#!/usr/bin/env python3
from collections import defaultdict

with open("input/04.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    data = sorted(data.split('\n'))  # this date format can be sorted lexicographically
    data = [l[1:].split('] ') for l in data]
    data = [(left[:-5], int(left[-2:]), left, right) for left, right in data]

    guard = None
    fallen_asleep = None
    minutes = {}
    asleep = {}
    for day, min, _, msg in data:
        if msg[0] == 'G':
            guard = int(msg.split(' ')[1][1:])
            if guard not in minutes:
                minutes[guard] = [0 for _ in range(60)]
                asleep[guard] = 0
            fallen_asleep = None
        elif msg[0] == 'f':
            fallen_asleep = min
        else:
            for m in range(fallen_asleep, min):
                minutes[guard][m] += 1
                asleep[guard] += 1

    sleepiest = max(asleep, key=lambda g: asleep[g])
    minute = max(enumerate(minutes[sleepiest]), key=lambda x: x[1])[0]

    return sleepiest * minute


test_data = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
test_output = solve(test_data)
test_expected = 240
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
