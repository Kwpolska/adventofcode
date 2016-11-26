#!/usr/bin/python3
import itertools
places = set()
pairs = {}
with open('09-input.txt') as fh:
    for l in fh:
        place1, _, place2, _, distance = l.strip().split()
        distance = int(distance)
        places.add(place1)
        places.add(place2)
        pairs[(place1, place2)] = distance
        pairs[(place2, place1)] = distance
places = list(places)
P = itertools.permutations(places)
ROUTES = {}
for i in P:
    distance = 0
    # Check each entry separately.
    for n in range(len(i) - 1):
        try:
            distance += pairs[(i[n], i[n + 1])]
        except KeyError:
            distance = -1
            break
    if distance != -1:
        ROUTES[i] = distance
print(min(ROUTES.values()))
print(max(ROUTES.values()))
