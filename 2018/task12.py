#!/usr/bin/env python3
with open("input/12.txt") as fh:
    file_data = fh.read().strip()


# a)
# ITER = 20
# b)
# ITER = 50000000000
ITER = 1000
# enough to see a pattern (the sums become a linear relation after some iterations)


def solve(data):
    lines = data.split('\n')
    init = lines[0].split()[-1]
    patterns_list = [line.split(' => ') for line in lines[2:] if line]
    patterns = dict(patterns_list)
    shift = 10000
    iter = ['.' for _ in range(shift)] + [i for i in init] + ['.' for _ in range(shift)]
    # iters = [iter]
    try:
        for num in range(1, ITER + 1):
            # if num % 10000 == 0: print('\r' + str(num), end='       ')
            new_iter = ['.' for _ in range(len(iter))]
            for idx in range(2, len(iter) - 2):
                box = iter[idx-2:idx+3]

                new_iter[idx] = patterns.get(''.join(box), '.')

            # iters.append(new_iter)
            iter = new_iter
            total = 0
            for idx, item in enumerate(iter):
                if item == '#':
                    total += idx - shift
            print(num, total)
    except KeyboardInterrupt:
        print(num, ''.join(iter))

    total = 0
    for idx, item in enumerate(iter):
        if item == '#':
            total += idx - shift
    return total


test_data = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""
# test_output = solve(test_data)
# test_expected = 325
# print(test_output, test_expected)
# assert test_output == test_expected
print(solve(file_data))
