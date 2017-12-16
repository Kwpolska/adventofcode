#!/usr/bin/env python3
with open("input/16.txt") as fh:
    file_data = fh.read().strip()


def solve(data, size=16):
    programs = []
    for i in range(size):
        programs.append(chr(0x61 + i))
    for move in data.split(','):
        ch, args = move[0], move[1:]
        if ch == 's':
            a = int(args)
            programs = programs[-a:] + programs[:-a]
        elif ch == 'x':
            aidx, bidx = map(int, args.split('/'))
            programs[aidx], programs[bidx] = programs[bidx], programs[aidx]
        elif ch == 'p':
            a, b = args.split('/')
            aidx, bidx = map(lambda x: programs.index(x), (a, b))
            programs[aidx], programs[bidx] = programs[bidx], programs[aidx]
        else:
            raise NotImplementedError()
    return ''.join(programs)


test_data = "s1,x3/4,pe/b"
test_output = solve(test_data, 5)
test_expected = "baedc"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
