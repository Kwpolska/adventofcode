#!/usr/bin/python3
import itertools
people = set()
pairs = {}
with open('13-input.txt') as fh:
    for l in fh:
        try:
            PERSON1, would, DESC, VALUE, happines, units, by, sitting, next, to, PERSON2 = l.strip().split()
        except:
            print(l)
            exit(1)
        VALUE = int(VALUE)
        if DESC == 'lose':
            VALUE = -VALUE
        # period
        PERSON2 = PERSON2[:-1]
        people.add(PERSON1)
        people.add(PERSON2)
        pairs[(PERSON1, PERSON2)] = VALUE

# Add self.
ME = "Chris"
for person in people:
    pairs[(ME, person)] = 0
    pairs[(person, ME)] = 0
people.add(ME)

people = list(people)
P = itertools.permutations(people)
SEATINGS = {}
for i in P:
    distance = 0
    # Check each entry separately.
    for n, self in enumerate(i):
        left = i[n - 1]
        try:
            right = i[n + 1]
        except IndexError:
            right = i[0]
        distance += pairs[(self, left)]
        distance += pairs[(self, right)]
    if distance != -1:
        SEATINGS[i] = distance
print(max(SEATINGS.values()))
