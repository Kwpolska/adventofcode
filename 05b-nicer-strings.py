#!/usr/bin/python
import string
import re
import time
NICE = 0
R = []
for l in string.ascii_lowercase:
    R.append(re.compile("{0}\w{0}".format(l)))

def test(s):
    #print(s)
    # 1a. Contains a pair that appears at least twice
    pairs = [''.join(i) for i in zip(s, s[1:])]
    seen = []
    f1a = False
    f1l = []
    for p in pairs:
        if p in seen:
            f1a = True
            f1l.append(p)
        else:
            seen.append(p)
    if not f1a:
        #print("- 1a")
        return False
    else:
        print(s)
        print("+ 1a {0}".format(f1l))
    # 1b. But cannot overlap
    for i in f1l:
        flag = 0
        for n, c in enumerate(s):
            if flag == 0 and c == i[0]:
                flag += 1
            elif flag == 1 and c == i[1]:
                flag = 0
                # found a pair. now let’s test others.
                try:
                    if s[n] + s[n + 1] in f1l:
                        print("- 1b")
                        return False
                except IndexError:
                    pass
    print("+ 1b")
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
