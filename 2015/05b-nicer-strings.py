#!/usr/bin/python
import string
import re
NICE = 0
R = []
for l in string.ascii_lowercase:
    R.append(re.compile("{0}\w{0}".format(l)))

def test(s):
    print(s)
    # 1. Contains a pair that appears at least twice, but cannot overlap
    f1 = False
    # "borrowed" from /u/C0urante: https://www.reddit.com/r/adventofcode/comments/3viazx/day_5_solutions/cxnswjz
    # (previous solution used zip(), which was apparently wrong)
    for i in range(len(s) - 3):
        pair = s[i:i + 2]
        next = s[i + 2:]
        if pair in next:
            f1 = True
    if not f1:
        return False
    # 2. One letter which repeats with exactly one letter in between
    for r in R:
        m = r.search(s)
        if m:
            print("+ 2 {0}".format(m.group()))
            return True
    print("- 2")
    return False

#test('aabcdefgaa')

with open('05-input.txt') as fh:
    for s in fh.readlines():
        NICE += int(test(s.strip()))
print(NICE)
