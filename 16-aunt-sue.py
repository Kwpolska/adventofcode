#!/usr/bin/python3
import re
LOOKING_FOR = {
    "perfumes": "1",
    "vizslas": "0",
    "cars": "2",
    "trees": "3",
    "samoyeds": "2",
    "cats": "7",
    "akitas": "0",
    "goldfish": "5",
    "pomeranians": "3",
    "children": "3"
}

R = re.compile("Sue (\d+): (.*)")
SUES = {}

with open("16-inputB.txt") as fh:
    for l in fh:
        l = l.strip()
        number, data = R.match(l).groups()
        number = int(number)
        datadict = {}
        for entry in data.split(", "):
            d = entry.split(": ")
            datadict[d[0]] = d[1]
        SUES[number] = datadict

CANDIDATES = {}
for number, data in SUES.items():
    match = True
    for k, v in data.items():
        if k not in LOOKING_FOR:
            continue
        if k in ['cats', 'trees']:
            test = LOOKING_FOR[k] < v
        elif k in ['pomeranians', 'goldfish']:
            test = LOOKING_FOR[k] > v
        else:
            test = LOOKING_FOR[k] == v
        if test:
            match = match and True
        else:
            match = False
    if match:
        CANDIDATES[number] = data

for number, data in CANDIDATES.items():
    print(number, data)
