#!/usr/bin/env python3


class Marble:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert_after(self, value: int):
        new = Marble(value)
        new.left = self
        new.right = self.right
        self.right.left = new
        self.right = new
        return new

    def remove(self):
        self.right.left = self.left
        self.left.right = self.right

    def __str__(self):
        return str(self.value)


def go_left(marble: Marble, number: int) -> Marble:
    for _ in range(number):
        marble = marble.left
    return marble


def solve(elves, last_marble):
    # first two turns done by hand
    zero = Marble(0); one = Marble(1); two = Marble(2)
    zero.left = one; zero.right = two
    two.left = zero; two.right = one
    one.left = two; one.right = zero
    current_marble: Marble = two
    elf_scores = {i: 0 for i in range(elves)}
    for next_marble in range(3, last_marble + 1):
        if next_marble % 23 == 0:
            current_elf = (next_marble - 1) % elves
            elf_scores[current_elf] += next_marble
            deleted = go_left(current_marble, 7)
            current_marble = deleted.right
            deleted.remove()
            elf_scores[current_elf] += deleted.value
        else:
            current_marble = current_marble.right.insert_after(next_marble)
        if elves == 9:
            current_elf = (next_marble - 1) % elves
            print(f"[{current_elf + 1}]", end='')
            cm = zero
            while True:
                if cm == current_marble:
                    print(f" \033[32m{cm.value}\033[0m", end='')
                else:
                    print(f" {cm.value}", end='')
                cm = cm.right
                if cm == zero:
                    break
            print()

    return max(elf_scores.values())


tests_data = [(9, 25), (10, 1618), (13, 7999), (17, 1104), (21, 6111), (30, 5807)]
tests_output = [solve(*test_data) for test_data in tests_data]
tests_expected = [32, 8317, 146373, 2764, 54718, 37305]
for test_output, test_expected in zip(tests_output, tests_expected):
    print(test_output, test_expected)
    assert test_output == test_expected
print('PART 1:', solve(441, 71032))
print('PART 2:', solve(441, 71032 * 100))
