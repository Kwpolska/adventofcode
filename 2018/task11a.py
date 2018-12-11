#!/usr/bin/env python3
def solve(data):
    values = [[-1000 for _ in range(302)] for _ in range(302)]
    # squares = [[-1000 for _ in range(302)] for _ in range(302)]
    squares = {}
    for x in range(1, 301):
        for y in range(1, 301):
            v = ((x + 10) * y + data) * (x + 10)
            values[x][y] = v // 100 % 10 - 5
    for x in range(1, 299):  # last square is 298-299-300
        for y in range(1, 299):
            sq = 0
            for a in [0, 1, 2]:
                for b in [0, 1, 2]:
                    sq += values[x + a][y + b]
            squares[(x, y)] = sq

    xy, mv = max(squares.items(), key=lambda kv: kv[1])
    return xy, mv


test_data = [18, 42]
test_expected = [((33, 45), 29), ((21, 61), 30)]
for td, te in zip(test_data, test_expected):
    test_output = solve(td)
    print(test_output, te)
    assert test_output == te
print(solve(4842))
