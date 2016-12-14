#!/usr/bin/env python3
with open("input/14_hashes.txt") as fh:
    file_data = fh.read().strip()

data = {}
keys = []
out = []
for line in file_data.split('\n'):
    i, hash, m3, m5 = line.split(':')
    if m3:
        i = int(i)
        m3 = m3.split(',')[0]
        m5 = [x for x in m5.split(',') if x]
        keys.append(i)
        data[i] = (hash, m3, m5)

for key in keys:
    hash, m3, m5 = data[key]
    for newkey in range(key + 1, key + 1001):
        if newkey in data and m3 in data[newkey][2]:
            out.append(key)

print(out[63])
