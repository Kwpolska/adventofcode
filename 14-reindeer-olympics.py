#!/usr/bin/python3
class Reindeer(object):
    # I feel like doing OOP today.
    name = "Santa"
    speed = 0
    fly_time = 0
    rest_time = 0
    distance = 0
    in_fly = 0
    in_rest = 0
    points = 0

    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
        self.in_fly = 0
        self.in_rest = 0
        self.distance = 0
        self.points = 0

REINDEERS = {}
# Read in reindeers!
with open("14-input.txt") as fh:
    for l in fh:
        name, can, fly, speed, non_si_unit, for_, fly_time, seconds, but, then, must, rest, for_, rest_time, seconds = l.strip().split()
        REINDEERS[name] = Reindeer(name, speed, fly_time, rest_time)

CURRENT_DISTANCE = {}

TIME = 0
while TIME < 2503:
    for r in REINDEERS.values():
        if r.in_fly < r.fly_time:
            r.distance += r.speed
            r.in_fly += 1
        else:
            r.in_rest += 1
        if r.in_rest == r.rest_time:
            r.in_fly = 0
            r.in_rest = 0
    for n, r in REINDEERS.items():
        print(n, r.distance)
    winner = max(REINDEERS.items(), key=lambda e: e[1].distance)
    winner[1].points += 1
    TIME += 1

RESULTS = sorted(REINDEERS.items(), key=lambda e: e[1].points)
for name, r in RESULTS:
    print(name, r.distance, r.points)
