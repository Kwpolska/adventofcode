#!/usr/bin/env python3
# 16b1_auto: figure out opcode meaning
import json
from typing import Dict, List

input_data = """addr [6, 12, 15]
addi [4, 6, 12, 15]
mulr [6]
muli [5, 6, 12, 15]
banr [0, 4, 5, 6, 10, 11]
bani [0, 5, 6, 8, 10, 11, 12]
borr [6, 12]
bori [4, 6, 10, 12]
setr [2, 4, 6, 10, 12]
seti [0, 4, 6, 12, 15]
gtir [0, 2, 3, 5, 6, 8, 11, 12]
gtri [0, 3, 4, 6, 7, 8, 9, 11, 12]
gtrr [0, 3, 5, 6, 7, 8, 11, 12]
eqir [0, 1, 3, 4, 5, 7, 8, 9, 11, 12]
eqri [0, 1, 3, 5, 7, 8, 11, 12, 13]
eqrr [0, 1, 3, 5, 8, 9, 11, 13, 14]"""

d: Dict[str, List[int]] = {}

for l in input_data.split('\n'):
    instruction, possibilities = l[:4], json.loads(l[5:])
    d[instruction] = possibilities

seen = 0
instructions: Dict[int, str] = {i: None for i in range(16)}

while seen < 16:
    instruction: str
    possibilities: List[int]
    for instruction, possibilities in d.items():
        if len(possibilities) == 1:
            seen += 1
            found = possibilities[0]
            instructions[found] = instruction
            print(instruction, '=', found)
            del d[instruction]
            for poslist in d.values():
                if found in poslist:
                    poslist.remove(found)
            break

print("\n{")
print(",\n".join(f"    {i}: {instructions[i]}" for i in range(16)))
print("}")
