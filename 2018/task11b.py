#!/usr/bin/env python3
def solve(data):
    values = [[-1000 for _ in range(302)] for _ in range(302)]
    # squares = [[-1000 for _ in range(302)] for _ in range(302)]
    squares = {}
    for x in range(1, 301):
        for y in range(1, 301):
            v = ((x + 10) * y + data) * (x + 10)
            values[x][y] = v // 100 % 10 - 5
    best = (0, 0, 0)
    best_value = 0
    for s in range(1, 21):
        # from megathread: correct answer tends to be <20, since most of the grid is negative
        print(s)
        for x in range(1, 302 - s):
            for y in range(1, 302 - s):
                sq = 0
                for a in range(s):
                    for b in range(s):
                        sq += values[x + a][y + b]
                if sq > best_value:
                    best = (x, y, s)
                    best_value = sq

    return best


# test_data = [18, 42]
# test_expected = [(90, 269, 16)]
# for td, te in zip(test_data, test_expected):
    # test_output = solve(td)
    # print(test_output, te)
    # assert test_output == te
print(solve(4842))
