#!/usr/bin/env python3
from __future__ import annotations
from typing import List
from dataclasses import dataclass, field

with open("input/08.txt") as fh:
    file_data = fh.read().strip()


@dataclass()
class Node:
    children: List[Node] = field(default_factory=list)
    meta: List[int] = field(default_factory=list)


def parse(data: List[int]) -> Node:
    n = Node()
    children = data.pop(0)
    meta = data.pop(0)
    for _ in range(children):
        n.children.append(parse(data))
    for _ in range(meta):
        n.meta.append(data.pop(0))
    return n


def get_value(node: Node) -> int:
    if node.children:
        total = 0
        for idx in node.meta:
            # WHY ONE-INDEXED?!
            if 1 <= idx <= len(node.children):
                total += get_value(node.children[idx - 1])
        return total
    else:
        return sum(node.meta)


def solve(data: str) -> int:
    root: Node = parse(list(int(i) for i in data.split()))
    return get_value(root)


test_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
test_output = solve(test_data)
test_expected = 66
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
