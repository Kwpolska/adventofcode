#!/usr/bin/python3
import itertools
import re
import kwpbar

r = re.compile("([A-Za-z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")

class Ingredient(object):
    name = ""
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

INGREDIENTS = []

# Read ingredient information
with open('15-input.txt') as fh:
    for l in fh:
        data = r.match(l.strip())
        i = Ingredient(*data.groups())
        INGREDIENTS.append(i)

best_score = 0
#best_set = []

tested = 0
pbar_max = 176851

for cookie in itertools.combinations_with_replacement(INGREDIENTS, 100):
    kwpbar.pbar(tested, pbar_max)
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    for i in cookie:
        capacity += i.capacity
        durability += i.durability
        flavor += i.flavor
        texture += i.texture
        calories += i.calories

    tested += 1
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        continue
    if calories != 500: # Part 2
        continue
    score = capacity * durability * flavor * texture
    if score > best_score:
        best_score = score

print('\n{0}'.format(best_score))
