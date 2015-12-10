#!/usr/bin/python3
IN = ["1113222113"]
def parse(i):
    sequences = [[1, i[0]]]
    for c in i[1:]:
        if c == sequences[-1][1]:
            sequences[-1][0] += 1
        else:
            sequences.append([1, c])
    o = ""
    for c, s in sequences:
        o += str(c)
        o += str(s)
    return o

for i in range(50):
    IN.append(parse(IN[-1]))

print(len(IN[-1]))
