#!/usr/bin/env python3
import re
import attr
import pprint
import collections

re1 = re.compile(r'(.+) \((\d+)\)')
re2 = re.compile(r'(.+) \((\d+)\) -> (.+)')

@attr.s
class Node(object):
    name = attr.ib()
    weight = attr.ib()
    parent = attr.ib(default=None)
    child_names = attr.ib(default=attr.Factory(list))
    child_nodes = attr.ib(default=attr.Factory(list))


with open("input/07.txt") as fh:
    file_data = fh.read().strip()

def get_weight(node):
    child_weights = [get_weight(n) for n in node.child_nodes]
    if not child_weights:
        return node.weight
    if len(set(child_weights)) != 1:
        # Found the wrong one.
        right_weight = collections.Counter(child_weights).most_common()[0][0]
        wrong_weight = collections.Counter(child_weights).most_common()[-1][0]
        wrong_node = [n for n in node.child_nodes if get_weight(n) == wrong_weight][0]
        right_node = [n for n in node.child_nodes if get_weight(n) == right_weight][0]  # any
        # print(right_weight, wrong_weight, right_node.name, wrong_node.name)
        # Are children balanced?
        if len(set(get_weight(n) for n in wrong_node.child_nodes)) == 1:
            # Yes, parent is wrong
            # Using exceptions like goto. So sue me.
            raise ValueError(wrong_node.weight + (right_weight - wrong_weight))
        else:
            # No, a child is wrong
            raise Exception("Branch not implemented (not needed)")
    return sum(child_weights) + node.weight

def solve(data):
    nodes = {}
    for l in data.split('\n'):
        if '->' in l:
            name, weight, children = re2.findall(l)[0]
        else:
            name, weight = re1.findall(l)[0]
            children = ''
        child_names = list(filter(None, children.split(', ')))
        nodes[name] = Node(name, int(weight), child_names=child_names)
    for node in nodes.values():
        for cname in node.child_names:
            cnode = nodes[cname]
            node.child_nodes.append(cnode)
            cnode.parent = node

    top_node = [n for n in nodes.values() if n.parent is None][0]
    try:
        get_weight(top_node)
    except ValueError as e:
        return int(str(e))


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
test_expected = 60
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
