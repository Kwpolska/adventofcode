#!/usr/bin/env python3
import sys
with open("input/16.txt") as fh:
    file_data = fh.read().strip()

SWAP = 1
EXCHANGE = 2
PARTNER = 4

def solve(data, size=16):
    programs = []
    moves = []
    seen = []
    for i in range(size):
        programs.append(chr(0x61 + i))
    for move in data.split(','):
        ch, args = move[0], move[1:]
        if ch == 's':
            a = int(args)
            moves.append((SWAP, a))
        elif ch == 'x':
            aidx, bidx = map(int, args.split('/'))
            moves.append((EXCHANGE, aidx, bidx))
        elif ch == 'p':
            a, b = args.split('/')
            moves.append((PARTNER, a, b))
        else:
            raise NotImplementedError()

    for i in range(1000000000):
        sys.stderr.write(f'\r{i}')
        # optimization idea from /u/simonsrealaccount
        # https://www.reddit.com/r/adventofcode/comments/7k572l/2017_day_16_solutions/drboovu/
        state = ''.join(programs)
        if state in seen:
            print(seen)
            return seen[1000000000 % i]
        seen.append(state)

        for move in moves:
            if move[0] & SWAP:
                # print(move)
                a = move[1]
                programs = programs[-a:] + programs[:-a]
            elif move[0] & EXCHANGE:
                aidx, bidx = move[1], move[2]
                programs[aidx], programs[bidx] = programs[bidx], programs[aidx]
            elif move[0] & PARTNER:
                a, b = move[1], move[2]
                aidx, bidx = map(lambda x: programs.index(x), (a, b))
                programs[aidx], programs[bidx] = programs[bidx], programs[aidx]
            else:
                raise NotImplementedError()
    sys.stderr.write('\n\n')
    return ''.join(programs)


# test_data = "s1,x3/4,pe/b"
# test_output = solve(test_data, 5)
# test_expected = "baedc"
# print(test_output, test_expected)
# assert test_output == test_expected
print(solve(file_data))
