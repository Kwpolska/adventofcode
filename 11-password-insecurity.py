#!/usr/bin/python3
import string
import re
pwd = "hxbxwxba"
WRAP = "{"  # ord('z') + 1
triplets = zip(string.ascii_lowercase, string.ascii_lowercase[1:], string.ascii_lowercase[2:])
striplets = [''.join(i) for i in triplets]

def validate(pwd):
    # 1. password must include one increasing straight of at least three
    #    letters, like abc, bcd, cde, …, xyz
    if any(i in pwd for i in striplets):
        pass
    else:
        return False
    # 2. passwords may not contain the letters i, o, or l
    if 'i' in pwd or 'o' in pwd or 'l' in pwd:
        return False
    # 3. passwords must contain at least two different, non-overlapping pairs of
    #    letters, like aa, bb, or zz.
    # Stolen from /u/knipil, because I needed a better idea.
    return not len(re.findall(r'([a-z])\1', pwd)) < 2


def increment(pwd):
    p = list(reversed(pwd))
    newp = []
    wraparound = True
    for char in p:
        if wraparound:
            char = chr(ord(char) + 1)
            if char == WRAP:
                char = 'a'
                wraparound = True
            else:
                wraparound = False
        newp.append(char)
    if wraparound:
        # if we exceed the 8th character
        return increment(pwd)

    return ''.join(reversed(newp))

found = 0
while found != 2:
    pwd = increment(pwd)
    if validate(pwd):
        print(pwd)
        found += 1
