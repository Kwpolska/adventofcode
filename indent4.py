#!/usr/bin/env python3
import textwrap
import sys
if len(sys.argv) != 2:
    print("usage: ./indent4.py FILENAME")
    exit(2)
else:
    with open(sys.argv[1]) as fh:
        print(textwrap.indent(fh.read(), 4 * ' '))
