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
    id: int
    x: int
    y: int
    dir: Direction
    next_turn: Turn

    def __hash__(self):
        return self.id


def print_(sd, carts):
    print('\033[0;0H')
    for x, line in enumerate(sd):
        o = ''
        for y, ch in enumerate(line):
            for c in carts:
                if c.x == x and c.y == y:
                    o += CARTCHAR[c.dir]
                    break
            else:
                o += ch
        print(o)


def solve(data):
    sd = []
    for line in data.split('\n'):
        sd.append(list(line))
    carts = []
    i = 0
    for x, line in enumerate(sd):
        for y, ch in enumerate(line):
            if ch in {'<', '>'}:
                sd[x][y] = '-'
            elif ch in {'^', 'v'}:
                sd[x][y] = '|'
            else:
                continue
            carts.append(Cart(i, x, y, Direction(ch), Turn.LEFT))
            i += 1
    # print_(sd, carts)

    while True:
        deleted = set()
        if len(carts) == 1:
            return f"{carts[0].y},{carts[0].x}"
        for cart in sorted(carts, key=lambda cart: (cart.x, cart.y)):
            if cart in deleted:
                continue
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
            for other_cart in carts:
                if other_cart is not cart and cart.x == other_cart.x and cart.y == other_cart.y:
                    deleted.add(cart)
                    deleted.add(other_cart)
                    carts.remove(cart)
                    carts.remove(other_cart)
        # look for crashes
        #look_again = True
        #while look_again:
        #    look_again = False
        #    for cart1, cart2 in itertools.permutations(carts, 2):
        #        if cart1.x == cart2.x and cart1.y == cart2.y:
        #            carts.remove(cart1)
        #            carts.remove(cart2)
        #            look_again = True
        #            break

        # print_(sd, carts)
        # import time
        # time.sleep(0.2)


test_data = r"""/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/
"""
test_output = solve(test_data)
test_expected = "6,4"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data))
