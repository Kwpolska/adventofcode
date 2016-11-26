#!/usr/bin/python
a = input()
up = a.count("(")
down = a.count(")")
print("up", up)
print("down", down)
print("TOTAL", up - down)
