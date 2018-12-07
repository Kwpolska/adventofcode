#!/usr/bin/env python3
import collections

with open("input/06.txt") as fh:
    file_data = fh.read().strip()


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(data, min_xy, max_xy):
    points = []
    nearest = {}
    for l in data.split('\n'):
        points.append(tuple(int(i) for i in l.split(', ')))
    for x in range(min_xy, max_xy):
        print(x)
        for y in range(min_xy, max_xy):
            xy = (x, y)
            dst = []
            for p in points:
                # dst.append((p, manhattan(p, xy)))
                md = abs(p[0] - x) + abs(p[1] - y)  # manhattan(p, xy)
                dst.append((p, md))
            min_dist = min(d[1] for d in dst)
            found = list(filter(lambda d: d[1] == min_dist, dst))
            if len(found) == 1:
                nearest[xy] = found[0][0]
            else:
                nearest[xy] = None
    # banned points are on the edges
    banned = {None}
    for p in range(min_xy, max_xy):
        banned.add(nearest[(p, min_xy)])
        banned.add(nearest[(min_xy, p)])
        banned.add(nearest[(p, max_xy - 1)])
        banned.add(nearest[(max_xy - 1, p)])
    c = collections.Counter(nearest.values())
    for p, count in c.most_common():
        if p not in banned:
            return count

    return data


test_data = "1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9"
test_output = solve(test_data, 0, 10)
test_expected = 17
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data, 40, 360))
