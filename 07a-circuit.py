#!/usr/bin/python3
import operator
wires = {}
queue = []
operations = {
    'AND': operator.and_,
    'OR': operator.or_,
    'NOT': operator.invert,
    #'XOR': operator.xor,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift
}

def parse(expr, dest):
    if ' ' not in expr:
        if expr.isdigit():
            wires[dest] = int(expr)
        else:
            try:
                wires[dest] = wires[expr]
            except KeyError:
                queue.append((expr, dest))
                return
    else:
        if expr.startswith('NOT'):
            oper, op1 = expr.split()
            op2 = '0'
        else:
            op1, oper, op2 = expr.split()

        if op1.isdigit():
            op1 = int(op1)
        else:
            try:
                op1 = wires[op1]
            except KeyError:
                queue.append((expr, dest))
                return

        if op2.isdigit():
            op2 = int(op2)
        else:
            try:
                op2 = wires[op2]
            except KeyError:
                queue.append((expr, dest))
                return
        if oper == 'NOT':
            wires[dest] = operations[oper](op1)
        else:
            wires[dest] = operations[oper](op1, op2)

with open('07-input.txt') as fh:
    for l in fh:
        for i in range(0, len(queue)):
            parse(*queue.pop(0))
        expr, dest = l.strip().split(' -> ')
        parse(expr, dest)
while queue:
    parse(*queue.pop(0))
print(wires)
print(wires['a'])
