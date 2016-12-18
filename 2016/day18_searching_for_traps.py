#!/usr/bin/env python3
# Part 1: You got rank 818 on this star's leaderboard.
# Part 2: You got rank 803 on this star's leaderboard.

def solve(data, m):
    rows = [data]
    cols = len(data)
    for rown in range(1, m):
        previous = rows[-1]
        row = ""
        for i in range(cols):
            toptiles = []
            for n in (i - 1, i, i + 1):
                if n == -1 or n == cols:
                    toptiles.append('.')
                else:
                    toptiles.append(previous[n])

            # Check if tile is safe
            l, c, r = toptiles
            if (
                    (l == c == '^' and r == '.') or
                    (c == r == '^' and l == '.') or
                    (l == '^' and c == r == '.') or
                    (r == '^' and l == c == '.')
            ):
                # It’s a trap!
                row += '^'
            else:
                row += '.'
        rows.append(row)
    out = '\n'.join(rows)
    return out.count('.')


test_data = "..^^."
test_output = solve(test_data, 3)
test_expected = 6 # "..^^.\n.^^^^\n^^..^"
print(test_output, test_expected)
assert test_output == test_expected
# print(solve(".^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.", 40))
print(solve(".^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.", 400000))
