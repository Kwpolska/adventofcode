#!/usr/bin/python3
import json
with open('12-input.txt') as fh:
    j = json.load(fh)

def s(o):
    SUM = 0
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "red" or v == "red":
                return 0
            elif isinstance(v, list) or isinstance(v, dict):
                SUM += s(v)
            else:
                try:
                    SUM += int(v)
                except ValueError:
                    pass
    elif isinstance(o, list):
        for v in o:
            if isinstance(v, list) or isinstance(v, dict):
                SUM += s(v)
            else:
                try:
                    SUM += int(v)
                except ValueError:
                    pass
    else:
        raise NotImplementedError
    return SUM

print(s(j))
