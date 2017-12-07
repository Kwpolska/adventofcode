#!/usr/bin/env python3
import re
import attr

re1 = re.compile(r'(.+) \((\d+)\)')
re2 = re.compile(r'(.+) \((\d+)\) -> (.+)')

@attr.s
class Node(object):
    name = attr.ib()
    weight = attr.ib()
    parent = attr.ib(default=None)
    children_names = attr.ib(default=attr.Factory(list))
    children_nodes = attr.ib(default=attr.Factory(list))


with open("input/07.txt") as fh:
    file_data = fh.read().strip()


def solve(data):
    nodes = {}
    for l in data.split('\n'):
        if '->' in l:
            name, weight, children = re2.findall(l)[0]
        else:
            name, weight = re1.findall(l)[0]
            children = ''
        children_names = list(filter(None, children.split(', ')))
        nodes[name] = Node(name, weight, children_names=children_names)
    for node in nodes.values():
        for cname in node.children_names:
            cnode = nodes[cname]
            node.children_nodes.append(cnode)
            cnode.parent = node

    return [n for n in nodes.values() if n.parent is None][0].name


test_data = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
test_output = solve(test_data)
test_expected = "tknk"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
