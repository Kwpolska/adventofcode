#!/usr/bin/env python3
from PIL import Image

POINT_COLORS = list(range(0, 250, 5))

with open("input/06.txt") as fh:
    file_data = fh.read().strip()


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(data, min_xy, max_xy, near):
    points = []
    nearest = {}
    candidates = []
    for l in data.split('\n'):
        points.append(tuple(int(i) for i in l.split(', ')))
    pc_map = {point: POINT_COLORS[i] for i, point in enumerate(points)}
    for x in range(min_xy, max_xy):
        print(x)
        for y in range(min_xy, max_xy):
            xy = (x, y)
            dst = []
            dst_sum = 0
            for p in points:
                # dst.append((p, manhattan(p, xy)))
                md = abs(p[0] - x) + abs(p[1] - y)
                dst.append((p, md))
                dst_sum += md
            if dst_sum < near:
                candidates.append(xy)
            min_dist = min(d[1] for d in dst)
            found = list(filter(lambda d: d[1] == min_dist, dst))
            if len(found) == 1:
                nearest[xy] = found[0][0]
            else:
                nearest[xy] = None

    img = Image.new('RGB', (max_xy, max_xy), color=(255, 255, 255))
    candidates_set = set(candidates)
    for x in range(min_xy, max_xy):
        for y in range(min_xy, max_xy):
            p = (x, y)
            nv = nearest.get(p)
            if nv is not None:
                red = 0
                green = pc_map[nv]
            else:
                red = 255
                green = 0
            blue = 255 if p in candidates_set else 0
            img.putpixel(p, (red, green, blue))
    for p in points:
        img.putpixel(p, (255, 255, 255))
    img.save("../out/task06.png")
    return len(candidates)


test_data = "1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9"
test_output = solve(test_data, 0, 10, 32)
test_expected = 16
print(test_output, test_expected)
assert test_output == test_expected
# print(solve(file_data, 0, 360, 10000))
print(solve(file_data, 0, 400, 10000))
