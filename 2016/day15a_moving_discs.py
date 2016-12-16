#!/usr/bin/env python3
def solve(data):
    positions = []
    for idx, val in enumerate(data, 1):
        # Add the index to account for time passing.
        cycle = val[0]
        starting_rotation = (val[1] + idx) % cycle
        to_zero = (cycle - starting_rotation) % cycle
        print(idx, val, starting_rotation, to_zero)
        # The disc reaches position 0 at to_zero + n * cycle.
        rotations = set(range(to_zero, 10000000, cycle))
        positions.append(rotations)

    intersections = positions[0]
    for s in positions[1:]:
        intersections = intersections & s
    return (min(intersections))


# Input processed manually.
test_data = ((5, 4), (2, 1))
test_output = solve(test_data)
test_expected = 5
input_data = (
    (5, 2),
    (13, 7),
    (17, 10),
    (3, 2),
    (19, 9),
    (7, 0),
    (11, 0),  # Part 2
)
print(test_output, test_expected)
assert test_output == test_expected
print(solve(input_data))
