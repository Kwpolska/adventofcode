#!/usr/bin/env python3
from typing import Dict, List, Set
import attr
with open("input/12.txt") as fh:
    file_data = fh.read().strip()


@attr.s(hash=True)
class Program(object):
    name: str = attr.ib(str)
    connections_str: List[str] = attr.ib(attr.Factory(list), hash=False)
    connections: 'List[Program]' = attr.ib(attr.Factory(list), hash=False)


def find_connections(program: Program, found_connections: Set[Program]):
    found_connections.add(program)
    for p in program.connections:
        if p in found_connections:
            continue
        find_connections(p, found_connections)
    return found_connections


def solve(data):
    programs: Dict[Program] = {}
    for line in data.split('\n'):
        l, r = line.split(' <-> ')
        rl = r.split(', ')
        programs[l] = Program(l, rl)

    for p in programs.values():
        for conn in p.connections_str:
            p2: Program = programs[conn]
            p.connections.append(p2)
            p2.connections.append(p)

    all_groups = set()
    for p in programs.values():
        found_connections: Set[Program] = set()
        find_connections(p, found_connections)
        all_groups.add(frozenset(found_connections))

    return len(all_groups)


test_data = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""
test_output = solve(test_data)
test_expected = 2
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
