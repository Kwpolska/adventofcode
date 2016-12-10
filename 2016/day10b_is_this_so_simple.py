#!/usr/bin/env python3
# You got rank 449 on this star's leaderboard.
from collections import defaultdict

with open("input/10_setup.txt") as fh:
    file_setup = fh.read().strip()

with open("input/10_moves.txt") as fh:
    file_moves = fh.read().strip()


def solve(setup, moves):
    output = {}
    bots = defaultdict(list)
    for l in setup.split('\n'):
        _, value, _, _, _, bot = l.split()
        bots[int(bot)].append(int(value))
    moves = moves.split('\n')
    while moves:
        moves2 = []
        for l in moves:
            _, bot, _, _, _, destL, valueL, _, _, _, destH, valueH = l.split()
            bot = int(bot)
            valueL = int(valueL)
            valueH = int(valueH)
            n = len(bots[bot])
            if n != 2:
                # print("Bot {0} has {1} chip(s), skipping".format(bot, n))
                moves2.append(l)
            else:
                low, high = sorted(bots[bot])
                bots[bot] = []
                if destL == "output":
                    output[valueL] = low
                else:
                    bots[valueL].append(low)

                if destH == "output":
                    output[valueH] = high
                else:
                    bots[valueH].append(high)
        moves = moves2

    # print(bots)
    return output[0] * output[1] * output[2]


test_data = ['value 5 goes to bot 2\nvalue 3 goes to bot 1\nvalue 2 goes to bot 2',
             'bot 2 gives low to bot 1 and high to bot 0\nbot 1 gives low to output 1 and high to bot 0\nbot 0 gives low to output 2 and high to output 0']
# test_output = solve(*test_data)
test_expected = ({0: 5, 1: 2, 2: 3}, {0: [], 1: [], 2: []})
# print(test_output, test_expected)
# assert test_output == test_expected
print(solve(file_setup, file_moves))
