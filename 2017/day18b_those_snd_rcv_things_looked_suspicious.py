#!/usr/bin/env python3
# Some ideas (and debugging hint) stolen from https://www.reddit.com/r/adventofcode/comments/7kj35s/2017_day_18_solutions/dreth75/
from collections import defaultdict, deque
with open("input/18.txt") as fh:
    file_data = fh.read().strip()


def p(arg, registers):
    if isinstance(arg, int):
        return arg
    return registers[arg]

def other(i):
    return int(not i)

def solve(data):
    instructions_raw = data.split('\n')
    instructions = []
    for line in instructions_raw:
        parsed = line.split()
        instruction, args = parsed[0], parsed[1:]
        args2 = []
        for a in args:
            try:
                args2.append(int(a))
            except ValueError:
                args2.append(a)
        instructions.append((instruction, args2))

    state = {
        0: {
            'rip': 0,
            'registers': defaultdict(int, p=0),
            'outgoing': deque(),
            'is_rcv': False,
            'is_running': True,
        },
        1: {
            'rip': 0,
            'registers': defaultdict(int, p=1),
            'outgoing': deque(),
            'is_rcv': False,
            'is_running': True,
        }
    }
    program = 0
    pstate = state[0]
    linstr = len(instructions)
    sent_1_values = 0
    while True:
        instruction, args = instructions[pstate['rip']]
        # print(instruction, args)
        if instruction == 'snd':
            if program == 1:
                sent_1_values += 1
            pstate['outgoing'].append(p(args[0], pstate['registers']))
        elif instruction == 'set':
            pstate['registers'][args[0]] = p(args[1], pstate['registers'])
        elif instruction == 'add':
            pstate['registers'][args[0]] += p(args[1], pstate['registers'])
        elif instruction == 'mul':
            pstate['registers'][args[0]] *= p(args[1], pstate['registers'])
        elif instruction == 'mod':
            pstate['registers'][args[0]] %= p(args[1], pstate['registers'])
        elif instruction == 'rcv':
            other_state = state[other(program)]
            other_queue = other_state['outgoing']
            if other_queue:
                pstate['is_rcv'] = False
                value = other_queue.popleft()
                pstate['registers'][args[0]] = value
            elif not other_state['is_running']:
                # Deadlock.
                return sent_1_values
            elif not pstate['outgoing'] and other_state['is_rcv']:
                # Deadlock.
                return sent_1_values
            else:
                # Can context switch.
                pstate['is_rcv'] = True
                old_state = pstate
                program = other(program)
                pstate = state[program]
                # print(sent_1_values, "Context switch", old_state, "→", pstate)
                pstate['rip'] -= 1
        elif instruction == 'jgz':
            if p(args[0], pstate['registers']) > 0:
                pstate['rip'] += p(args[1], pstate['registers'])
                pstate['rip'] -= 1
        pstate['rip'] += 1

        if not 0 <= pstate['rip'] < linstr:
            if not state[other(program)]['is_running']:
                return sent_1_values
            pstate['is_running'] = False

            # swap back since other program's not done
            program = other(program)
            pstate = state[program]


test_data = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

test_output = solve(test_data)
test_expected = 3
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
