#!/usr/bin/python3
import hashlib
KEY = b"yzbqklnj"
i = 1
while True:
    d = hashlib.md5(KEY + str(i).encode('ascii')).hexdigest()
    #if d.startswith('00000'):
    if d.startswith('000000'):
        print(i)
        break
    i += 1
