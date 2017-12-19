#!/usr/bin/env python3
with open("input/19.txt") as fh:
    file_data = fh.read()

DOWN = (1, 0)
UP = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
NEXTDIR = {
    DOWN: (LEFT, RIGHT),
    UP: (LEFT, RIGHT),
    LEFT: (UP, DOWN),
    RIGHT: (UP, DOWN),
}


def go(position: tuple, direction: tuple) -> tuple:
    p1, p2 = position
    d1, d2 = direction
    return p1 + d1, p2 + d2


def at(position: tuple, map: list) -> str:
    x, y = position
    try:
        return map[x][y]
    except:
        print(position, "??")
        raise


def is_valid(symbol: str) -> bool:
    return symbol in ('|', '-', '+') or symbol.isalpha()


def solve(data: str, start: int):
    lines = data.split('\n')
    direction = DOWN
    position = (0, start)
    count = 0
    while True:
        symbol = at(position, lines)
        count += 1
        print(position, symbol)
        if not is_valid(symbol):
            count -= 1
            print("End condition", symbol, position)
            return count
        elif symbol == '|' or symbol == '-' or symbol.isalpha():
            # Go ahead.
            position = go(position, direction)
        elif symbol == '+':
            # Go somewhere else.
            for possible_dir in NEXTDIR[direction]:
                possible_position = go(position, possible_dir)
                if is_valid(at(possible_position, lines)):
                    position = possible_position
                    direction = possible_dir
                    break
            else:
                print("Nowhere to go", position)
                return count
        else:
            print("Invalid symbol", position, symbol)

    return data


test_data = """\
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 

"""
test_output = solve(test_data, 5)
test_expected = 38
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data, 13))
