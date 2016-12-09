#!/usr/bin/env python3
import re
import collections

REGEX = re.compile(r"([a-z-]+?)-(\d+)\[([a-z]{5})\]")

with open("input/04.txt") as fh:
    file_data = fh.read()


def solve(data):
    sum = 0
    for line in data.split('\n'):
        if not line:
            continue
        name, sector_id, checksum = REGEX.match(line).groups()

        letters = name.replace('-', '')
        c = collections.Counter(letters)
        cs = c.keys()
        cs = sorted(cs)
        cs = sorted(cs, key=lambda x: -c[x])
        if ''.join(cs[:5]) == checksum:
            # VALID
            key = int(sector_id) % 26  # less work to do
            decrypted = ""
            for char in name:
                if char == "-":
                    decrypted += " "
                else:
                    code = ord(char)
                    code = ((code - 0x61 + key) % 26) + 0x61
                    decrypted += chr(code)

            print(name, decrypted, sector_id)

    return sum


test_data = "aaaaa-bbb-z-y-x-123[abxyz]\na-b-c-d-e-f-g-h-987[abcde]\nnot-a-real-room-404[oarel]\ntotally-real-room-200[decoy]"
test_output = solve(test_data)
test_expected = 1514
# assert test_output == test_expected
print(solve(file_data))
