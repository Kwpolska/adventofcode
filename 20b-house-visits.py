#!/usr/bin/python3
# Idea stolen from /u/r_sreeram, /u/elguillaume — thanks!

from collections import defaultdict

houses = defaultdict(int)
INPUT = 36000000
N1 = int(INPUT / 10)

for elf in range(1, N1):
    visits = 0
    for visited in range(elf, N1, elf):
        houses[visited] += elf * 11
        visits += 1
        if houses[visited] >= INPUT or visits >= 50:
            break

print(min(i for i in houses if houses[i] >= INPUT))
