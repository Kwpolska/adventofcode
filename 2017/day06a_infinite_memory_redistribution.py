#!/usr/bin/env python3
def solve(data):
    state = [int(i) for i in data.split()]
    seen = set()
    steps = 0
    while tuple(state) not in seen:
        seen.add(tuple(state))
        # Pick largest index.
        to_redist = max(state)
        i = state.index(to_redist)  # first (avoids collisions)
        state[i] = 0
        i += 1
        while to_redist:
            if i >= len(state):
                i = 0
            state[i] += 1
            to_redist -= 1
            i += 1
        steps += 1
    return steps


test_data = "0 2 7 0"
test_output = solve(test_data)
test_expected = 5
print(test_output, test_expected)
assert test_output == test_expected
print(solve("0 5 10 0 11 14 13 4 11 8 8 7 1 4 12 11"))
