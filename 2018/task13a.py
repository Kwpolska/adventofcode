#!/usr/bin/env python3
import enum
import itertools
from dataclasses import dataclass


with open("input/13.txt") as fh:
    file_data = fh.read()


class Direction(enum.Enum):
    LEFT = '<'
    RIGHT = '>'
    UP = '^'
    DOWN = 'v'


class Turn(enum.Enum):
    LEFT = 1
    STRAIGHT = 2
    RIGHT = 3


NEXT_TURN = {Turn.LEFT: Turn.STRAIGHT, Turn.STRAIGHT: Turn.RIGHT, Turn.RIGHT: Turn.LEFT}
# / slash
SLASH = {Direction.UP: Direction.RIGHT,
         Direction.RIGHT: Direction.UP,
         Direction.DOWN: Direction.LEFT,
         Direction.LEFT: Direction.DOWN}
# \ backslash
BACKSLASH = {Direction.UP: Direction.LEFT,
             Direction.LEFT: Direction.UP,
             Direction.DOWN: Direction.RIGHT,
             Direction.RIGHT: Direction.DOWN}

DX = {Direction.UP: -1, Direction.DOWN: 1}
DY = {Direction.LEFT: -1, Direction.RIGHT: 1}

CARTCHAR = {Direction.UP: '^', Direction.DOWN: 'v',
            Direction.LEFT: '<', Direction.RIGHT: '>'}

LEFT_TURN = {Direction.UP: Direction.LEFT,
             Direction.DOWN: Direction.RIGHT,
             Direction.LEFT: Direction.DOWN,
             Direction.RIGHT: Direction.UP}

RIGHT_TURN = {Direction.UP: Direction.RIGHT,
              Direction.DOWN: Direction.LEFT,
              Direction.LEFT: Direction.UP,
              Direction.RIGHT: Direction.DOWN}

@dataclass()
class Cart:
    x: int
    y: int
    dir: Direction
    next_turn: Turn


def print_(sd, carts):
    for x, line in enumerate(sd):
        for y, ch in enumerate(line):
            for c in carts:
                if c.x == x and c.y == y:
                    print(CARTCHAR[c.dir], end='')
                    break
            else:
                print(ch, end='')
        print()


def solve(data):
    sd = []
    # for line in data.strip().split('\n'):
    for line in data.split('\n'):
        sd.append(list(line))
    carts = []
    for x, line in enumerate(sd):
        for y, ch in enumerate(line):
            if ch in {'<', '>'}:
                sd[x][y] = '-'
            elif ch in {'^', 'v'}:
                sd[x][y] = '|'
            else:
                continue
            carts.append(Cart(x, y, Direction(ch), Turn.LEFT))
    # print_(sd, carts)

    while True:
        for cart in sorted(carts, key=lambda cart: (cart.x, cart.y)):
            x, y = cart.x, cart.y
            if sd[x][y] == '+':
                # intersection
                if cart.next_turn == Turn.LEFT:
                    cart.dir = LEFT_TURN[cart.dir]
                elif cart.next_turn == Turn.RIGHT:
                    cart.dir = RIGHT_TURN[cart.dir]
                cart.next_turn = NEXT_TURN[cart.next_turn]
            elif sd[x][y] == '/':
                # direction change
                cart.dir = SLASH[cart.dir]
            elif sd[x][y] == '\\':
                # direction change
                cart.dir = BACKSLASH[cart.dir]
            cart.x += DX.get(cart.dir, 0)
            cart.y += DY.get(cart.dir, 0)
        # look for crashes
        for cart1, cart2 in itertools.permutations(carts, 2):
            if cart1.x == cart2.x and cart1.y == cart2.y:
                return f"{cart1.y},{cart1.x}"

        # print_(sd, carts)
        # import time
        # time.sleep(0.1)


test_data = r"""/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   
"""
test_output = solve(test_data)
test_expected = "7,3"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
