#!/usr/bin/env python3
import attr
import operator
from typing import List, Tuple, Dict

import sys

with open("input/13.txt") as fh:
    file_data = fh.read().strip()

TOP = -1
BOTTOM = 1


@attr.s
class Layer:
    number = attr.ib(0)
    range = attr.ib(0)
    position = attr.ib(0)
    direction = attr.ib(BOTTOM)

    def step(self) -> None:
        if self.range is None:
            return
        self.position += self.direction
        if self.position >= (self.range - 1) or self.position == 0:
            self.direction *= -1

    def check(self) -> int:
        if self.range is None or self.position != 0:
            return 0
        return 1


def solve(data):
    layer_info: List[Tuple[int]] = [tuple(map(int, line.split(': '))) for line in data.split('\n')]
    max_layer: int = max(layer_info, key=operator.itemgetter(0))[0]
    li_dict: Dict[int, int] = dict(layer_info)
    layers: List[Layer] = []

    # Create layers
    for i in range(max_layer + 1):
        lrange: int = li_dict.get(i)
        if lrange is not None:
            layers.append(Layer(i, lrange))
        else:
            layers.append(Layer(i, None))

    wait = 0
    failure = 1
    layers_current = [attr.evolve(l) for l in layers]  # hacky
    while failure > 0:
        sys.stderr.write(f"\r{wait}")
        wait += 1
        failure = 0

        for l in layers_current:
            l.step()
        layers_test = [attr.evolve(l) for l in layers_current]  # one more copy

        for i in range(max_layer + 1):
            failure += layers_test[i].check()
            if failure: continue
            for l in layers_test:
                l.step()
    print("\n")

    return wait


test_data = "0: 3\n1: 2\n4: 4\n6: 4"
test_output = solve(test_data)
test_expected = 10
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
