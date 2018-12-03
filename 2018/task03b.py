#!/usr/bin/env python3
import re
REGEX = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
with open("input/03.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    claimants = {}
    ids = set()
    banned_ids = set()
    for l in data.split('\n'):
        id, top, left, w, h = [int(i) for i in REGEX.match(l).groups()]
        ids.add(id)
        for x in range(top, w + top):
            for y in range(left, h + left):
                point = (x, y)
                claimants[point] = claimants.get(point, []) + [id]
    for point, claimant_ids in claimants.items():
        if len(claimant_ids) > 1:
            banned_ids.update(set(claimant_ids))
    return ids - banned_ids


test_data = "#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2"
test_output = solve(test_data)
test_expected = {3}
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
