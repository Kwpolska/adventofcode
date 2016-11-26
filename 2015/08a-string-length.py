#!/usr/bin/python3
# While this could be done with eval(), I’m a better person than that.
L = 0
M = 0
with open('08-input.txt') as fh:
    for l in fh:
        data = l.strip()
        # Subtract all characters.
        literal = len(data)
        memory = 0
        # 0 = ordinary, 1 = backslash, 2 = x
        flag = 0
        for ch in data[1:-1]:
            if flag == 0 and ch == '\\':
                flag = 1
            elif flag == 1 and ch == 'x':
                flag = 2
            elif flag == 2:
                flag = 3
            elif flag == 3:
                flag = 0
                memory += 1
            elif flag == 1:
                flag = 0
                memory += 1
            else:
                memory += 1

        L += literal
        M += memory

print("L", L)
print("M", M)
print("-", L - M)
