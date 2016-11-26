#!/usr/bin/python3
# While this could be done with eval(), I’m a better person than that.
L = 0
D = 0
with open('08-input.txt') as fh:
    for l in fh:
        data = l.strip()
        # Subtract all characters.
        literal = len(data)
        double = 2
        for ch in data:
            if ch in ['"', '\\']:
                double += 2
            else:
                double += 1

        L += literal
        D += double

print("L", L)
print("D", D)
print("-", D - L)
